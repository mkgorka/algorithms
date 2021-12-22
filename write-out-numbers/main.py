def number2words(num):
    ''' Solution for Codewars challenge: https://www.codewars.com/kata/52724507b149fa120600031d '''

    n_lst = [int(el) for el in str(num)]
    words_lst: list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                       "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
                       "nineteen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if num <= 20:
        num_word = words_lst[num]
    elif 20 < num < 100:
        if num % 10 == 0:
            sign: str = ""
        else:
            sign: str = "-"

        if n_lst[1] == 0:
            num_word = words_lst[18 + num // 10]
        else:
            num_word = words_lst[18 + num // 10] + sign + words_lst[n_lst[1]]
    elif 100 <= num < 1000:
        tens_lst: list = [str(elem) for elem in n_lst[1:]]
        tens_int: int = int("".join(tens_lst))
        if tens_int > 10:
            tens = words_lst[18 + (tens_int // 10)]
        else:
            tens = words_lst[tens_int]
        if n_lst[1] == 0 and n_lst[2] == 0:
            num_word = words_lst[n_lst[0]] + " hundred"
        elif n_lst[1] == 0:
            num_word = words_lst[n_lst[0]] + " hundred " + tens
        elif n_lst[2] == 0:
            num_word = words_lst[n_lst[0]] + " hundred " + tens
        else:
            units = "-" + words_lst[n_lst[2]]
            num_word = words_lst[n_lst[0]] + " hundred " + tens + units
    elif 1000 < num < 10000:
        pass
    return num_word
