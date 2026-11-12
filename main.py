import numpy as np
import matplotlib.pyplot as plt
import math
from sympy import *
from matplotlib import cm
%matplotlib widget

print("=" * 60)
print("Упражнение 1")
print("=" * 60)

p1 = Point3D(1, 1, 2)
p2 = Point3D(2, 4, 7)
p3 = Point3D(3, 5, 1)

plane1 = Plane(p1, p2, p3)
print("Уравнение плоскости через три точки:")
print(plane1.equation())

v1 = p2 - p1
v2 = p3 - p1
n = v1.cross(v2)
print("\nНормальный вектор (из векторного произведения):", n)

plane1_check = Plane(p1, normal_vector=n)
print("Проверка через точку и нормальный вектор:")
print(plane1_check.equation())

print("\n" + "=" * 60)
print("Упражнение 2")
print("=" * 60)

plane_base = Plane(Point3D(0, 0, 0), normal_vector=(1, 2, 3))
print("Исходная плоскость:")
print(plane_base.equation())

A = Point3D(4, 2, 3)
B = Point3D(2, 0, 1)

AB = B - A
print("Вектор AB:", AB)

n_base = Point3D(1, 2, 3)
n_new = AB.cross(n_base)
print("Нормальный вектор искомой плоскости:", n_new)

plane2 = Plane(A, normal_vector=n_new)
print("Уравнение искомой плоскости:")
print(plane2.equation())

dot_product = n_base.dot(n_new)
print("Скалярное произведение нормальных векторов:", dot_product)
print("Плоскости перпендикулярны, если скалярное произведение = 0")

print("\n" + "=" * 60)
print("Упражнение 3")
print("=" * 60)

plane3 = Plane(Point3D(3, 0, 0), normal_vector=(1, 1, 1))
print("Уравнение плоскости:")
print(plane3.equation())

M = Point3D(1, 2, 3)
print("Точка M:", M)

dist = plane3.distance(M)
print("Расстояние от точки до плоскости:", dist)

print("Проверка по формуле:", abs(1 + 2 + 3 - 3) / math.sqrt(3))

print("\n" + "=" * 60)
print("Упражнение 4")
print("=" * 60)

M4 = Point3D(1, -1, -3)
n4 = Point3D(2, -3, 5)

plane4 = Plane(M4, normal_vector=n4)
print("Уравнение плоскости:")
eq4 = plane4.equation()
print(eq4)

O = Point3D(0, 0, 0)
dist4 = plane4.distance(O)
print("Расстояние от начала координат до плоскости:", dist4)

A4, B4, C4, D4 = 2, -3, 5, 10
f4 = lambda x, y: (-A4*x - B4*y - D4) / C4

fig4 = plt.figure(figsize=(8, 8))
ax4 = fig4.add_subplot(1, 1, 1, projection='3d')
xval4 = np.linspace(-5, 5, 50)
yval4 = np.linspace(-5, 5, 50)
x4, y4 = np.meshgrid(xval4, yval4)
z4 = f4(x4, y4)

ax4.plot([M4.x], [M4.y], [M4.z], 'ro', label='M(1,-1,-3)')
ax4.quiver(M4.x, M4.y, M4.z, n4.x, n4.y, n4.z, color='blue', label='n(2,-3,5)')
ax4.text(M4.x + 0.5, M4.y + 0.5, M4.z - 0.5, 'M')

surf4 = ax4.plot_surface(x4, y4, z4, rstride=5, cstride=5, cmap=cm.plasma, alpha=0.6)
ax4.set_xlabel('X')
ax4.set_ylabel('Y')
ax4.set_zlabel('Z')
ax4.set_title('Плоскость 2x - 3y + 5z + 10 = 0')
ax4.view_init(20, -60)
plt.show()

print("\n" + "=" * 60)
print("Упражнение 5")
print("=" * 60)

M5 = Point3D(2, -3, -6)
a5 = Point3D(-3, 2, -1)
b5 = Point3D(0, 3, 1)
N5 = Point3D(-3, 1, 3)

n5 = a5.cross(b5)
print("Нормальный вектор (a x b):", n5)

plane5 = Plane(M5, normal_vector=n5)
print("Уравнение плоскости:")
eq5 = plane5.equation()
print(eq5)

dist5 = plane5.distance(N5)
print("Расстояние от N(-3,1,3) до плоскости:", dist5)

A5, B5, C5, D5 = 5, 3, -9, -55
f5 = lambda x, y: (-A5*x - B5*y - D5) / C5

fig5 = plt.figure(figsize=(8, 8))
ax5 = fig5.add_subplot(1, 1, 1, projection='3d')
xval5 = np.linspace(-10, 10, 50)
yval5 = np.linspace(-10, 10, 50)
x5, y5 = np.meshgrid(xval5, yval5)
z5 = f5(x5, y5)

ax5.plot([M5.x], [M5.y], [M5.z], 'ro', label='M(2,-3,-6)')
ax5.plot([N5.x], [N5.y], [N5.z], 'go', label='N(-3,1,3)')
ax5.quiver(M5.x, M5.y, M5.z, a5.x, a5.y, a5.z, color='blue', label='a(-3,2,-1)')
ax5.quiver(M5.x, M5.y, M5.z, b5.x, b5.y, b5.z, color='green', label='b(0,3,1)')
ax5.quiver(M5.x, M5.y, M5.z, n5.x, n5.y, n5.z, color='red', label='n(5,3,-9)')

ax5.text(M5.x + 0.5, M5.y + 0.5, M5.z - 0.5, 'M')
ax5.text(N5.x + 0.5, N5.y + 0.5, N5.z - 0.5, 'N')

surf5 = ax5.plot_surface(x5, y5, z5, rstride=5, cstride=5, cmap=cm.viridis, alpha=0.6)
ax5.set_xlabel('X')
ax5.set_ylabel('Y')
ax5.set_zlabel('Z')
ax5.set_title('Плоскость 5x + 3y - 9z - 55 = 0')
ax5.view_init(20, -60)
plt.show()

print("\n" + "=" * 60)
print("Упражнение 6")
print("=" * 60)

M6 = Point3D(-1, 3, 0)
N6 = Point3D(2, 4, -1)

n_base6 = Point3D(1, -2, 3)

MN = N6 - M6
print("Вектор MN:", MN)

n6 = MN.cross(n_base6)
print("Нормальный вектор искомой плоскости:", n6)

plane6 = Plane(M6, normal_vector=n6)
print("Уравнение искомой плоскости:")
eq6 = plane6.equation()
print(eq6)

dot6 = n_base6.dot(n6)
print("Скалярное произведение нормальных векторов:", dot6)

A6, B6, C6, D6 = 1, -4, -3, 13
f6 = lambda x, y: (-A6*x - B6*y - D6) / C6

A6b, B6b, C6b, D6b = 1, -2, 3, -10
f6b = lambda x, y: (-A6b*x - B6b*y - D6b) / C6b

fig6 = plt.figure(figsize=(10, 8))
ax6 = fig6.add_subplot(1, 1, 1, projection='3d')
xval6 = np.linspace(-10, 10, 50)
yval6 = np.linspace(-10, 10, 50)
x6, y6 = np.meshgrid(xval6, yval6)

z6 = f6(x6, y6)
z6b = f6b(x6, y6)

ax6.plot([M6.x], [M6.y], [M6.z], 'ro', label='M(-1,3,0)')
ax6.plot([N6.x], [N6.y], [N6.z], 'go', label='N(2,4,-1)')

surf6 = ax6.plot_surface(x6, y6, z6, rstride=5, cstride=5, cmap=cm.plasma, alpha=0.5)
surf6b = ax6.plot_surface(x6, y6, z6b, rstride=5, cstride=5, cmap=cm.viridis, alpha=0.5)

ax6.set_xlabel('X')
ax6.set_ylabel('Y')
ax6.set_zlabel('Z')
ax6.set_title('Искомая: x - 4y - 3z + 13 = 0\nИсходная: x - 2y + 3z - 10 = 0')
ax6.view_init(20, -60)
plt.show()

print("Условие перпендикулярности: скалярное произведение нормальных векторов = 0")
print("n1 = (1,-2,3), n2 = (1,-4,-3)")
print("n1 * n2 = 1*1 + (-2)*(-4) + 3*(-3) = 1 + 8 - 9 = 0 — верно")

print("\n" + "=" * 60)
print("Дополнительное задание")
print("=" * 60)

n1 = Point3D(2, -1, -12)
n2 = Point3D(3, 1, -7)
n3 = Point3D(4, -2, 0)

line_dir = n1.cross(n2)
print("Направляющий вектор линии пересечения:", line_dir)

n_new = line_dir.cross(n3)
print("Нормальный вектор искомой плоскости:", n_new)

point_on_line = Point3D(1, -1, 0)

plane_extra = Plane(point_on_line, normal_vector=n_new)
print("Уравнение искомой плоскости:")
print(plane_extra.equation())

Ae, Be, Ce, De = 1, 2, 5, 1
fe = lambda x, y: (-Ae*x - Be*y - De) / Ce

fig_extra = plt.figure(figsize=(10, 8))
ax_extra = fig_extra.add_subplot(1, 1, 1, projection='3d')
xval_e = np.linspace(-10, 10, 50)
yval_e = np.linspace(-10, 10, 50)
xe, ye = np.meshgrid(xval_e, yval_e)
ze = fe(xe, ye)

ax_extra.plot([1], [-1], [0], 'ro', label='Точка на линии (1,-1,0)')

surf_e = ax_extra.plot_surface(xe, ye, ze, rstride=5, cstride=5, cmap=cm.plasma, alpha=0.6)
ax_extra.set_xlabel('X')
ax_extra.set_ylabel('Y')
ax_extra.set_zlabel('Z')
ax_extra.set_title('Искомая плоскость: x + 2y + 5z + 1 = 0')
ax_extra.view_init(20, -60)
plt.show()

print("\nВсе задания выполнены.")ел слева при x->-1-:", f6(np.array([-1 - eps]))[0])
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
