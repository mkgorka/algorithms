def pig_it(text):
    """Solution for task: https://www.codewars.com/kata/520b9d2ad5c005041100000f"""
    suffix = "ay"
    text_splt = text.split(" ")
    result = []

    for word in text_splt:
        if word.isalpha():
            first_letter = word[0]
            temp_lst = list(word)
            temp_lst[0] = ""
            n_word = "".join(temp_lst) + first_letter
            res = n_word+suffix
            result.append(res)
        else:
            result.append(word)
    return " ".join(result)
