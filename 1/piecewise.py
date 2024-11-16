def get_piecewise_linear_interpolation(x: float, x_y_ranges: list[tuple[int, int]]) -> float:
    for i in range(len(x_y_ranges) - 1):
        x_i, y_i = x_y_ranges[i]
        x_i_next, y_i_next = x_y_ranges[i + 1]
        
        # Перевірка на те, чи x є в межах поточного інтервалу.
        # Це робить функцію кусковою
        is_x_inside_the_range = x >= x_i and x <= x_i_next
        if not is_x_inside_the_range:
            continue
        
        # Лінійна інтерполяція між двома точками
        slope = (y_i_next - y_i) / (x_i_next - x_i)
        return y_i + slope * (x - x_i)
    
    return None # Якщо x не знаходиться в жодному з наданих інтервалів
