def high(word):
  
    """Given a string of words, find the highest scoring word.
    Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
    Return the highest scoring word as a string."""

    word_list = word.split(" ")
    highest_score = []
    max_counter = 0

    for idx, word in enumerate(word_list):
        total_sum = 0
        for letter in word:
            let_int = ord(letter) - 96
            total_sum += let_int

        if total_sum > max_counter:
            max_counter = total_sum
            highest_score.clear()
            highest_score.append(word_list[idx])

    return "".join(highest_score)
