import sys

def solve():
    # Читаем все данные из ввода
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    idx = 1

    # Словарь: { номер_телефона: { месяц: сумма_секунд } }
    # И общий словарь для подсчета всех секунд абонента
    stats = {}
    total_seconds = {}

    for _ in range(n):
        phone = input_data[idx]
        date = input_data[idx+1]
        duration = int(input_data[idx+2])
        idx += 3

        # Извлекаем месяц из даты (формат DD.MM.2021)
        # Дата: "06.12.2021" -> split('.') -> ['06', '12', '2021'] -> месяц это индекс 1
        month = int(date.split('.')[1])

        # Считаем общее время абонента
        total_seconds[phone] = total_seconds.get(phone, 0) + duration

        # Считаем время по месяцам для конкретного абонента
        if phone not in stats:
            stats[phone] = {}
        
        stats[phone][month] = stats[phone].get(month, 0) + duration

    # Находим самого болтливого абонента (максимальная сумма секунд)
    # Если несколько абонентов наговорили одинаково, берем любого (или первого по алфавиту, но в задаче не уточняется)
    best_phone = max(total_seconds, key=total_seconds.get)

    # Теперь среди месяцев этого абонента находим самый болтливый месяц
    phone_months = stats[best_phone]
    
    # Находим месяц с максимальным количеством секунд
    # Если несколько месяцев имеют одинаковое время, берем тот, что меньше по номеру (обычно так в задачах)
    best_month = max(phone_months, key=phone_months.get)

    # Выводим результат
    print(f"{best_phone} {best_month}")

if __name__ == "__main__":
    solve()
