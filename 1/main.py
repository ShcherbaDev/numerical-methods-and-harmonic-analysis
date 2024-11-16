from math import log, pow
import matplotlib.pyplot as plt
from lagrange import get_lagrange
from piecewise import get_piecewise_linear_interpolation

# Варіант 6: f(x) = ln(x^4 - 2x^2 + 3)
def f(x: float) -> float:
    return log(pow(x, 4) - 2 * pow(x, 2) + 3)

# Отримання n рівновіддалених вузлів на проміжку [a, b]
def get_interpolation_range_nodes(
    range_start: int,
    range_end: int,
    number_of_nodes: int
) -> list[float]:
    step = (range_end - range_start) / (number_of_nodes - 1)
    return [range_start + i * step for i in range(number_of_nodes)]

# Вхідні дані
range_start = 1
range_end = 3
number_of_nodes = 4

# Вузли та значення функції у вузлах
nodes_x = get_interpolation_range_nodes(range_start, range_end, number_of_nodes)
nodes_y = [f(x) for x in nodes_x]
nodes = list(zip(nodes_x, nodes_y))

# Обрахунок точок щоб отримати гладкий та точний графік
x_values = get_interpolation_range_nodes(range_start, range_end, 100)
y_values = [f(x) for x in x_values]
lagrange_values = [get_lagrange(x, nodes) for x in x_values]

# ============
#  Завдання 4
# ============

# Графік функції f(x) та поліному L(x)
plt.figure(figsize=(12, 6))
plt.plot(x_values, y_values, label="$f(x)$")
plt.plot(x_values, lagrange_values, label="$L(x)$", linestyle="--")
plt.scatter(nodes_x, nodes_y, label="Вузли інтерполяції", color="red", zorder=999)
plt.title("Інтерполяція поліномом Лагранжа функції $f(x) = \ln{(x^4 - 2x^2 + 3)}$")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

# Графік похибки інтерполяції f(x) - L(x)
# та отримання найбільшого відхилення
errors = [f_x - l_x for f_x, l_x in zip(y_values, lagrange_values)]
delta_n = max(abs(err) for err in errors)

plt.figure(figsize=(12, 6))
plt.plot(x_values, errors, label="Похибка $f(x) - L(x)$", color="green")
plt.axhline(0, color="black", linestyle=":", linewidth=3)
plt.title(f"Графік похибки інтерполяції $f(x) - L(x)$\nДефект наближення: {delta_n}")
plt.xlabel("x")
plt.ylabel("Похибка")
plt.legend()
plt.grid(True)
plt.show()

# ============
#  Завдання 5
# ============

# Значення кусково-лінійної інтерполяції
g_values = [get_piecewise_linear_interpolation(x, nodes) for x in x_values]

# Графік f(x) та кусково-лінійної інтерполяції g(x)
plt.figure(figsize=(12, 6))
plt.plot(x_values, y_values, label="$f(x)$")
plt.plot(x_values, g_values, label="$g(x)$", linestyle="--")
plt.scatter(nodes_x, nodes_y, label="Вузли інтерполяції", color="red", zorder=999)
plt.title("Кусково-лінійна інтерполяція $f(x)$")
plt.xlabel("x")
plt.xlabel("y")
plt.legend()
plt.grid(True)
plt.show()

# Графік похибки інтерполяції f(x) - g(x) 
# та отримання найбільшого відхилення
errors_g = [f(x) - g for x, g in zip(x_values, g_values)]
delta_g = max(abs(err) for err in errors_g)

plt.figure(figsize=(12, 6))
plt.plot(x_values, errors_g, label="Похибка $f(x) - g(x)$", color="green")
plt.axhline(0, color="black", linestyle=":", linewidth=3)
plt.title(f"Графік похибки інтерполяції $f(x) - g(x)$\nДефект наближення: {delta_g}")
plt.xlabel("x")
plt.ylabel("Похибка")
plt.legend()
plt.grid(True)
plt.show()
