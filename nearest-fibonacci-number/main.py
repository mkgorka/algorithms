import math


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
# def is_perfect_sqrt(number):
#     n = int(math.sqrt(number))
#     return n * n == number
#
# def is_fib_number(n):
#     return is_perfect_sqrt(5 * n * n + 4) or is_perfect_sqrt(5 * n * n - 4)
#
# if is_fib_number(number):
#     nearest_fib_number = number
# else:
#     for numb in range(0, number):
#         if is_fib_number(numb):
#             num_diff = abs(numb - number)
#             if num_diff <= min_diff:
#                 min_diff = num_diff
#                 min_diff_dct[numb] = min_diff
#         nearest_fib_number = min(min_diff_dct, key=min_diff_dct.get)
# print(nearest_fib_number)
# return nearest_fib_number

# if sqrt(5*number**2+4)%1==0 or sqrt(5*number**2-4)%1==0:
#     nearest_fib_number = number
# else:
#


nearest_fibonacci(1)
nearest_fibonacci(2)
nearest_fibonacci(9)
nearest_fibonacci(17)
nearest_fibonacci(54)
