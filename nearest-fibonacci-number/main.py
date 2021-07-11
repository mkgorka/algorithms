def nearest_fibonacci(number):
    """Finds the nearest Fibonacci number to a given a positive integer(number).
    If there are more than one Fibonacci numbers with equal distance to the given number, returns the smallest one."""
    numbers=[]
    curr_num, next_num = 0, 1
    nth_fib_num = curr_num + next_num

    while nth_fib_num < number:
        numbers.append(nth_fib_num)
        nth_fib_num = curr_num + next_num
        curr_num = next_num
        next_num = nth_fib_num




nearest_fibonacci(8)
