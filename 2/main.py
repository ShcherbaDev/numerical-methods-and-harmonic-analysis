import math
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

# ============
#  Завдання 3
# ============

h = 0.1

def analytical_function(x, C):
    return C*math.exp(x**2) - x**2 - 1

def differential_function(x, y):
    return 2*x*y + 2*x**3

# Розрахунок аналітичного розв'язку
x_values = arrange(x_0, x_n, h)
analytical_solution_values = [analytical_function(x, C_value) for x in x_values]

# Розрахунок наближеного розв'язку за Рунге-Кутти 2-го розряду
_, numerical_function_values = runge_kutta_2_order(differential_function, x_0, y_0, x_n, h)

print(f"\nТаблиця для h={h}:")
print("| x | Аналітичний розв'язок | Наближений розв'язок |")
print("|---|-----------------------|----------------------|")
for x, y_analytical, y_numerical in zip(x_values, analytical_solution_values, numerical_function_values):
    print(f"| {x} | {round(y_analytical, 4)} | {round(y_numerical, 4)} |")
print("")

# ============
#  Завдання 4
# ============

analytical_function_value_at_xn = analytical_function(x_n, C_value)
step_sizes = [0.1, 0.05, 0.025, 0.01]
results = []

for h in step_sizes:
    _, numerical_function_values = runge_kutta_2_order(differential_function, x_0, y_0, x_n, h)
    numerical_function_value_at_xn = numerical_function_values[-1]
    error = abs(analytical_function_value_at_xn - numerical_function_value_at_xn)
    results.append((h, numerical_function_value_at_xn, error))

print("| h | Наближений розв'язок у x_n | Похибка |")
print("|---|----------------------------|---------|")
for h, y_numerical, error in results:
    print(f"| {h} | {round(y_numerical, 4)} | {round(error, 4)} |")
