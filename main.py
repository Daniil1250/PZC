import sys

def solve():
    f = sys.stdin
    first_line = f.readline()
    if not first_line:
        return
    n = int(first_line)

    totals = {}
    month_data = {}

    for _ in range(n):
        parts = f.readline().split()
        if not parts:
            continue
        phone = int(parts[0])
        month = int(parts[1][3:5])
        sec = int(parts[2])

        totals[phone] = totals.get(phone, 0) + sec
        
        if phone not in month_data:
            month_data[phone] = {}
        month_data[phone][month] = month_data[phone].get(month, 0) + sec

    best_phone = max(totals, key=totals.get)
    best_month = max(month_data[best_phone], key=month_data[best_phone].get)

    print(f"+{best_phone} {best_month}")

if __name__ == "__main__":
    solve()
