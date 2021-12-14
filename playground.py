def add(*args):
    total_sum = 0
    for val in args:
        try:
            total_sum += val
        except TypeError:
            continue
    return total_sum

print(add(5,3,2,'wale',7,2))