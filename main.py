import sys

def solve():
    f = sys.stdin
    first_line = f.readline()
    if not first_line:
        return
    n = int(first_line)

    totals = {}
    lines = []

    for _ in range(n):
        line = f.readline()
        if not line:
            break
        lines.append(line)
        parts = line.split()
        
        phone = int(parts[0])
        sec = int(parts[2])

        totals[phone] = totals.get(phone, 0) + sec

    best_phone = max(totals, key=totals.get)

    months = [0] * 13

    for line in lines:
        parts = line.split()
        phone = int(parts[0])
        
        if phone == best_phone:
            month = int(parts[1][3:5])
            sec = int(parts[2])
            months[month] += sec

    best_month = 0
    max_sec = -1
    for m in range(1, 13):
        if months[m] > max_sec:
            max_sec = months[m]
            best_month = m

    print(f"+{best_phone} {best_month}")

if __name__ == "__main__":
    solve() 
