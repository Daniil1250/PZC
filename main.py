import numpy as np
import matplotlib.pyplot as plt
import math
from sympy import *
from matplotlib import cm

print('Упражнение 1')
L1 = Line(Point3D(2,-1,0), direction_ratio=[3,4,2])
L2 = Line(Point3D(7,1,3), direction_ratio=[3,4,2])
d = L1.distance(L2)
print('Расстояние между параллельными прямыми (distance):', d)

q = np.array([3,4,2])
a = np.array([2,-1,0])
b = np.array([7,1,3])
ab = b - a
d_vec = np.linalg.norm(np.cross(ab, q)) / np.linalg.norm(q)
print('Расстояние через векторное произведение:', d_vec)

print('Упражнение 2')
M = Point3D(9,8,7)
pl = Plane(Point3D(1,4,6), normal_vector=(2,4,6))
Lperp = pl.perpendicular_line(M)
print('Общее уравнение прямой:', Lperp.equation())
n1 = np.array([2,4,6])
n2 = np.array([2,4,6])
cross_n = np.cross(n1, n2)
print('Векторное произведение нормалей:', cross_n)
print('Векторное произведение нормалей равно нулю, так как нормали коллинеарны;')
print('это означает, что прямая перпендикулярна плоскости и её направляющий вектор')
print('совпадает с нормалью плоскости (2,4,6).')

print('Пример 2')
a_pl = Plane(Point3D(0,0,-1.5), normal_vector=(4,-2,-2))
b_ln = Line(Point3D(3,6,-7), direction_ratio=np.array([1,1,-2]))
ang = a_pl.angle_between(b_ln)
print('Угол между прямой и плоскостью:', ang)
n = np.array([4,-2,-2])
q = np.array([1,1,-2])
sin_angle = np.dot(n, q) / np.linalg.norm(n) / np.linalg.norm(q)
alfa = np.arcsin(np.abs(sin_angle))
print('Угол между n и q в градусах:', math.degrees(alfa))

print('Пример 3')
a = np.array([[1,2],[2,-2]])
b = np.array([-2,5])
x = np.linalg.inv(a).dot(b)
x0, y0, z0 = x[0], x[1], 0
print('Точка на прямой имеет координаты:', x0, y0, z0)

d1 = Plane(Point3D(0,-1,0), normal_vector=(1,2,-3))
d2 = Plane(Point3D(0,0,5), normal_vector=(2,-2,1))
L = d1.intersection(d2)
print('L=', L)

n1 = np.array([1,2,-3])
n2 = np.array([2,-2,1])
q = np.cross(n1, n2)
print('Направляющий вектор q:', q)

A = Point3D(1,-S(3)/2,0)
B = Point3D(-3,-S(17)/2,-6)
qAB = B - A
print('Направляющий вектор q (AB):', qAB)

M1 = Point(1,-1.5,0)
M2 = Point(-3,-8.5,-6)
lp3 = Line(M1, M2)
print('Параметрические уравнения:', lp3.arbitrary_point())

qq = np.linalg.norm(q)
ca, cb, cc = q[0]/qq, q[1]/qq, q[2]/qq
print('Косинусы углов с осями:', ca, cb, cc)
print('Проверка cos^2+cos^2+cos^2:', ca**2 + cb**2 + cc**2)

A1, B1, C1, D1 = 1, 2, -3, 2
A2, B2, C2, D2 = 2, -2, 1, -5
f1 = lambda x, y: (-A1*x - B1*y - D1) / C1
f2 = lambda x, y: (-A2*x - B2*y - D2) / C2

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1,1,1, projection='3d')
xval = np.linspace(-4,4,100)
yval = np.linspace(-4,4,100)
x, y = np.meshgrid(xval, yval)
z1 = f1(x, y)
ax.plot_surface(x, y, z1, cmap=cm.spring, alpha=0.3)
z2 = f2(x, y)
ax.plot_surface(x, y, z2, cmap=cm.spring, alpha=0.3)
p = np.array([1,-1.5,0])
v = np.array([4,7,6])
ax.quiver(*p, *v/2, color='Red')
ax.plot([1,5],[-1.5,5.5],[0,6],'--',color='Blue')
ax.plot([1,-3],[-1.5,-8.5],[0,-6],'--',color='Blue')
plt.xlabel('x'); plt.ylabel('y')
plt.title(r'$\frac{x-1}{-4}=\frac{y+1.5}{-7}=\frac{z}{-6}$')
plt.plot(1,-1.5,0,'ok')
eps=0.5
ax.text(1+eps,-1.5+eps,0-eps,'$M(1,-1.5,0)$')
plt.show()

print('Упражнение 3')
M0 = Point3D(2,-1,-3)
q_dir = np.array([2,-4,1])
Lpar = Line(M0, direction_ratio=q_dir)
print('Параметрические уравнения:', Lpar.arbitrary_point())

P = Plane(M0, normal_vector=q_dir)
print('Уравнение плоскости:', P.equation())
print('Нормаль плоскости:', q_dir)
print('Направляющий вектор прямой:', q_dir)
print('Скалярное произведение нормали и направляющего вектора:', np.dot(q_dir, q_dir))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
t = np.linspace(-3,3,50)
xs = 2 + 2*t
ys = -1 - 4*t
zs = -3 + t
ax.plot(xs, ys, zs, color='b')
ax.quiver(2,-1,-3, 2,-4,1, color='r')
plt.title('Прямая через M(2,-1,-3)')
plt.show()

print('Упражнение 4')
n1 = np.array([1,-1,2])
n2 = np.array([2,1,-1])
q1 = np.cross(n1, n2)
L1 = Line(Point3D(0,0,0), direction_ratio=q1)
q2 = np.array([1,1,1])
L2 = Line(Point3D(0,0,0), direction_ratio=q2)
ang = L1.angle_between(L2)
print('Направляющий вектор первой прямой:', q1)
print('Угол между прямыми (рад):', ang)
print('Угол между прямыми (град):', math.degrees(ang))

print('Упражнение 5')
def distance_lines(L1, L2):
    pA = np.array(L1.p1, dtype=float)
    q1 = np.array(L1.direction, dtype=float)
    P = Plane(Point3D(*pA), normal_vector=tuple(q1))
    pts = [L2.p1, L2.p2]
    proj = []
    for pt in pts:
        v = np.array(pt, dtype=float) - pA
        v_proj = v - np.dot(v, q1) / np.dot(q1, q1) * q1
        proj.append(pA + v_proj)
    PL2 = Line(Point3D(*proj[0]), Point3D(*proj[1]))
    d = Point3D(*pA).distance(PL2)
    return d

l1 = Line(Point(2,-1,0), direction_ratio=[3,4,2])
l2 = Line(Point(7,1,3), direction_ratio=[3,4,2])
print('а) расстояние (упражнение 1):', distance_lines(l1, l2))

l3 = Line(Point(9,0,2), direction_ratio=[-6,2,1])
l4 = Line(Point(-5,-5,1), direction_ratio=[3,2,-2])
print('б) расстояние:', distance_lines(l3, l4))

print('Дополнительное задание')
R = 5
C = 10
N = 24
phi = np.linspace(0, 2*np.pi, N, endpoint=False)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(N):
    x1, y1 = R*np.cos(phi[i]), R*np.sin(phi[i])
    j = (i + N//3) % N
    x2, y2 = R*np.cos(phi[j]), R*np.sin(phi[j])
    ax.plot([x1,x2],[y1,y2],[0,C], color='b')
ax.set_title('Башня Шухова')
plt.show()tourf(x, y, Z, zdir='z', offset=np.min(Z), cmap=my_cmap)
ax.contourf(x, y, Z, zdir='x', offset=-2, cmap=my_cmap)
ax.contourf(x, y, Z, zdir='y', offset=2, cmap=my_cmap)
plt.title('Эллиптический параболоид x^2 + 2y^2 = z')
plt.show()

print('Задание: эллипсоид')
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
x, y = np.meshgrid(x, y)
z = lambda x, y: np.sqrt(np.maximum(0, 1 - x**2/4 - y**2/1))
Z = z(x, y)
fig = plt.figure(figsize=(7, 7))
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, Z, alpha=0.8, cmap='viridis')
ax.plot_surface(x, y, -Z, alpha=0.8, cmap='viridis')
plt.title('Эллипсоид x^2/4 + y^2 + z^2 = 1')
plt.show()

print('Задание: гиперболоид')
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
x, y = np.meshgrid(x, y)
z = lambda x, y: x**2 - y**2
Z = z(x, y)
fig = plt.figure(figsize=(7, 7))
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, Z, alpha=0.8, cmap='plasma')
ax.contourf(x, y, Z, zdir='z', offset=np.min(Z), cmap='plasma')
plt.title('Гиперболический параболоид z = x^2 - y^2')
plt.show()

print('Задание: конус')
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
x, y = np.meshgrid(x, y)
z = lambda x, y: np.sqrt(x**2 + y**2)
Z = z(x, y)
fig = plt.figure(figsize=(7, 7))
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, Z, alpha=0.8, cmap='cividis')
ax.plot_surface(x, y, -Z, alpha=0.8, cmap='cividis')
plt.title('Конус z^2 = x^2 + y^2')
plt.show()

print('Задание: цилиндр')
theta = np.linspace(0, 2*np.pi, 100)
zz = np.linspace(-2, 2, 100)
theta, zz = np.meshgrid(theta, zz)
X = 2*np.cos(theta)
Y = 2*np.sin(theta)
fig = plt.figure(figsize=(7, 7))
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, zz, alpha=0.8, cmap='spring')
plt.title('Цилиндр x^2 + y^2 = 4')
plt.show()

print('Задание: однополостный гиперболоид')
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
x, y = np.meshgrid(x, y)
z = lambda x, y: np.sqrt(np.maximum(0, 1 + x**2 + y**2))
Z = z(x, y)
fig = plt.figure(figsize=(7, 7))
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, Z, alpha=0.8, cmap='coolwarm')
ax.plot_surface(x, y, -Z, alpha=0.8, cmap='coolwarm')
plt.title('Однополостный гиперболоид -x^2 - y^2 + z^2 = 1')
plt.show()
