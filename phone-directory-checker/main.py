import re

def phone(strng, num):
    arr = strng.splitlines()
    result_arr = []
    counter = 0
    address = "adres"
    name = "name"

    for i in arr:
        if num in i:
            result_arr.append(i)
            counter += 1
        if counter > 1:
            result = f"Error => Too many people: {num}"
        elif counter == 0:
            result = f"Error => Not found: {num}"
        elif counter == 1:
            for el in result_arr:
                op_idx = el.index("<")
                cl_idx = el.index(">")
                name = el[op_idx:cl_idx].strip("<")
                i_el = re.sub('[<>,$+;/]', '', el)
                n_el = i_el.replace(name, '')
                nn_el = n_el.replace(num, '')

                address = " ".join(nn_el.split())
            result = f"Phone => {num}, Name => {name}, Address => {address}"
    return result
