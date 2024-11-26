from arrange import arrange


def runge_kutta_2_order(f, x_0, y_0, x_n, h) -> tuple[list[int], list[int]]:
    x_values = arrange(x_0, x_n, h)
    y_values = [0] * len(x_values)
    y_values[0] = y_0

    for i in range(1, len(x_values)):
        x = x_values[i - 1]
        y = y_values[i - 1]

        k_1 = h * f(x, y)
        k_2 = h * f(x + h, y + k_1)

        y_values[i] = y + (k_1 + k_2) / 2

    return x_values, y_values
