#3 АВТОРИЗАЦИЯ НА САЙТЕ, РАБОТА С КУКИ И СЕССИЕЙ

import requests
from bs4 import BeautifulSoup as bs4

# Будем хранить куки как БРАУЗЕР
session = requests.Session()


login_link = "https://quotes.toscrape.com/login"

response = session.get(login_link)

print("Статус загрузки сайта: ", response.status_code)


# Мы качаем HTML, и за счет второго парметра мы ЧИТАЕМ этот файл
# pumping = качаем
pumping = bs4(response.text, "html.parser")

# find - ищет первый элемент на странице котокрый подходит под мои УСЛОВИЯ
# ЕСТЬ еще find_all - он ищет все элементы, которые СООТВЕТСВУЮТ условию
# и выводит их СПИСКОМ
# Первый параметр находит именно ТЕГ, а второй парметр (ключ=значения)
hidden_input = pumping.find("input", {"type": "hidden"})

# После найденого поля, достаем сам ТОКЕН, из атрибута VALUE
token = hidden_input["value"]
print("Найденный токен: ", token)


login_data = {
    "csrf_token": token,
    "username": "admin",
    "password": "1234"
}

post_response = session.post(login_link, data=login_data)

print("Статус отправки формы: ", post_response.status_code)



# 6. Проверяем главную страницу через СЕССИЮ
main_page = session.get("https://quotes.toscrape.com/")

if "Logout" in main_page.text:
    print("Мы авторизованы!") 
    with open("1.html", "w", encoding="UTF-8") as file:
        file.write(main_page.text)
    print("\nФайл скачан!") 
else:
    print("Ошибка авторизации!")
