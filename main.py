import matplotlib.pyplot as plt
import numpy as np


x_parabola = np.linspace(-5, 5, 100)
y_parabola = x_parabola**2


x_hyperbola = np.linspace(0.1, 5, 100)
y_hyperbola = 1 / x_hyperbola


plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(x_parabola, y_parabola, 'b-', marker='o', markevery=10, label='y = x^2')
plt.title('Парабола')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()


plt.subplot(1, 2, 2)
plt.plot(x_hyperbola, y_hyperbola, 'r--', marker='s', markevery=10, label='y = 1/x')
plt.title('Гипербола')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
