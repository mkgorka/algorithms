def high_and_low(numbers):
    numbers_list = numbers.split()
    comp_list = [int(i) for i in numbers_list]
    comp_list.sort()
    min_value = comp_list[0]
    max_value = comp_list[-1]
    numbers = str(max_value) + " " + str(min_value)
    return numbers
