import time
from playwright.sync_api import sync_playwright

def parse_wb_orders():
    with sync_playwright() as p:
        # 1. Открываем браузер (headless=False, чтобы видеть, что происходит)
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        print("1. Открываем страницу входа Wildberries...")
        page.goto("https://www.wildberries.ru/")
        time.sleep(3)

        # 2. Нажимаем кнопку "Войти"
        print("2. Кликаем 'Войти'...")
        try:
            # Кнопка входа в шапке сайта (селектор может меняться, проверь в DevTools)
            page.click("text=Войти", timeout=10000)
            time.sleep(2)
        except:
            print("Кнопка 'Войти' не найдена. Возможно, ты уже авторизован.")

        # 3. Вводим номер телефона (замени на свой)
        print("3. Вводим номер телефона...")
        phone = "+79001234567"  # <-- ЗАМЕНИ НА СВОЙ НОМЕР
        try:
            # Поле ввода телефона
            page.fill("input[type='tel']", phone)
            time.sleep(1)
            page.click("text=Получить код")
            print("Код отправлен на номер. Ждём SMS...")
        except Exception as e:
            print(f"Ошибка при вводе номера: {e}")

        # 4. ЖДЁМ ВВОДА КОДА ВРУЧНУЮ (скрипт просто спит, пока ты вводишь)
        print("\n>>> ВВЕДИ КОД ИЗ SMS В БРАУЗЕРЕ ВРУЧНУЮ <<<")
        print("Скрипт ждёт 120 секунд...")
        time.sleep(120)

        # 5. Проверяем, что вошли (ищем кнопку профиля или имя)
        print("\n4. Проверяем авторизацию...")
        if "Личный кабинет" in page.content() or "Профиль" in page.content():
            print("Авторизация успешна!")

            # 6. Сохраняем сессию (cookies + localStorage)
            context.storage_state(path="wb_session.json")
            print("Сессия сохранена в wb_session.json")

            # 7. Переходим на страницу заказов
            print("5. Переходим на страницу заказов...")
            page.goto("https://www.wildberries.ru/lk/myorders/archive")
            time.sleep(3)

            # 8. Парсим заказы (простой пример — ищем карточки)
            print("6. Парсим данные...")
            html = page.content()
            
            # Сохраняем HTML для отладки — посмотри, какие классы реально там
            with open("wb_orders.html", "w", encoding="utf-8") as f:
                f.write(html)
            print("HTML сохранён в wb_orders.html — открой и посмотри классы карточек.")

        else:
            print("Авторизация не удалась. Проверь, вошёл ли ты в браузере.")

        browser.close()

if __name__ == "__main__":
    parse_wb_orders()
