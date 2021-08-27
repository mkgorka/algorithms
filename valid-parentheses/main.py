def valid_parentheses(string):
    open_char_counter: int = 0
    close_char_counter: int = 0
    string_lst = [el for el in string]
    for element in string_lst:
        if close_char_counter <= open_char_counter:
            if element == "(":
                open_char_counter += 1
            elif element == ")":
                close_char_counter += 1

    if open_char_counter == close_char_counter:
        return True
    else:
        return False
