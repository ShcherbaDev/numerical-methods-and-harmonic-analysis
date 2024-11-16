def get_lagrange(x: float, x_y: list[tuple[int, int]]) -> float:
    result = 0

    for i in range(len(x_y)):
        x_i, y_i = x_y[i]
        numerator = 1
        denominator = 1
        
        for j in range(len(x_y)):
            x_j = x_y[j][0]
            if i != j:
                numerator *= x - x_j
                denominator *= x_i - x_j
        
        result += y_i * (numerator / denominator)
    
    return result
