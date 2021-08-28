def is_merge(s, part1, part2):
    """Solution for https://www.codewars.com/kata/54c9fcad28ec4c6e680011aa
    Checks if a given string s can be formed from two other given strings - part1 and part2
    so that characters in part1 and part2 are in the same order as in given string s."""
    result = ""
    total_length: int = len(part1) + len(part2)
    deposit: list = []
    p1_splt: list = [i for i in part1]
    p2_splt: list = [j for j in part2]

    if not s:
        result = 'Value is not what was expected'

    if len(s) == total_length:
        for idx, el in enumerate(s):
            if len(p1_splt) > 0 and el == p1_splt[0]:
                result = True
                p1_splt.remove(el)
                if len(p2_splt) > 0 and el == p2_splt[0]:
                    deposit.append(el)
                    p2_splt.remove(el)
            elif len(p2_splt) > 0 and el == p2_splt[0]:
                result = True
                p2_splt.remove(el)
            elif not p1_splt or el != p1_splt[0] and not p2_splt or el != p2_splt[0]:
                if len(deposit) > 0 and el == deposit[0]:
                    result = True
                    deposit.remove(el)
                elif not deposit or el != deposit[0]:
                    return False
            else:
                return False
        return result
    else:
        return False
