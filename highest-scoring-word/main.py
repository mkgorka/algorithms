def high(word):
    word_list = word.split(" ")
    highest_score_wrd = []
    max_counter = 0

    for idx, word in enumerate(word_list):
        sum = 0
        for letter in word:
            let_int = ord(letter) - 96
            sum += let_int

        if sum > max_counter:
            max_counter = sum
            highest_score_wrd.clear()
            highest_score_wrd.append(word_list[idx])

    return "".join(highest_score_wrd)
