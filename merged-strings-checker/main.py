def is_merge(s, part1, part2):
    result = ""
    total_length = len(part1) + len(part2)
    deposit = []
    p1_splt = [i for i in part1]
    p2_splt = [j for j in part2]

    if not s:
        result = "Value is not what was expected"

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
