```python
# Лабораторная работа №9. Исследование функций на Python
# Простое решение всех упражнений

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


# ---------- УПРАЖНЕНИЕ 1 ----------
# y = (x^4 + 2x^2 + x + 2) / (x^3 + 2x^2 + x + 2)

def f1(x):
    return (x**4 + 2*x**2 + x + 2) / (x**3 + 2*x**2 + x + 2)

x = np.linspace(-10, 10, 2000)
y = f1(x)
y[np.abs(y) > 50] = np.nan  # обрезаем у разрывов

plt.figure()
plt.plot(x, y)
plt.grid()
plt.title("Упражнение 1")
plt.show()

# нули
print("Нули упражнения 1:")
for i in range(len(x)-1):
    if y[i]*y[i+1] < 0:
        print("  x =", round(optimize.brentq(f1, x[i], x[i+1]), 4))

# производные через конечные разности
dy = np.gradient(y, x)
d2y = np.gradient(dy, x)

# экстремумы — где dy меняет знак
print("Экстремумы упражнения 1:")
for i in range(1, len(x)-1):
    if dy[i-1]*dy[i] < 0:
        print("  x =", round(x[i], 4), " y =", round(f1(x[i]), 4))

# точки перегиба — где d2y меняет знак
print("Точки перегиба упражнения 1:")
for i in range(1, len(x)-1):
    if d2y[i-1]*d2y[i] < 0:
        print("  x =", round(x[i], 4))

print("Асимптота: y = x")
print()


# ---------- УПРАЖНЕНИЕ 2 ----------
# Распределение Максвелла

def maxwell(x, beta=1):
    return np.where(x > 0, np.sqrt(2/np.pi) * beta**1.5 * x**2 * np.exp(-beta*x**2/2), 0)

x = np.linspace(0, 6, 1000)
plt.figure()
plt.plot(x, maxwell(x, 1))
plt.grid()
plt.title("Упражнение 2: распределение Максвелла, β=1")
plt.show()

print("Упражнение 2:")
print("  Нуль: x = 0")
print("  Асимптота: y = 0 при x → +∞")

# максимум
res = optimize.fmin(lambda t: -maxwell(t, 1), 1.0, disp=False)
print("  Максимум: x =", round(res[0], 4), " f =", round(maxwell(res[0], 1), 4))

# влияние beta
plt.figure()
for b in [0.5, 1, 2, 4]:
    plt.plot(x, maxwell(x, b), label=f"β={b}")
plt.legend()
plt.grid()
plt.title("Влияние β")
plt.show()
print("  С ростом β график сужается и растёт, максимум смещается влево.")
print()


# ---------- УПРАЖНЕНИЕ 3 ----------
# y = sqrt((x^3 - 2x^2)/(x - 3))

def f3(x):
    v = (x**3 - 2*x**2) / (x - 3)
    return np.where(v >= 0, np.sqrt(np.maximum(v, 0)), np.nan)

x1 = np.linspace(-5, 2.5, 1000)   # левая ветвь
x2 = np.linspace(3.1, 8, 1000)    # правая ветвь

plt.figure()
plt.plot(x1, f3(x1))
plt.plot(x2, f3(x2))
plt.grid()
plt.title("Упражнение 3")
plt.show()

print("Упражнение 3:")
print("  Область определения: x ≤ 2 или x > 3")
print("  Нули: x = 0, x = 2")
print("  Вертикальная асимптота: x = 3")
print("  Наклонная асимптота при x → +∞: y ≈ x + 0.5")

dy = np.gradient(f3(x2), x2)
print("  Стационарные точки на x > 3:")
for i in range(1, len(x2)-1):
    if dy[i-1]*dy[i] < 0:
        print("    x =", round(x2[i], 4), " y =", round(f3(x2[i]), 4))
print()


# ---------- УПРАЖНЕНИЕ 4 ----------
# f(x) = e^(-x) * sin(3πx) на [0; 2]

def f4(x):
    return np.exp(-x) * np.sin(3*np.pi*x)

x = np.linspace(0, 2, 2000)
plt.figure()
plt.plot(x, f4(x))
plt.grid()
plt.title("Упражнение 4: экстремумы")
plt.show()

dy = np.gradient(f4(x), x)

print("Упражнение 4:")
print("  Локальные максимумы:")
for i in range(1, len(x)-1):
    if dy[i-1] > 0 and dy[i] < 0:
        print("    x =", round(x[i], 4), " f =", round(f4(x[i]), 4))
        plt.plot(x[i], f4(x[i]), 'ro')

print("  Локальные минимумы:")
for i in range(1, len(x)-1):
    if dy[i-1] < 0 and dy[i] > 0:
        print("    x =", round(x[i], 4), " f =", round(f4(x[i]), 4))
        plt.plot(x[i], f4(x[i]), 'go')
print()


# ---------- УПРАЖНЕНИЕ 5 ----------
# f(x) = sin x - x^2 cos x на [-10; 10]
# точки перегиба — нули второй производной

def f5(x):
    return np.sin(x) - x**2 * np.cos(x)

x = np.linspace(-10, 10, 4000)
y = f5(x)
d2y = np.gradient(np.gradient(y, x), x)

plt.figure()
plt.plot(x, y)
plt.grid()
plt.title("Упражнение 5: точки перегиба")
plt.show()

print("Упражнение 5: точки перегиба")
for i in range(1, len(x)-1):
    if d2y[i-1]*d2y[i] < 0:
        print("  x =", round(x[i], 4), " f =", round(f5(x[i]), 4))
        plt.plot(x[i], f5(x[i]), 'ro')
print()


# ---------- УПРАЖНЕНИЕ 6 ----------
# f(x) = e^(1/(x^2-1))

def f6(x):
    with np.errstate(divide='ignore', over='ignore'):
        return np.exp(1/(x**2 - 1))

# три куска графика
x1 = np.linspace(-4, -1.05, 1000)
x2 = np.linspace(-0.95, 0.95, 1000)
x3 = np.linspace(1.05, 4, 1000)

plt.figure()
plt.plot(x1, np.clip(f6(x1), 0, 50))
plt.plot(x2, f6(x2))
plt.plot(x3, np.clip(f6(x3), 0, 50))
plt.grid()
plt.title("Упражнение 6")
plt.show()

print("Упражнение 6:")
print("  Нулей нет")
print("  Точки разрыва: x = -1 и x = 1")
print("  f(-1⁻) = +∞, f(-1⁺) = 0")
print("  f(1⁻) = 0, f(1⁺) = +∞")
print("  Вертикальные асимптоты: x = -1, x = 1")
print("  Горизонтальная асимптота: y = 1")

# экстремум
res = optimize.fmin(f6, 0.5, disp=False)
print("  Минимум: x =", round(res[0], 4), " f =", round(f6(res[0]), 4))

# точки перегиба
x = np.linspace(-3, 3, 4000)
y = f6(x)
y[np.abs(y) > 100] = np.nan
d2y = np.gradient(np.gradient(y, x), x)

print("  Точки перегиба:")
for i in range(1, len(x)-1):
    if not np.isnan(d2y[i]) and d2y[i-1]*d2y[i] < 0:
        print("    x =", round(x[i], 4), " f =", round(f6(x[i]), 4))
```
