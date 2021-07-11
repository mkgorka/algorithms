def kebabize(string):
    result = []
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for char in string:
        if ord(char) in range(65, 91):
            s_char = " " + char
            result.append(s_char)
        elif char in numbers:
            result.append("")
        else:
            result.append(char)

    inter_string = "".join(result).lower().strip().replace(" ", "-")
    final_result = inter_string.replace(" ", "-")
    return final_result
