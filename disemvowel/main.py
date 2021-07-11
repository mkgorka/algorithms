def disemvowel(string):
    vowel = "aeiouAEIOU"
    vowel_string = ""
    disemvoweled_string = ""

    for char in string:
        if char in vowel:
            vowel_string += char
        else:
            disemvoweled_string += char
    return disemvoweled_string
