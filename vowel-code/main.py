vowel_dict = {"a": 1, "e": 2, "i":  3, "o": 4, "u": 5}


def encode(st):
    encoded = []
    for char in st:
        if char in vowel_dict and char == char.lower():
            en_char = char.replace(char, str(vowel_dict[char]))
            encoded.append(en_char)
        else:
            encoded.append(char)
    st = "".join(encoded)
    return st


def decode(st):
    decoded = []
    inverted_vowel_dict = {str(v): k for k, v in vowel_dict.items()}  # inverted dictionary

    for char in st:
        if char in inverted_vowel_dict:
            de_char = char.replace(char,inverted_vowel_dict[char])
            decoded.append(de_char)
        else:
            decoded.append(char)
    st = "".join(decoded)
    
    return st
