```python
# -*- coding: utf-8 -*-
# Лабораторная работа 10. Прямая на плоскости
# Решение упражнений 1–8

import numpy as np
import matplotlib.pyplot as plt
from sympy import *

# ============================================================
# Упражнение 1. Параметрические уравнения прямой из примера 3
# ============================================================
p1, p2 = Point(1, 0), Point(5, 3)
L = Line(p1, p2)
print("Упражнение 1")
print("Общее уравнение:", L.equation())
print("Параметрическое представление:", L.arbitrary_point())

# ============================================================
# Упражнение 2. Расстояние от точки (-1, 1) до прямой через (1,4) и (5,3)
# ============================================================
print("\nУпражнение 2")
L2 = Line(Point(1, 4), Point(5, 3))
d = L2.distance(Point(-1, 1))
print("Расстояние =", d)

# ============================================================
# Упражнение 3. Прямая L2 через (-2, 2), параллельная L1
# ============================================================
print("\nУпражнение 3")
L1 = Line(Point(0, 0), Point(2, 3))
L2 = L1.parallel_line(Point(-2, 2))
print("L1:", L1.equation())
print("L2:", L2.equation())

# Рисунок к упражнению 3
x = np.linspace(-5, 5, 100)
y1 = 1.5 * x
y2 = 1.5 * x + 5
plt.figure()
plt.plot(x, y1, label='L1: y = 1.5x')
plt.plot(x, y2, label='L2: y = 1.5x + 5')
plt.plot(0, 0, 'ko'); plt.plot(2, 3, 'ko')
plt.plot(-2, 2, 'ro')
plt.text(0.2, 0.2, 'A(0,0)')
plt.text(2.2, 3.2, 'B(2,3)')
plt.text(-2.2, 2.2, 'M(-2,2)')
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(True); plt.axis('equal')
plt.legend()
plt.title('Упражнение 3: параллельные прямые')
plt.show()

# ============================================================
# Упражнение 4. Прямая L3 через (-2, 2), перпендикулярная L1
# ============================================================
print("\nУпражнение 4")
L3 = L1.perpendicular_line(Point(-2, 2))
print("L3:", L3.equation())

x = np.linspace(-5, 5, 100)
y1 = 1.5 * x
y3 = -2/3 * x + 2/3
plt.figure()
plt.plot(x, y1, label='L1: y = 1.5x')
plt.plot(x, y3, label='L3: y = -2/3 x + 2/3')
plt.plot(-2, 2, 'ro')
plt.text(-1.8, 2.2, 'M(-2,2)')
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(True); plt.axis('equal')
plt.legend()
plt.title('Упражнение 4: перпендикулярные прямые')
plt.show()

# ============================================================
# Упражнение 5. Проекция точки (0.5, 0) на прямую x - y = 0
# ============================================================
print("\nУпражнение 5")
Lx = Line(Point(0, 0), Point(1, 1))  # x - y = 0
proj = Lx.projection(Point(0.5, 0))
print("Проекция:", proj)

# ============================================================
# Упражнение 6. Точка пересечения L1 и L3
# ============================================================
print("\nУпражнение 6")
inter = L1.intersection(L3)
print("Точка пересечения:", inter)

x = np.linspace(-5, 5, 100)
y1 = 1.5 * x
y3 = -2/3 * x + 2/3
plt.figure()
plt.plot(x, y1, label='L1')
plt.plot(x, y3, label='L3')
for p in inter:
    plt.plot(float(p.x), float(p.y), 'ro')
    plt.text(float(p.x)+0.2, float(p.y)+0.2, f'({float(p.x):.2f}, {float(p.y):.2f})')
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(True); plt.axis('equal')
plt.legend()
plt.title('Упражнение 6: пересечение L1 и L3')
plt.show()

# ============================================================
# Упражнение 7. Прямая через M0(0.6, -0.4) параллельно q(-3, 3)
# ============================================================
print("\nУпражнение 7")
M0 = Point(0.6, -0.4)
q = np.array([-3, 3])
# направляющий вектор q => нормаль n = (3, 3) (перпендикуляр)
# уравнение: 3(x-0.6) + 3(y+0.4) = 0 => 3x + 3y - 0.6 = 0 => x + y - 0.2 = 0
x = np.linspace(-5, 5, 100)
y = -x + 0.2
plt.figure()
plt.plot(x, y, label='Прямая: x + y - 0.2 = 0')
plt.plot(0.6, -0.4, 'ro')
plt.text(0.8, -0.2, 'M0(0.6, -0.4)')
plt.arrow(0, -2, q[0], q[1], width=0.08, color='green', length_includes_head=True)
plt.text(-2.5, -0.5, 'q(-3, 3)')
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(True); plt.axis('equal')
plt.legend()
plt.title('Упражнение 7')
plt.show()

# ============================================================
# Упражнение 8. Треугольник A(2,-2), B(3,5), C(6,1)
# ============================================================
print("\nУпражнение 8")
A = Point(2, -2)
B = Point(3, 5)
C = Point(6, 1)

# 1) Высота из B: прямая через B, перпендикулярная AC
AC = Line(A, C)
hB = AC.perpendicular_line(B)
print("1) Уравнение высоты из B:", hB.equation())

# 2) Длина высоты из B = расстояние от B до AC
hB_len = AC.distance(B)
print("2) Длина высоты из B:", hB_len)

# 3) Медиана из A: прямая через A и середину BC
Mbc = Point((B.x + C.x)/2, (B.y + C.y)/2)
medA = Line(A, Mbc)
print("3) Уравнение медианы из A:", medA.equation())

# 4) Длина медианы из A
medA_len = A.distance(Mbc)
print("4) Длина медианы из A:", medA_len)

# 5) Биссектриса угла C
# Направляющие векторы сторон CA и CB
vCA = np.array([float(A.x - C.x), float(A.y - C.y)])
vCB = np.array([float(B.x - C.x), float(B.y - C.y)])
uCA = vCA / np.linalg.norm(vCA)
uCB = vCB / np.linalg.norm(vCB)
bis_dir = uCA + uCB  # направление биссектрисы
# Прямая через C с направляющим bis_dir
# Нормаль: (-bis_dir[1], bis_dir[0])
n_bis = np.array([-bis_dir[1], bis_dir[0]])
# Уравнение: n_bis·(X - C) = 0
xx, yy = symbols('x y')
eq_bis = n_bis[0]*(xx - float(C.x)) + n_bis[1]*(yy - float(C.y))
eq_bis_simpl = simplify(eq_bis)
print("5) Уравнение биссектрисы угла C:", Eq(eq_bis_simpl, 0))

# Рисунок треугольника
plt.figure()
# Стороны
plt.plot([A.x, B.x, C.x, A.x], [A.y, B.y, C.y, A.y], 'k-', linewidth=1.5)
plt.plot(A.x, A.y, 'ko'); plt.text(float(A.x)+0.2, float(A.y)-0.5, 'A(2,-2)')
plt.plot(B.x, B.y, 'ko'); plt.text(float(B.x)+0.2, float(B.y)+0.2, 'B(3,5)')
plt.plot(C.x, C.y, 'ko'); plt.text(float(C.x)+0.2, float(C.y)+0.2, 'C(6,1)')

# Высота из B
x_h = np.linspace(-1, 8, 100)
# AC: через (2,-2) и (6,1): направление (4,3), нормаль (3,-4)
# 3(x-2) - 4(y+2) = 0 => 3x - 4y - 14 = 0 => y = (3x-14)/4
# высота из B: направление (4,3) => y - 5 = (3/4)(x - 3)
y_h = 5 + 0.75*(x_h - 3)
plt.plot(x_h, y_h, 'r--', label='Высота из B')

# Медиана из A
x_m = np.linspace(-1, 8, 100)
# Mbc = (4.5, 3), A=(2,-2): направление (2.5, 5) => y+2 = 2(x-2) => y = 2x - 6
y_m = 2*x_m - 6
plt.plot(x_m, y_m, 'g--', label='Медиана из A')

# Биссектриса из C
t = np.linspace(-2, 2, 100)
x_b = float(C.x) + bis_dir[0]*t
y_b = float(C.y) + bis_dir[1]*t
plt.plot(x_b, y_b, 'b--', label='Биссектриса из C')

plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(True); plt.axis('equal')
plt.legend()
plt.title('Упражнение 8: треугольник и его элементы')
plt.show()
```
