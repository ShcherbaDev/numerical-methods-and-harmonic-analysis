from math import exp
from runge_kutta import *

# Вхідні дані згідно 6-го варіанту
x_0 = 0
y_0 = -0.8
x_n = 1


def differenciyne_rivnyannya(x, y):
    return 2 * x * y + 2 * x**3


def analitychniy_rozvyazok(x, constant):
    return constant * exp(x**2) - x**2 - 1


print(list(runge_kutta_2_order(differenciyne_rivnyannya, x_0, y_0, x_n, 0.1)))
