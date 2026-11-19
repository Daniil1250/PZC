import sqlite3 as sql
import asyncio 
from ddgs import DDGS
from playwright.async_api import async_playwright 
import random
from bs4 import BeautifulSoup
import re


KEYWORDS = ["брови", "макияж", "укладка", "стрижка", "уход", "маникюр", "педикюр", "окрашивание", "эпиляция", "шугаринг", "массаж", "чистка", "маска"]


CARD_CLASS = "related-product-view _size_normal" 

async def human_delay(min_sec=2, max_sec=4):
    await asyncio.sleep(random.uniform(min_sec, max_sec))

async def main():
    print("1. Ищем ссылки на Яндекс.Карты...")
    urls_to_parse = []
    query = "site:yandex.ru/maps/org/ салон красоты Москва"
    
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=30))

    for res in results:
        link = res['href']
        if "yandex.ru/maps/org/" in link:
            clean_link = link.split('?')[0]
            if clean_link not in urls_to_parse:
                urls_to_parse.append(clean_link)

    print(f"Найдено ссылок: {len(urls_to_parse)}")
    
    conn = sql.connect('crm.db')
    cursor = conn.cursor()

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        count_saved = 0
        target_salons = 2 

        for url in urls_to_parse:
            if count_saved >= target_salons:
                break

            print(f"\n--- Проверяем: {url} ---")
            try:
                await page.goto(url, wait_until="domcontentloaded")
                await human_delay()

                cursor.execute("SELECT id FROM competitors WHERE url = ?", (url,))
                if cursor.fetchone():
                    print("  [Пропуск] Уже в базе.")
                    continue

                html_content = await page.content()
                soup = BeautifulSoup(html_content, "html.parser")

                salon_name_tag = soup.find("h1")
                salon_name = salon_name_tag.text.strip() if salon_name_tag else "Неизвестный салон"

                print("  Ищем ссылку с 'prices' в href...")
                price_url = None
                
                for a_tag in soup.find_all("a", href=True):
                    if "prices" in a_tag["href"]:
                        price_url = a_tag["href"]
                        break

                if price_url:
                    if price_url.startswith("/"):
                        full_price_url = f"https://yandex.ru{price_url}"
                    else:
                        full_price_url = price_url
                        
                    print(f"  Нашли ссылку: {full_price_url}")
                    print("  Переходим...")
                    await page.goto(full_price_url, wait_until="domcontentloaded")
                    await human_delay(3, 5)
                else:
                    print("  [ПРОПУСК] Ссылка на цены не найдена.")
                    continue

                
                print("  Парсим услуги и цены...")
                html_prices = await page.content()
                soup_prices = BeautifulSoup(html_prices, "html.parser")

                services_to_save = []

        
                cards = soup_prices.find_all(class_=CARD_CLASS)
                
                if not cards:
                    print(f"  [ВНИМАНИЕ] Карточки не найдены по классу '{CARD_CLASS}'.")
                
                for card in cards:

                    price_tag = card.find(string=lambda text: text and "₽" in text)
                    clean_price = ""
                    
                    if price_tag:
                        clean_price = re.sub(r'[^\d.]', '', price_tag.strip())
                        
                        image_url = card.find("img")["src"]

                        if image_url == None:
                            image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvPUPcFLaankMgzT_TqTByD26zl76G0xyXLOvKnZ3sQw&s=10"

                        name_tag = card.find(["h3", "h4"])
                        
                        if name_tag:
                            service_name = name_tag.text.strip()
                        else:
                            service_name = ""
                            for tag in card.find_all(["span", "div"]):
                                text = tag.text.strip()
                                if text and "₽" not in text and not any(char.isdigit() for char in text):
                                    service_name = text
                                    break
                                    
          
                        if not service_name:
                            service_name = "Неизвестная услуга"

                 
                        description = ""
                        all_text_blocks = card.find_all(["span", "div", "p"])
                        
                        for block in all_text_blocks:
                            text = block.text.strip()
                            if (text != service_name and 
                                "₽" not in text and 
                                text != clean_price and
                                len(text) > 15):
                                description = text
                                break

                        if any(word in service_name.lower() for word in KEYWORDS):
                            services_to_save.append({
                                "name": service_name,
                                "price": clean_price,
                                "description": description, 
                                "image_url": image_url
                            })
                            print(f"    + {service_name} | {clean_price} руб. | {description[:30]}...")

                if services_to_save:
                    cursor.execute("INSERT INTO competitors (name, url) VALUES (?, ?)", (salon_name, url))
                    salon_id = cursor.lastrowid
                    count_saved += 1
                    
                    print(f"  [УСПЕХ] Сохранено услуг: {len(services_to_save)}")
                    for s in services_to_save:
                        cursor.execute(
                            "INSERT INTO prices (competitor_id, service_name, price, description, image_url) VALUES (?, ?, ?, ?, ?)",
                            (salon_id, s["name"], s["price"], s["description"], s["image_url"])
                        )
                else:
                    print("  [ПУСТО] Ничего не нашли по ключевым словам.")

            except Exception as e:
                print(f"  [ОШИБКА] {e}")

        await browser.close()
        conn.commit()
        conn.close()

    print(f"\nГотово! Успешно спарсено салонов: {count_saved}")

if __name__ == "__main__":
    asyncio.run(main())
