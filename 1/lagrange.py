def get_lagrange(x: float, x_y: list[tuple[int, int]]) -> float:
    n = len(x_y)
    result = 0

    for i in range(n):
        x_i, y_i = x_y[i]
        numerator = 1
        denominator = 1
        
        for j in range(n):
            x_j = x_y[j][0]
            if i != j:
                numerator *= x - x_j
                denominator *= x_i - x_j
        
        result += y_i * (numerator / denominator)

    return result
