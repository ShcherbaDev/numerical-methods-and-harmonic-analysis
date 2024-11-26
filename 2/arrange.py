def arrange(start, end, step):
    result = [start]

    while result[-1] + step <= end:
        result.append(round(result[-1] + step, 1))

    return result
