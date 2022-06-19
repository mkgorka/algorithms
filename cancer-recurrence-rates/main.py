def recurrence(values):
    increase: int = 0
    increase_lst: list = []
    modified_increase_lst: list = []
    nadir_value: float = min(values)
    value_len: int = len(values)
    for idx, val in enumerate(values):
        if val == nadir_value:
            nadir_value_idx: int = idx
            break

    after_nadir_lst: list = values[nadir_value_idx:value_len]

    for idx, value in enumerate(after_nadir_lst):
        if idx < len(after_nadir_lst) - 1:
            if value < after_nadir_lst[idx + 1]:
                increase += 1
                increase_lst.append(value)
                if increase == 3:
                    increase_lst.append(after_nadir_lst[idx + 1])
                    break
            else:
                increase_lst.clear()
                increase = 0
    if increase == 3:
        for idx, val in enumerate(increase_lst[:-1]):
            sign: str = "->"
            increase_val: float = increase_lst[idx + 1]
            element: list = [str(val), sign, str(increase_val)]
            values_el = "".join(element)
            modified_increase_lst.append(values_el)

        verdict = "True" + "\n# Nadir " + str(nadir_value) + ", 3 subsequent rises: " + ", ".join(modified_increase_lst)
        return True
    else:
        verdict = "False" + "\n# Nadir " + str(nadir_value) + ". No subsequent sequence of 3 consecutive rises."
        return False
    return verdict



