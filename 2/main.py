from math import e
from sympy import *

# Вхідні дані згідно 6-го варіанту
x_0 = 0
y_0 = -0.8
x_n = 1

def differenciyne_rivnyannya(x, y):
    return 2*x*y + 2*x**3

def analitychniy_rozvyazok(x, constant):
    return constant * e ** (x ** 2) - (x ** 2) - 1
