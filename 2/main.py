import math
import matplotlib.pyplot as plt
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

# Розрахунок наближеного розв'язку за Рунге-Кутти 2-го і 4-го розрядів
numerical_function_values_2_order = runge_kutta_2_order(differential_function, x_0, y_0, x_n, h)
numerical_function_values_4_order = runge_kutta_4_order(differential_function, x_0, y_0, x_n, h)

print(f"\nТаблиця для h={h}:")
print("| x | Аналітичний розв'язок | Наближений розв'язок Рунге-Кутти 2-го порядку | Наближений розв'язок Рунге-Кутти 4-го порядку |")
print("|---|-----------------------|-----------------------------------------------|-----------------------------------------------|")
for x, y_analytical, y_numerical_2_order, y_numerical_4_order in zip(x_values, analytical_solution_values, numerical_function_values_2_order, numerical_function_values_4_order):
    print(f"| {x} | {round(y_analytical, 8)} | {round(y_numerical_2_order, 8)} | {round(y_numerical_4_order, 8)} |")
print("")

# ============
#  Завдання 4
# ============

def theoretical_error_runge_kutta_2_order(h):
    return h ** 2
def theoretical_error_runge_kutta_4_order(h):
    return h ** 4

analytical_function_value_at_xn = analytical_function(x_n, C_value)
step_sizes = [0.1, 0.05, 0.025, 0.01]

runge_kutta_2_results = []
runge_kutta_2_actual_errors = []
runge_kutta_2_theoretical_errors = []

runge_kutta_4_results = []
runge_kutta_4_actual_errors = []
runge_kutta_4_theoretical_errors = []

for h in step_sizes:
    runge_kutta_2_numerical_function_values = runge_kutta_2_order(differential_function, x_0, y_0, x_n, h)
    numerical_function_value_at_xn = runge_kutta_2_numerical_function_values[-1]
    
    runge_kutta_2_actual_error = abs(analytical_function_value_at_xn - numerical_function_value_at_xn)
    runge_kutta_2_actual_errors.append(runge_kutta_2_actual_error)
    
    runge_kutta_2_theoretical_error = theoretical_error_runge_kutta_2_order(h)
    runge_kutta_2_theoretical_errors.append(runge_kutta_2_theoretical_error)
    
    runge_kutta_2_results.append((h, numerical_function_value_at_xn, runge_kutta_2_actual_error))
    
    
    runge_kutta_4_numerical_function_values = runge_kutta_4_order(differential_function, x_0, y_0, x_n, h)
    numerical_function_value_at_xn = runge_kutta_4_numerical_function_values[-1]
    
    runge_kutta_4_actual_error = abs(analytical_function_value_at_xn - numerical_function_value_at_xn)
    runge_kutta_4_actual_errors.append(runge_kutta_4_actual_error)
    
    runge_kutta_4_theoretical_error = theoretical_error_runge_kutta_4_order(h)
    runge_kutta_4_theoretical_errors.append(runge_kutta_4_theoretical_error)
    
    runge_kutta_4_results.append((h, numerical_function_value_at_xn, runge_kutta_4_actual_error))

print("| h | Наближений розв'язок у x_n для Рунге-Кутти 2-го порядку | Похибка |")
print("|---|---------------------------------------------------------|---------|")
for h, y_numerical, error in runge_kutta_2_results:
    print(f"| {h} | {round(y_numerical, 8)} | {round(error, 8)} |")

print("Висновок: при зменшенні кроку зменшується й похибка")
print("При h=0.01 похибка дуже мала\n")

print("| h | Наближений розв'язок у x_n для Рунге-Кутти 4-го порядку | Похибка |")
print("|---|---------------------------------------------------------|---------|")
for h, y_numerical, error in runge_kutta_4_results:
    print(f"| {h} | {round(y_numerical, 8)} | {round(error, 8)} |")
print("Висновок: Рунге-Кутти 4-го порядку має меншу похибку, ніж другого порядку")

# ============
#  Завдання 5
# ============

plt.figure(figsize=(12, 6))
plt.plot(step_sizes, runge_kutta_2_actual_errors, label="Фактична похибка", marker="o")
plt.plot(step_sizes, runge_kutta_2_theoretical_errors, label="Теоретична похибка", marker="o")
plt.title("Фактична і теоретична похибки Рунге-Кутти 2-го порядку")
plt.xlabel("Крок h")
plt.ylabel("Похибка")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(step_sizes, runge_kutta_4_actual_errors, label="Фактична похибка", marker="o")
plt.plot(step_sizes, runge_kutta_4_theoretical_errors, label="Теоретична похибка", marker="o")
plt.title("Фактична і теоретична похибки Рунге-Кутти 4-го порядку")
plt.xlabel("Крок h")
plt.ylabel("Похибка")
plt.legend()
plt.grid(True)
plt.show()
