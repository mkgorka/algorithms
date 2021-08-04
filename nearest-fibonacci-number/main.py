import math


def nearest_fibonacci(number):
    """Finds the nearest Fibonacci number to a given positive integer(number).
    If there are more than one Fibonacci numbers with equal distance to the given number, return the smallest one."""
    fib_numbers = [0, 1]
    num_1, num_2 = 0, 1
    min_diff = 0

    for num in range(0, number):
        next_num = num_1 + num_2
        fib_numbers.append(next_num)
        num_1 = num_2
        num_2 = next_num

    if number in fib_numbers:
        nearest_fib_number = number
    else:
        for idx, numb in range(fib_numbers):
            num_diff = abs(numb-number)
            if num_diff <= min_diff:
                min_diff = num_diff
    return nearest_fib_number
