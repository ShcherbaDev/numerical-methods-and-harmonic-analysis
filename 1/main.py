import matplotlib.pyplot as plt
from math import log, pow
from lagrange import get_lagrange

range_start = 1
range_end = 4

# Варіант 6: f(x) = ln(x^4 - 2x^2 + 3)
def f(x):
    return log(pow(x, 4) - 2 * pow(x, 2) + 3)

# Отримання n рівновіддалених вузлів на проміжку [a, b]
def get_interpolation_range(a, b, n):
    result = [a]
    step = (b - a) / n
    while result[-1] < b:
        result.append(result[-1] + step)
    return result

def get_nodes(a, b, n):
    x_values = get_interpolation_range(a, b, n)
    y_values = [f(x) for x in x_values]
    return list(zip(x_values, y_values))


# Генерація точок для графіків
nodes = get_nodes(range_start, range_end, 5)
x_values = get_interpolation_range(range_start, range_end, 100)
y_function_values = [f(x) for x in x_values]
y_poly = [get_lagrange(x, nodes) for x in x_values]

plt.plot(x_values, y_function_values, label="$f(x) = \ln{(x^4 - 2x^2 + 3)}$")
plt.plot(x_values, y_poly, label="Поліном Лагранжа")
plt.scatter(*zip(*nodes), color="red", label="Вузли інтерполяції")

plt.legend()
plt.show()
