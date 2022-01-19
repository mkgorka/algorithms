def next_bigger(number):
    digit_lst: list = [int(digit) for digit in str(number)]
    digit_lst_reversed = list(reversed(digit_lst))

    for idx_i, i in enumerate(digit_lst_reversed[1::]):
        for idx_j, j in enumerate(digit_lst_reversed):
            if i < j:
                idx_i, idx_j = digit_lst_reversed.index(i), digit_lst_reversed.index(j)
                digit_lst_reversed[idx_i], digit_lst_reversed[idx_j] = digit_lst_reversed[idx_j], digit_lst_reversed[
                    idx_i]
                next_bigger_number_lst: list = (list(reversed(digit_lst_reversed)))
                next_bigger_number_to_str: str = "".join(map(str, next_bigger_number_lst))
                next_bigger_number: int = int(next_bigger_number_to_str)
                return next_bigger_number


