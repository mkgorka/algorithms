def dashatize(n: int):
<<<<<<< HEAD
    """Solution for the challenge: https://www.codewars.com/kata/58223370aef9fc03fd000071"""
=======
    """Solution for Codewars challenge: https://www.codewars.com/kata/58223370aef9fc03fd000071"""
>>>>>>> ac8335b1cb76d6821cce8143a01ecfd3e43d11f6
    n_str = [int(x) for x in str(n)]
    result_list = [str(n_str[0])]

    for index in range(1, len(n_str)):
        current = n_str[index]
        if current % 2 == 1 or n_str[index - 1] % 2 == 1 and current % 2 == 0:
            el_signed = "-" + str(current)
            result_list.append(el_signed)
        else:
            result_list.append(current)
    result = "".join(result_list).strip("-")
    return result
