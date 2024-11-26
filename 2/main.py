import sympy as sp
from runge_kutta import *

# Вхідні дані для 6-го варіанту
x_0 = 0
y_0 = -0.8
x_n = 1

# ============
#  Завдання 2
# ============

x, C = sp.symbols("x C")
y = sp.Function("y")

# Загальний розв'язок
general_solution = C * sp.exp(x**2) - x**2 - 1

differential_expression_left = sp.diff(general_solution, x)
differential_expression_right = 2*x*general_solution + 2*x**3

C_value = sp.solve(general_solution.subs(x, x_0) - y_0, C)[0]

partial_solution = general_solution.subs(C, C_value)
print(f"Частинний аналітичний розв'язок: y = {partial_solution}")

is_solution = sp.simplify(differential_expression_left - differential_expression_right) == 0
print(f"Загальний розв'язок задовільняє диференціальне рівняння: {'Так' if is_solution else 'Ні'}")
