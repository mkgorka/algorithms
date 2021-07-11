def decipher_this(string):
  
""" Deciphers given string. For each word:
the second and the last letter is switched,
the first letter is replaced by its character code"""

    result_lst = []
    val_lst = []
    el_lst = []
    str_splitted = string.split(" ")
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for word in str_splitted:
        if word.isdecimal():
            int_word = int(word)
            letter = word.replace(word, chr(int_word))
            result_lst.append(letter)
        else:
            for idx, val in enumerate(word[:4]):
                if val in numbers:
                    val_lst.append(val)
                elif word[idx-1] in numbers and word[idx] not in numbers:
                    word_lst = list(word)
                    word_lst[idx], word_lst[-1] = word_lst[-1], word_lst[idx]
                    letter = word_lst[idx]
                    last_letter = word_lst[-1]
                    result_lst.append(letter)
                else:
                    pass
        str_val_lst = "".join(val_lst)
        result_lst.append(str_val_lst.replace(str_val_lst, chr(str_val_lst)))
    return result_lst
