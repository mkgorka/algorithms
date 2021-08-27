def valid_parentheses(string):
    """Solution for task: https://www.codewars.com/kata/52774a314c2333f0a7000688
    Determines if the order of the parentheses from the given string is valid."""
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
