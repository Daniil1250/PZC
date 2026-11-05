# ============================================================
# Лабораторная работа №9. Исследование поведения и свойств функций
# ============================================================

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from scipy.misc import derivative


def find_roots(func, a, b, n=2000):
    """Поиск нулей функции на отрезке [a, b] методом brentq."""
    xs = np.linspace(a, b, n)
    roots = []
    for i in range(len(xs) - 1):
        try:
            f1, f2 = func(xs[i]), func(xs[i + 1])
            if f1 * f2 < 0:
                roots.append(optimize.brentq(func, xs[i], xs[i + 1]))
        except Exception:
            pass
    return roots


# ============================================================
# УПРАЖНЕНИЕ 1
# y = (x^4 + 2x^2 + x + 2) / (x^3 + 2x^2 + x + 2)
# ============================================================
print("=" * 60)
print("УПРАЖНЕНИЕ 1")
print("=" * 60)

def f1(x):
    return (x**4 + 2*x**2 + x + 2) / (x**3 + 2*x**2 + x + 2)

# Область определения
den_roots = np.roots([1, 2, 1, 2])
real_den = [r.real for r in den_roots if abs(r.imag) < 1e-9]
print("Корни знаменателя (точки разрыва):", real_den if real_den else "нет действительных")
print("Область определения: x ≠", real_den if real_den else "R")

# Графики на разных промежутках
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for ax, (a, b) in zip(axes, [(-10, -2), (-2, 2), (2, 10)]):
    x = np.linspace(a, b, 1000)
    y = f1(x)
    y = np.where(np.abs(y) < 50, y, np.nan)
    ax.plot(x, y)
    ax.grid(True)
    ax.set_title(f"x ∈ [{a}, {b}]")
plt.tight_layout()
plt.show()

# Нули функции
roots1 = find_roots(f1, -10, 10)
print("Нули функции:", [f"{r:.6f}" for r in roots1])

# Производные
def df1(x):
    return derivative(f1, x, dx=1e-6)
def d2f1(x):
    return derivative(df1, x, dx=1e-6)

stat1 = find_roots(df1, -10, 10)
print("Стационарные точки:")
for s in stat1:
    print(f"  x={s:.4f}, f={f1(s):.4f}, f''={d2f1(s):.4f}")

infl1 = find_roots(d2f1, -10, 10)
print("Точки перегиба:")
for p in infl1:
    print(f"  x={p:.4f}, f={f1(p):.4f}")

print("Наклонная асимптота: y = x (при x → ±∞)")
print()


# ============================================================
# УПРАЖНЕНИЕ 2
# Распределение Максвелла
# ============================================================
print("=" * 60)
print("УПРАЖНЕНИЕ 2")
print("=" * 60)

def maxwell(x, beta=1.0):
    return np.where(x > 0, np.sqrt(2 / np.pi) * beta**1.5 * x**2 * np.exp(-beta * x**2 / 2), 0.0)

# а) β = 1
x = np.linspace(0, 6, 1000)
plt.figure(figsize=(8, 5))
plt.plot(x, maxwell(x), label="f(x), β=1")

res = optimize.fmin(lambda t: -maxwell(t), 1.0, full_output=True, disp=False)
x_max = res[0][0]
print(f"Нуль функции: x = 0")
print(f"Точка максимума: x = {x_max:.4f}, f = {maxwell(x_max):.4f}")
plt.plot(x_max, maxwell(x_max), 'ro', label=f"max ({x_max:.3f}, {maxwell(x_max):.3f})")

def d2maxwell(x):
    return derivative(lambda t: maxwell(t), x, dx=1e-6, n=2)

infl2 = find_roots(d2maxwell, 0.1, 6)
print("Точки перегиба:")
for p in infl2:
    print(f"  x={p:.4f}, f={maxwell(p):.4f}")
    plt.plot(p, maxwell(p), 'go', label=f"перегиб x={p:.3f}")

plt.axhline(0, color='k', linewidth=0.8)
plt.legend()
plt.grid(True)
plt.title("Распределение Максвелла, β=1")
plt.show()
print("Горизонтальная асимптота: y = 0 при x → +∞")

# б) Влияние β
plt.figure(figsize=(8, 5))
for beta in [0.5, 1.0, 2.0, 4.0]:
    plt.plot(x, maxwell(x, beta), label=f"β={beta}")
plt.grid(True)
plt.legend()
plt.title("Влияние параметра β")
plt.show()
print("С ростом β максимум смещается влево и растёт, график становится уже.")
print()


# ============================================================
# УПРАЖНЕНИЕ 3
# y = sqrt((x^3 - 2x^2)/(x - 3))
# ============================================================
print("=" * 60)
print("УПРАЖНЕНИЕ 3")
print("=" * 60)

def f3(x):
    val = (x**3 - 2*x**2) / (x - 3)
    return np.where(val >= 0, np.sqrt(np.maximum(val, 0)), np.nan)

print("Область определения: x ≤ 2 или x > 3 (x ≠ 3)")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
for ax, (a, b) in zip(axes, [(-3, 2.5), (3.1, 8)]):
    x = np.linspace(a, b, 1000)
    ax.plot(x, f3(x))
    ax.grid(True)
    ax.set_title(f"x ∈ [{a}, {b}]")
plt.tight_layout()
plt.show()

print("Нули функции: x = 0, x = 2")

def g3(x):
    v = (x**3 - 2*x**2) / (x - 3)
    return np.sqrt(v) if v >= 0 else np.nan

stat3 = find_roots(lambda t: derivative(g3, t, dx=1e-6), 3.1, 8)
print("Стационарные точки:")
for s in stat3:
    print(f"  x={s:.4f}, y={g3(s):.4f}")

print("Вертикальная асимптота: x = 3")
print("Наклонная асимптота при x → +∞: y ≈ x + 0.5")
print()


# ============================================================
# УПРАЖНЕНИЕ 4
# f(x) = e^(-x) sin(3πx) на [0; 2]
# ============================================================
print("=" * 60)
print("УПРАЖНЕНИЕ 4")
print("=" * 60)

def f4(x):
    return np.exp(-x) * np.sin(3 * np.pi * x)

x = np.linspace(0, 2, 2000)
plt.figure(figsize=(10, 5))
plt.plot(x, f4(x), label="f(x) = e^(-x)·sin(3πx)")
plt.grid(True)

extrema = []
for k in range(-1, 7):
    xk = (np.arctan(3 * np.pi) + np.pi * k) / (3 * np.pi)
    if 0 <= xk <= 2:
        extrema.append(xk)

maxima, minima = [], []
for e in extrema:
    if f4(e) > f4(e - 0.01) and f4(e) > f4(e + 0.01):
        maxima.append(e)
    elif f4(e) < f4(e - 0.01) and f4(e) < f4(e + 0.01):
        minima.append(e)

print("Локальные максимумы:")
for m in maxima:
    print(f"  x = {m:.4f}, f = {f4(m):.4f}")
    plt.plot(m, f4(m), 'ro')

print("Локальные минимумы:")
for m in minima:
    print(f"  x = {m:.4f}, f = {f4(m):.4f}")
    plt.plot(m, f4(m), 'go')

plt.legend()
plt.title("Экстремумы f(x) = e^(-x)·sin(3πx)")
plt.show()
print()


# ============================================================
# УПРАЖНЕНИЕ 5
# f(x) = sin x - x^2 cos x на [-10; 10]
# ============================================================
print("=" * 60)
print("УПРАЖНЕНИЕ 5")
print("=" * 60)

def f5(x):
    return np.sin(x) - x**2 * np.cos(x)

def d2f5(x):
    return derivative(f5, x, dx=1e-6, n=2)

infl5 = find_roots(d2f5, -10, 10)
print("Точки перегиба на [-10, 10]:")
for p in infl5:
    print(f"  x = {p:.6f}, f(x) = {f5(p):.6f}")

x = np.linspace(-10, 10, 2000)
plt.figure(figsize=(12, 5))
plt.plot(x, f5(x), label="f(x) = sin x − x²cos x")
for p in infl5:
    plt.plot(p, f5(p), 'ro', markersize=5)
plt.grid(True)
plt.legend()
plt.title("Точки перегиба")
plt.show()
print()


# ============================================================
# УПРАЖНЕНИЕ 6
# f(x) = e^(1/(x^2-1))
# ============================================================
print("=" * 60)
print("УПРАЖНЕНИЕ 6")
print("=" * 60)

def f6(x):
    with np.errstate(divide='ignore', over='ignore'):
        return np.exp(1 / (x**2 - 1))

print("Нулей нет (функция всюду положительна)")
print("Точки разрыва: x = -1, x = 1")
for x0 in [-1, 1]:
    print(f"  f({x0}⁻) = {f6(x0 - 1e-6)}")
    print(f"  f({x0}⁺) = {f6(x0 + 1e-6)}")
print("Пределы при x → ±∞: f(x) → 1")

def df6(x):
    return derivative(f6, x, dx=1e-7)
def d2f6(x):
    return derivative(f6, x, dx=1e-5, n=2)

stat6 = find_roots(df6, -5, 5)
print("Стационарные точки:")
for s in stat6:
    print(f"  x={s:.6f}, f={f6(s):.6f}, f''={d2f6(s):.4f}")

infl6 = find_roots(d2f6, -5, 5)
print("Точки перегиба:")
for p in infl6:
    print(f"  x={p:.6f}, f={f6(p):.6f}, tg угла наклона = {df6(p):.6f}")

print("Асимптоты:")
print("  Вертикальные: x = -1, x = 1")
print("  Горизонтальная: y = 1")

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for ax, (a, b) in zip(axes, [(-4, -1.05), (-0.95, 0.95), (1.05, 4)]):
    x = np.linspace(a, b, 1000)
    y = np.clip(f6(x), 0, 50)
    ax.plot(x, y)
    ax.grid(True)
    ax.set_title(f"x ∈ [{a:.2f}, {b:.2f}]")
plt.tight_layout()
plt.show()

print("=" * 60)
print("РАБОТА ЗАВЕРШЕНА")
print("=" * 60)
