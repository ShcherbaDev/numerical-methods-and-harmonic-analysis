def arrange(start, end, step):
    result = [start]

    while round(result[-1] + step, 10) <= end:
        result.append(round(result[-1] + step, 10))

    return result
