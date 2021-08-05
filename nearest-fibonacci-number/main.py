def nearest_fibonacci(number: int):
    """Finds the nearest Fibonacci number to a given positive integer(number).
    If there are more than one Fibonacci numbers with equal distance to the given number, return the smallest one."""
    fib_numbers = [0, 1]
    num_1, num_2 = 0, 1
    min_diff = number
    nearest_fib_number: int
    min_diff_dct = {}

    while num_2 < number:
        next_num = num_1 + num_2
        fib_numbers.append(next_num)
        num_1 = num_2
        num_2 = next_num

    if number in fib_numbers:
        nearest_fib_number = number
    else:
        for numb in fib_numbers:
            num_diff = abs(numb - number)
            if num_diff <= min_diff:
                min_diff = num_diff
                min_diff_dct[numb] = min_diff
        nearest_fib_number = min(min_diff_dct, key=min_diff_dct.get)
    return nearest_fib_number
