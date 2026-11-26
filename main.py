import numpy as np
import matplotlib.pyplot as plt
import math
from sympy import *
from matplotlib import cm

print('Задание 1')
p1, p2 = Point(1,0,0), Point(5,3,2)
L1 = Line(p1, p2)
print('Общее уравнение прямой:', L1.equation())
print('Параметрические уравнения прямой:', Line(p1, p2).arbitrary_point())

l1 = Line(Point(2,-1,0), direction_ratio=[3,4,2])
l2 = Line(Point(7,1,3), direction_ratio=[3,4,2])
d = l1.distance(l2)
print('Расстояние между параллельными прямыми (distance):', d)

q = np.array([3,4,2])
a = np.array([2,-1,0])
b = np.array([7,1,3])
ab = b - a
d_vec = np.linalg.norm(np.cross(ab, q)) / np.linalg.norm(q)
print('Расстояние через векторное произведение:', d_vec)

print('Задание 2')
M = Point3D(9,8,7)
pl = Plane(Point3D(1,4,6), normal_vector=(2,4,6))
Lperp = pl.perpendicular_line(M)
print('Общее уравнение прямой:', Lperp.equation())
n1 = np.array([2,4,6])
n2 = np.array([2,4,6])
print('Векторное произведение нормалей:', np.cross(n1, n2))
print('Нормаль плоскости коллинеарна направляющему вектору прямой')

print('Задание 3')
a_pl = Plane(Point3D(0,0,-1.5), normal_vector=(4,-2,-2))
b_ln = Line(Point3D(3,6,-7), direction_ratio=np.array([1,1,-2]))
ang = a_pl.angle_between(b_ln)
print('Угол между прямой и плоскостью:', ang)
n = np.array([4,-2,-2])
q = np.array([1,1,-2])
sin_angle = np.dot(n, q) / np.linalg.norm(n) / np.linalg.norm(q)
alfa = np.arcsin(np.abs(sin_angle))
print('Угол между n и q в градусах:', math.degrees(alfa))

print('Задание 4')
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

P = Plane(M0, normal_vector=np.cross(q_dir, np.array([1,0,0])))
P2 = Plane(M0, normal_vector=q_dir)
print('Нормаль плоскости:', q_dir)
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
L1 = Line(Point3D(0,0,0), direction_ratio=np.cross(np.array([1,-1,2]), np.array([2,1,-1])))
L2 = Line(Point3D(0,0,0), direction_ratio=np.array([1,1,1]))
ang = L1.angle_between(L2)
print('Угол между прямыми (рад):', ang)
print('Угол между прямыми (град):', math.degrees(ang))

print('Упражнение 5')
def distance_lines(L1, L2):
    p1 = np.array(L1.p1, dtype=float)
    q1 = np.array(L1.direction, dtype=float)
    p2 = np.array(L2.p1, dtype=float)
    q2 = np.array(L2.direction, dtype=float)
    P = Plane(Point3D(*p1), normal_vector=tuple(q1))
    proj = []
    for pt in [L2.p1, L2.p2]:
        v = np.array(pt, dtype=float) - p1
        v_proj = v - np.dot(v, q1) / np.dot(q1,q1) * q1
        proj.append(p1 + v_proj)
    PL2 = Line(Point3D(*proj[0]), Point3D(*proj[1]))
    d = Point3D(*p1).distance(PL2)
    return d

l1 = Line(Point(2,-1,0), direction_ratio=[3,4,2])
l2 = Line(Point(7,1,3), direction_ratio=[3,4,2])
print('а) расстояние:', distance_lines(l1, l2))

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
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from sympy import *

print('Пример 1')
a, b = 3, 2
t = np.arange(0, 2*np.pi, 0.01)
x = a*np.cos(t); y = b*np.sin(t)
plt.plot(x, y, lw=2)
plt.ylabel('$y$'); plt.xlabel('$x$')
plt.grid(); plt.title('эллипс'); plt.show()

e1 = Ellipse(Point(0,0), 3, 2)
print('Каноническое уравнение:', e1.equation())
print('Эксцентриситет:', e1.eccentricity)
print('Площадь:', e1.area)

print('Упражнение 1')
e2 = Ellipse(Point(3,1), hradius=3, eccentricity=Rational(4,5))
print('Уравнение:', e2.equation())
print('Параметрическое:', e2.arbitrary_point())
print('Эксцентриситет:', e2.eccentricity)
print('Фокусы:', e2.foci)
print('Фокальное расстояние:', e2.focus_distance)
print('Директрисы:', e2.directrices)
print('Полуоси:', e2.hradius, e2.vradius)

t = np.arange(0, 2*np.pi, 0.01)
xx = 3 + 3*np.cos(t)
yy = 1 + e2.vradius*np.sin(t)
plt.plot(xx, yy, lw=2)
plt.plot(3, 1, 'ko')
for f in e2.foci:
    plt.plot(float(f.x), float(f.y), 'ro')
for d in e2.directrices:
    if d[0] == 1:
        plt.axvline(float(d[1]), color='g', ls='--')
    else:
        plt.axhline(float(d[1]), color='g', ls='--')
plt.grid(); plt.title('эллипс с параметрами')
plt.show()

print('Пример 2')
plt.subplot(2,1,1)
x = np.arange(0, 8, 0.01)
y1 = np.sqrt(2*x); y2 = -np.sqrt(2*x)
plt.plot(x, y1, lw=2, color='r')
plt.plot(x, y2, lw=2, color='r')
plt.grid(); plt.title('парабола'); plt.show()

print('Пример 4')
p1 = Parabola(Point(0,-1), Line(Point(4,-1), Point(4,1)))
p1 = p1.equation()
print('Уравнение параболы:', p1)
print('Раскрытое:', expand(p1))

print('Упражнение 5')
expr = 4*x**2 + 9*y**2 - 8*x - 36*y + 4
print('Тип кривой: эллипс')
print('Канонический вид:', (x-1)**2/9 + (y-2)**2/4 - 1)
print('Фокусы: (1±sqrt(5), 2)')
print('Эксцентриситет: sqrt(5)/3')
print('Директрисы: x = 1 ± 9/sqrt(5)')
e3 = Ellipse(Point(1,2), 3, 2)
print('Проверка equation:', e3.equation())
print('Проверка foci:', e3.foci)
print('Проверка eccentricity:', e3.eccentricity)

print('Упражнение 6')
def complete_square(A, B, D, E, F):
    x0 = -D/(2*A) if A != 0 else 0
    y0 = -E/(2*B) if B != 0 else 0
    K = F - A*x0**2 - B*y0**2
    return (x0, y0, K)

print('Пример 4:', complete_square(0, 1, 0, 2, -15))
print('Упражнение 5:', complete_square(4, 9, -8, -36, 4))

print('Дополнительное задание')
from math import sqrt
ar = 1.666082
e_ma = 0.09346
a_ma = ar/(1+e_ma)
b_ma = a_ma*sqrt(1-e_ma**2)
c_ma = a_ma*e_ma
print('a_ma=', a_ma)
print('b_ma=', b_ma)
print('c_ma=', c_ma)

a_me=0.387098; b_me=0.378824; c_me=0.079602
a_v=0.723329; b_v=0.723312; c_v=0.004918
a_e=1.000001; b_e=0.999861; c_e=0.016700
a_ma=1.523679; b_ma=1.517010; c_ma=0.142403

t = np.arange(0, 2*np.pi+0.01, 0.01)
x_me = -c_me + a_me*np.cos(t); y_me = b_me*np.sin(t)
x_v = -c_v + a_v*np.cos(t); y_v = b_v*np.sin(t)
x_e = -c_e + a_e*np.cos(t); y_e = b_e*np.sin(t)
x_ma = -c_ma + a_ma*np.cos(t); y_ma = b_ma*np.sin(t)

ax = plt.axes()
ax.plot(x_me, y_me, 'm')
ax.plot(x_v, y_v, 'g')
ax.plot(x_e, y_e, 'b')
ax.plot(x_ma, y_ma, 'r')
ax.set_xlim([-2,2]); ax.set_ylim([-2,2]); ax.set_aspect('equal')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.title('Орбиты планет')
plt.show()

def kepler2(t, T, e):
    M = 2*np.pi/T*t
    return M + e*np.sin(M) + e**2*np.sin(M)*np.cos(M) + e**3/2*np.sin(M)*(3*np.cos(M)**2 - 1)

day = 50
e_me = 0.2056; e_v = 0.0068; e_e = 0.0167; e_ma = 0.0934
t_me = kepler2(day, 88.0, e_me)
x_me_d = -c_me + a_me*np.cos(t_me); y_me_d = b_me*np.sin(t_me)
t_v = kepler2(day, 224.7, e_v)
x_v_d = -c_v + a_v*np.cos(t_v); y_v_d = b_v*np.sin(t_v)
t_e = kepler2(day, 365.2, e_e)
x_e_d = -c_e + a_e*np.cos(t_e); y_e_d = b_e*np.sin(t_e)
t_ma = kepler2(day, 687.0, e_ma)
x_ma_d = -c_ma + a_ma*np.cos(t_ma); y_ma_d = b_ma*np.sin(t_ma)

ax = plt.axes()
ax.plot(x_me, y_me, 'm')
ax.plot(x_v, y_v, 'g')
ax.plot(x_e, y_e, 'b')
ax.plot(x_ma, y_ma, 'r')
ax.plot(x_me_d, y_me_d, 'mo')
ax.plot(x_v_d, y_v_d, 'go')
ax.plot(x_e_d, y_e_d, 'bo')
ax.plot(x_ma_d, y_ma_d, 'ro')
ax.set_xlim([-2,2]); ax.set_ylim([-2,2]); ax.set_aspect('equal')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.title('Положение планет на 50-й день')
plt.show()



import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from sympy import *

print('Пример 1')
x = np.linspace(-1, 1, 200)
y = np.linspace(-1, 1, 200)
x, y = np.meshgrid(x, y)
z = lambda x, y: x**2 + 2*y**2
Z = z(x, y)
fig = plt.figure(figsize=(7, 7))
ax = plt.axes(projection='3d')
my_cmap = plt.get_cmap('magma')
ax.plot_surface(x, y, Z, alpha=0.8, cmap=my_cmap)
ax.contourf(x, y, Z, zdir='z', offset=np.min(Z), cmap=my_cmap)
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
