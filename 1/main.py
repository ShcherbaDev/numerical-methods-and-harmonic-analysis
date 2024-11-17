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
range_end = 30
min_number_of_nodes = 4
max_number_of_nodes = 20
number_of_nodes_step = 4

deltas: list[dict[int, float, float]] = []

for number_of_nodes in range(min_number_of_nodes, max_number_of_nodes + 1, number_of_nodes_step):
    # Відображати графіки тільки на першій ітерації циклу
    is_first_iteration = number_of_nodes == min_number_of_nodes

    # Вузли та значення функції у вузлах
    nodes_x = get_interpolation_range_nodes(range_start, range_end, number_of_nodes)
    nodes_y = [f(x) for x in nodes_x]
    nodes = list(zip(nodes_x, nodes_y))

    # Обрахунок точок щоб отримати гладкий та точний графік
    x_values = get_interpolation_range_nodes(range_start, range_end, 1000)
    y_values = [f(x) for x in x_values]
    lagrange_values = [get_lagrange(x, nodes) for x in x_values]

    # ============
    #  Завдання 4
    # ============

    # Графік функції f(x) та поліному L(x)
    if is_first_iteration:
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

    if is_first_iteration:
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
    if is_first_iteration:
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

    if is_first_iteration:
        plt.figure(figsize=(12, 6))
        plt.plot(x_values, errors_g, label="Похибка $f(x) - g(x)$", color="green")
        plt.axhline(0, color="black", linestyle=":", linewidth=3)
        plt.title(f"Графік похибки інтерполяції $f(x) - g(x)$\nДефект наближення: {delta_g}")
        plt.xlabel("x")
        plt.ylabel("Похибка")
        plt.legend()
        plt.grid(True)
        plt.show()

    deltas.append({
        "nodes": number_of_nodes,
        "delta_n": delta_n,
        "delta_g": delta_g
    })
    
    # ============
    #  Завдання 7
    # ============

    extrapolation_left_x = get_interpolation_range_nodes(2 * range_start - range_end, range_start, 1000)
    extrapolation_right_x = get_interpolation_range_nodes(range_end, 2 * range_end - range_start, 1000)

    extrapolation_left_y = [f(x) for x in extrapolation_left_x]
    extrapolation_right_y = [f(x) for x in extrapolation_right_x]

    extrapolation_left_lagrange = [get_lagrange(x, nodes) for x in extrapolation_left_x]
    extrapolation_right_lagrange = [get_lagrange(x, nodes) for x in extrapolation_right_x]

    # Графік функції f(x) та поліному L(x) на [2a-b, 2b-a]
    extrapolation_x = extrapolation_left_x + extrapolation_right_x
    extrapolation_y = extrapolation_left_y + extrapolation_right_y
    extrapolation_lagrange = extrapolation_left_lagrange + extrapolation_right_lagrange
    
    if is_first_iteration:
        plt.figure(figsize=(12, 6))
        plt.plot(extrapolation_x, extrapolation_y, label="$f(x)$")
        plt.plot(extrapolation_x, extrapolation_lagrange, label="$L(x)$", linestyle="--")
        plt.title(f"Екстраполяція $f(x)$ та $L(x)$ на відрізку $[2a-b, 2b-a]$")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.grid(True)
        plt.show()

    # Графік похибок екстраполяції
    extrapolation_errors = [f_x - l_x for f_x, l_x in zip(extrapolation_y, extrapolation_lagrange)]
    extrapolation_delta = max(abs(err) for err in extrapolation_errors)

    if is_first_iteration:
        plt.figure(figsize=(12, 6))
        plt.plot(extrapolation_x, extrapolation_errors, label=f"Похибка $f(x) - L(x)$\n$\Delta = {extrapolation_delta}$")
        plt.axhline(0, color="black", linestyle=":", linewidth=3)
        plt.title(f"Похибки екстраполяції $f(x) - L(x)$ на $[2a-b, 2b-a]$")
        plt.xlabel("x")
        plt.ylabel("Похибка")
        plt.legend()
        plt.grid(True)
        plt.show()

# ============
#  Завдання 6
# ============

# Вивід таблиці дефектів наближення при різній кількості вузлів
# у markdown форматі
print("| $n$ | $\Delta_n$ | $\Delta_1$ |")
print("| --- | --- | --- |")
for row in deltas:
    number_of_nodes, delta_n, delta_g = row.values()
    print(f"| {number_of_nodes} | {delta_n} | {delta_g} |")

# Побудова графіку залежності \Delta_n і \Delta_1 від n
plt.figure(figsize=(10, 7))
plt.plot([row["nodes"] for row in deltas], [row["delta_n"] for row in deltas], label="$\Delta_n$", marker="o")
plt.plot([row["nodes"] for row in deltas], [row["delta_g"] for row in deltas], label="$\Delta_1$", marker="o")
plt.title("Залежність дефекту наближення від кількості вузлів")
plt.xlabel("Кількість вузлів $n$")
plt.ylabel("Дефект наближення")
plt.legend()
plt.grid(True)
plt.show()
