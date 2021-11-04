def order_weight(strng):
    strng_lst: list[str] = strng.split(" ")
    sum_number_pair_lst: list[int] = []
    digit_sum: int = 0
    sorted_strng_lst: list = []

    for number in strng_lst:
        for digit in number:
            digit = int(digit)
            digit_sum += digit
        sum_number_lst: list = [digit_sum, number]
        sum_number_pair_lst.append(sum_number_lst)
        digit_sum: int = 0
    sorted_sum_number_pair_lst: list = sorted(sum_number_pair_lst)

    for pair in sorted_sum_number_pair_lst:
        for el in pair:
            if isinstance(el, str):
                sorted_strng_lst.append(el)
    return " ".join(sorted_strng_lst)
