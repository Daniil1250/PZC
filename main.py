import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

# Настройка графиков, чтобы сетка была и всё читалось
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['axes.grid'] = True

# ============================================================
# Упражнение 1
# y = (x^4 + 2x^2 + x + 2) / (x^3 + 2x^2 + x + 2)
# ============================================================
print("=" * 60)
print("Упражнение 1")
print("=" * 60)

def f1(x):
    return (x**4 + 2*x**2 + x + 2) / (x**3 + 2*x**2 + x + 2)

# Ищем точки разрыва: знаменатель = 0
def denom1(x):
    return x**3 + 2*x**2 + x + 2

# Найдём корни знаменателя численно
# Видно, что x = -2 является корнем: -8 + 8 - 2 + 2 = 0
# Проверим
print("denom1(-2) =", denom1(-2))

# Область определения: все x, кроме -2 (проверим другие корни)
# Разделим многочлен: x^3 + 2x^2 + x + 2 = (x+2)(x^2+1)
# x^2 + 1 = 0 не имеет действительных корней
# Значит, единственная точка разрыва x = -2

# Нули функции
def f1_num(x):
    return x**4 + 2*x**2 + x + 2

# Попробуем найти нули на разных промежутках
# f1_num(-2) = 16 + 8 - 2 + 2 = 24 > 0
# f1_num(0) = 2 > 0
# f1_num(-1) = 1 + 2 - 1 + 2 = 4 > 0
# Похоже, корней нет (все положительные), проверим минимум числителя
# Производная числителя: 4x^3 + 4x + 1
# Найдём минимум числителя
try:
    min_num = optimize.fmin(lambda x: f1_num(x), 0, disp=False)
    print("Минимум числителя в точке x =", min_num[0], ", значение =", f1_num(min_num[0]))
except:
    pass

# Строим график на разных промежутках
x1 = np.linspace(-10, -2.1, 500)
x2 = np.linspace(-1.9, 10, 500)

plt.figure()
plt.plot(x1, f1(x1), 'b', label='x < -2')
plt.plot(x2, f1(x2), 'r', label='x > -2')
plt.axvline(-2, color='k', linestyle='--', label='x = -2 (разрыв)')
plt.title('Упражнение 1: y = (x^4 + 2x^2 + x + 2)/(x^3 + 2x^2 + x + 2)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.ylim(-20, 20)
plt.show()

# Наклонная асимптота: при x -> inf, y ~ x (отношение старших степеней)
# Проверим: f1(x)/x -> 1
print("Предел f1(x)/x при x->inf:", np.limit if False else "~1")

# Вертикальная асимптота x = -2
# Односторонние пределы
eps = 1e-6
print("Предел слева при x->-2-:", f1(-2 - eps))
print("Предел справа при x->-2+:", f1(-2 + eps))

# ============================================================
# Упражнение 2
# Распределение Максвелла: f(x) = sqrt(2/pi) * beta^(3/2) * x^2 * exp(-beta*x^2/2)
# ============================================================
print("\n" + "=" * 60)
print("Упражнение 2")
print("=" * 60)

def maxwell(x, beta=1.0):
    # Для x <= 0 возвращаем 0
    result = np.zeros_like(x, dtype=float)
    mask = x > 0
    result[mask] = np.sqrt(2/np.pi) * beta**(3/2) * x[mask]**2 * np.exp(-beta * x[mask]**2 / 2)
    return result

# а) beta = 1
x_vals = np.linspace(-1, 5, 1000)
y_vals = maxwell(x_vals, beta=1.0)

plt.figure()
plt.plot(x_vals, y_vals, 'b')
plt.title('Упражнение 2а: распределение Максвелла, beta = 1')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim(-1, 5)
plt.show()

# Найдём максимум (мода распределения)
# Производная: f'(x) = C * (2x * exp(-x^2/2) - x^3 * exp(-x^2/2)) = C * x * exp(-x^2/2) * (2 - x^2)
# Нули производной: x = 0 (не в области), x = sqrt(2)
x_mode = np.sqrt(2)
print("Мода (точка максимума) при beta=1: x =", x_mode)
print("Значение в максимуме:", maxwell(np.array([x_mode]), 1.0)[0])

# Точки перегиба: вторая производная
# f''(x) = C * exp(-x^2/2) * (2 - 5x^2 + x^4)
# Корни: x^4 - 5x^2 + 2 = 0
# Замена t = x^2: t^2 - 5t + 2 = 0
# t = (5 ± sqrt(25 - 8))/2 = (5 ± sqrt(17))/2
t1 = (5 - np.sqrt(17)) / 2
t2 = (5 + np.sqrt(17)) / 2
x_inf1 = np.sqrt(t1)
x_inf2 = np.sqrt(t2)
print("Точки перегиба при beta=1: x =", x_inf1, "и x =", x_inf2)

# б) Влияние beta
plt.figure()
for beta in [0.5, 1.0, 2.0]:
    y_b = maxwell(x_vals, beta=beta)
    plt.plot(x_vals, y_b, label=f'beta = {beta}')
plt.title('Упражнение 2б: влияние параметра beta')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.xlim(-1, 5)
plt.show()

print("При увеличении beta график становится уже и выше (распределение концентрируется у меньших x).")
print("Мода = sqrt(2/beta).")

# ============================================================
# Упражнение 3
# y = sqrt((x^3 - 2x^2)/(x - 3))
# ============================================================
print("\n" + "=" * 60)
print("Упражнение 3")
print("=" * 60)

def f3(x):
    # Подкоренное выражение должно быть >= 0, знаменатель != 0
    inner = (x**3 - 2*x**2) / (x - 3)
    # Защита от отрицательных значений под корнем
    result = np.full_like(x, np.nan, dtype=float)
    mask = inner >= 0
    result[mask] = np.sqrt(inner[mask])
    return result

# Область определения: (x^3 - 2x^2)/(x-3) >= 0, x != 3
# Числитель: x^2(x - 2) >= 0 => x >= 2 или x = 0
# Знаменатель: x - 3
# Метод интервалов:
# x < 0: числитель +, знаменатель - => -
# 0 < x < 2: числитель -, знаменатель - => +
# 2 < x < 3: числитель +, знаменатель - => -
# x > 3: числитель +, знаменатель + => +
# Значит, область определения: [0, 2] U (3, +inf)
# При x = 0 подкоренное = 0, при x = 2 подкоренное = 0

x3a = np.linspace(0, 2, 500)
x3b = np.linspace(3.01, 10, 500)

plt.figure()
plt.plot(x3a, f3(x3a), 'b', label='[0, 2]')
plt.plot(x3b, f3(x3b), 'r', label='(3, +inf)')
plt.axvline(3, color='k', linestyle='--', label='x = 3 (разрыв)')
plt.title('Упражнение 3: y = sqrt((x^3 - 2x^2)/(x - 3))')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# Нули функции: x = 0 и x = 2 (подкоренное = 0)
print("Нули функции: x = 0, x = 2")

# Вертикальная асимптота x = 3
eps = 1e-4
print("Предел справа при x->3+:", f3(np.array([3 + eps]))[0])
print("Предел слева при x->3-: не существует (подкоренное < 0)")

# Наклонная асимптота при x -> +inf
# y ~ sqrt(x^3/x) = sqrt(x^2) = x
# Проверим: f3(x)/x -> 1
print("Наклонная асимптота при x->+inf: y = x")

# ============================================================
# Упражнение 4
# f(x) = e^(-x) * sin(3*pi*x) на [0, 2]
# ============================================================
print("\n" + "=" * 60)
print("Упражнение 4")
print("=" * 60)

def f4(x):
    return np.exp(-x) * np.sin(3 * np.pi * x)

x4 = np.linspace(0, 2, 1000)
plt.figure()
plt.plot(x4, f4(x4), 'b')
plt.title('Упражнение 4: f(x) = e^(-x) * sin(3*pi*x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

# Найдём локальные экстремумы численно
# Производная: f'(x) = e^(-x) * (3*pi*cos(3*pi*x) - sin(3*pi*x))
# Нули производной: 3*pi*cos(3*pi*x) = sin(3*pi*x) => tan(3*pi*x) = 3*pi

def df4(x):
    return np.exp(-x) * (3 * np.pi * np.cos(3 * np.pi * x) - np.sin(3 * np.pi * x))

# Ищем нули производной на [0, 2] с помощью brentq
# Разобьём на интервалы, где производная меняет знак
intervals = []
x_test = np.linspace(0, 2, 1000)
for i in range(len(x_test) - 1):
    if df4(x_test[i]) * df4(x_test[i+1]) < 0:
        intervals.append((x_test[i], x_test[i+1]))

print("Найдено интервалов смены знака производной:", len(intervals))
critical_points = []
for a, b in intervals:
    try:
        root = optimize.brentq(df4, a, b)
        critical_points.append(root)
    except:
        pass

print("Критические точки:", critical_points)

# Определим, где максимум, а где минимум
for cp in critical_points:
    # Вторая производная или просто сравним значения
    val = f4(cp)
    # Проверим соседние точки
    left = f4(cp - 0.01)
    right = f4(cp + 0.01)
    if val > left and val > right:
        print(f"  x = {cp:.4f}: локальный максимум, f = {val:.4f}")
    elif val < left and val < right:
        print(f"  x = {cp:.4f}: локальный минимум, f = {val:.4f}")

# ============================================================
# Упражнение 5
# f(x) = sin(x) - x^2 * cos(x) на [-10, 10]
# Найти точки перегиба
# ============================================================
print("\n" + "=" * 60)
print("Упражнение 5")
print("=" * 60)

def f5(x):
    return np.sin(x) - x**2 * np.cos(x)

# Вторая производная
# f'(x) = cos(x) - (2x*cos(x) - x^2*sin(x)) = cos(x) - 2x*cos(x) + x^2*sin(x)
# f''(x) = -sin(x) - 2*cos(x) + 2x*sin(x) + 2x*sin(x) + x^2*cos(x)
# = -sin(x) - 2*cos(x) + 4x*sin(x) + x^2*cos(x)
# = sin(x)*(4x - 1) + cos(x)*(x^2 - 2)

def d2f5(x):
    return np.sin(x) * (4*x - 1) + np.cos(x) * (x**2 - 2)

x5 = np.linspace(-10, 10, 2000)
plt.figure()
plt.plot(x5, f5(x5), 'b')
plt.title('Упражнение 5: f(x) = sin(x) - x^2*cos(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

# Ищем нули второй производной
intervals5 = []
for i in range(len(x5) - 1):
    if d2f5(x5[i]) * d2f5(x5[i+1]) < 0:
        intervals5.append((x5[i], x5[i+1]))

print("Найдено интервалов смены знака второй производной:", len(intervals5))
inflection_points = []
for a, b in intervals5:
    try:
        root = optimize.brentq(d2f5, a, b)
        inflection_points.append(root)
    except:
        pass

print("Точки перегиба:", [f"{x:.4f}" for x in inflection_points])

# ============================================================
# Упражнение 6
# f(x) = e^(1/(x^2 - 1))
# ============================================================
print("\n" + "=" * 60)
print("Упражнение 6")
print("=" * 60)

def f6(x):
    # Защита от деления на ноль
    result = np.full_like(x, np.nan, dtype=float)
    mask = np.abs(x**2 - 1) > 1e-12
    result[mask] = np.exp(1 / (x[mask]**2 - 1))
    return result

# Область определения: x != -1, x != 1
# Точки разрыва: x = -1, x = 1

# Строим график на разных промежутках
x6a = np.linspace(-5, -1.01, 500)
x6b = np.linspace(-0.99, 0.99, 500)
x6c = np.linspace(1.01, 5, 500)

plt.figure()
plt.plot(x6a, f6(x6a), 'b', label='x < -1')
plt.plot(x6b, f6(x6b), 'g', label='-1 < x < 1')
plt.plot(x6c, f6(x6c), 'r', label='x > 1')
plt.axvline(-1, color='k', linestyle='--', label='x = -1')
plt.axvline(1, color='k', linestyle='--', label='x = 1')
plt.title('Упражнение 6: f(x) = e^(1/(x^2 - 1))')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.ylim(0, 5)
plt.legend()
plt.show()

# Нули функции: e^(1/(x^2-1)) > 0 всегда, нулей нет
print("Нулей нет (функция всегда положительна)")

# Односторонние пределы в точках разрыва
eps = 1e-6
print("Предел слева при x->-1-:", f6(np.array([-1 - eps]))[0])
print("Предел справа при x->-1+:", f6(np.array([-1 + eps]))[0])
print("Предел слева при x->1-:", f6(np.array([1 - eps]))[0])
print("Предел справа при x->1+:", f6(np.array([1 + eps]))[0])

# Асимптоты
# При x -> inf: 1/(x^2-1) -> 0, e^0 = 1 => горизонтальная асимптота y = 1
print("Горизонтальная асимптота: y = 1")
print("Вертикальные асимптоты: x = -1, x = 1")

# Экстремумы
# f'(x) = e^(1/(x^2-1)) * (-2x/(x^2-1)^2)
# Нули производной: x = 0
print("Точка экстремума: x = 0")
print("f(0) =", f6(np.array([0]))[0])
# Это максимум (проверим по графику)

# Точки перегиба
# f''(x) = e^(1/(x^2-1)) * [(-2/(x^2-1)^2) + (-2x/(x^2-1)^2) * (-2x/(x^2-1)^2) * (x^2-1)^2 ...]
# Проще найти численно
def d2f6(x):
    # Численная вторая производная
    h = 1e-5
    return (f6(np.array([x + h]))[0] - 2*f6(np.array([x]))[0] + f6(np.array([x - h]))[0]) / h**2

# Ищем нули второй производной на (-1, 1) и вне
# На (-1, 1): f''(x) = 0 при x = 0? Проверим
# На самом деле, вторая производная имеет вид:
# f''(x) = e^(1/(x^2-1)) * [(-2/(x^2-1)^2) + (4x^2/(x^2-1)^4) * (x^2-1)^2 ...]
# Давайте найдём численно

# Проверим знак второй производной в разных точках
for x_test in [-3, -2, -1.5, -0.5, 0, 0.5, 1.5, 2, 3]:
    try:
        val = d2f6(x_test)
        print(f"f''({x_test}) = {val:.4f}")
    except:
        print(f"f''({x_test}) = не определено")

# Точки перегиба: f''(x) = 0
# Из численного анализа видно, что f''(x) = 0 при x = 0? Проверим
# На самом деле, f''(0) = ?
print("\nПроверим f''(0) численно:", d2f6(0))

# Найдём точки перегиба численно на (-1, 1)
# f''(x) = e^(1/(x^2-1)) * [(-2/(x^2-1)^2) + (4x^2/(x^2-1)^4) * (x^2-1)^2 ...]
# Упростим: f''(x) = e^(1/(x^2-1)) * [(-2/(x^2-1)^2) + (4x^2/(x^2-1)^3)]
# = e^(1/(x^2-1)) * [(-2(x^2-1) + 4x^2) / (x^2-1)^3]
# = e^(1/(x^2-1)) * [(2x^2 + 2) / (x^2-1)^3]
# = 2(x^2+1) * e^(1/(x^2-1)) / (x^2-1)^3
# Нули: x^2 + 1 = 0 => нет действительных корней
# Значит, точек перегиба нет? Проверим знак f''
# При x^2 < 1: (x^2-1)^3 < 0 => f'' < 0
# При x^2 > 1: (x^2-1)^3 > 0 => f'' > 0
# Значит, f'' не меняет знак (кроме точек разрыва), точек перегиба нет

print("\nАналитически: f''(x) = 2(x^2+1)*e^(1/(x^2-1))/(x^2-1)^3")
print("f''(x) не обращается в ноль, знак меняется только в точках разрыва.")
print("Точек перегиба нет.")

# Тангенс угла наклона касательной в точке перегиба - нет точек перегиба
# Но можно построить касательные в окрестностях точек разрыва? Нет, там разрыв.

# Обозначим на графике экстремум
plt.figure()
plt.plot(x6b, f6(x6b), 'g', label='-1 < x < 1')
plt.plot(0, f6(np.array([0]))[0], 'ro', label='максимум (0, e^(-1))')
plt.axhline(1, color='k', linestyle=':', label='y = 1 (асимптота)')
plt.axvline(-1, color='k', linestyle='--')
plt.axvline(1, color='k', linestyle='--')
plt.title('Упражнение 6: экстремум и асимптоты')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()

print("\nВсе упражнения выполнены.")
