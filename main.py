# ============================================================
# ПАРСИНГ ЗАКАЗОВ WILDBERRIES С АВТОРИЗАЦИЕЙ ЧЕРЕЗ SMS
# ============================================================
# Библиотеки: pip install playwright
# Браузер:    playwright install chromium
# ============================================================

import time
from playwright.sync_api import sync_playwright

# --- НАСТРОЙКИ ---
PHONE = "+79001234567"          # <-- ЗАМЕНИ НА СВОЙ НОМЕР
SESSION_FILE = "wb_session.json" # Файл, где храним сессию
ORDERS_URL = "https://www.wildberries.ru/lk/myorders/archive"

def parse_orders():
    with sync_playwright() as p:
        # 1. Запускаем браузер (headless=False — чтобы видеть окно в кадре)
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        print("1. Открываем Wildberries...")
        page.goto("https://www.wildberries.ru/")
        time.sleep(3)

        # 2. Открываем окно входа
        print("2. Открываем форму входа...")
        try:
            # Кнопка "Войти" в шапке. Если селектор изменится — правь здесь.
            page.click("text=Войти", timeout=10000)
            time.sleep(2)
        except:
            print("Кнопка 'Войти' не найдена. Возможно, уже авторизован.")

        # 3. Подставляем номер телефона
        print("3. Вводим номер телефона...")
        try:
            page.fill("input[type='tel']", PHONE)
            time.sleep(1)
            page.click("text=Получить код")
            print("Код отправлен. Проверь телефон.")
        except Exception as e:
            print(f"Ошибка при вводе номера: {e}")

        # 4. ЖДЁМ РУЧНОГО ВВОДА SMS (скрипт спит 120 секунд)
        print("\n>>> ВВЕДИ КОД ИЗ SMS В БРАУЗЕРЕ ВРУЧНУЮ <<<")
        print("Скрипт ждёт 120 секунд...")
        time.sleep(120)

        # 5. Сохраняем сессию (cookies + localStorage)
        print("\n4. Сохраняем сессию...")
        context.storage_state(path=SESSION_FILE)
        print(f"Сессия сохранена в {SESSION_FILE}")

        # 6. Переходим к заказам
        print("5. Переходим на страницу заказов...")
        page.goto(ORDERS_URL)
        time.sleep(3)

        # 7. Парсим заказы (упрощённо — берём текст карточек)
        print("6. Собираем данные...")
        html = page.content()

        # Сохраняем HTML, чтобы ты мог найти актуальные классы
        with open("wb_orders.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("HTML сохранён в wb_orders.html — открой и посмотри классы карточек.")

        # Простой пример: ищем все блоки с классом, содержащим "order"
        # (WB часто меняет верстку, поэтому сначала сохраняем HTML)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")
        cards = soup.find_all(class_=lambda c: c and "order" in c.lower())

        print(f"\nНайдено блоков с 'order' в классе: {len(cards)}")
        for i, card in enumerate(cards[:3], 1):  # покажем первые 3
            text = card.get_text(strip=True)[:100]
            print(f"  Заказ {i}: {text}...")

        print("\nГотово! Браузер закроется через 5 секунд.")
        time.sleep(5)
        browser.close()

if __name__ == "__main__":
    parse_orders()
