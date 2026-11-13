import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    idx = 1

    stats = {}
    total_seconds = {}

    for _ in range(n):
        phone = input_data[idx]
        date = input_data[idx+1]
        duration = int(input_data[idx+2])
        idx += 3

        month = int(date.split('.')[1])

        total_seconds[phone] = total_seconds.get(phone, 0) + duration

        if phone not in stats:
            stats[phone] = {}
        
        stats[phone][month] = stats[phone].get(month, 0) + duration

    best_phone = max(total_seconds, key=total_seconds.get)
    phone_months = stats[best_phone]
    best_month = max(phone_months, key=phone_months.get)

    print(f"{best_phone} {best_month}")

if __name__ == "__main__":
    solve()
