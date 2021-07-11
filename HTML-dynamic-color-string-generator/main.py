import random
import string


def generate_color_rgb():
    digits = string.digits
    letters = string.ascii_letters
    hash_symbol = "#"
    random_color_rgb = "".join(random.choices(letters+digits, k=6))

    hex_color = hash_symbol + random_color_rgb


    print(hex_color)
generate_color_rgb()
