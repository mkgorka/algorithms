def highest_rank(arr):
    val_dict = {}

    for val in arr:
        if val in val_dict:
            counter = val_dict[val]
            counter += 1
            val_dict[val] = counter
        else:
            counter = 1
            val_dict[val] = counter
    print(val_dict)

    max_count = max(val_dict.values())
    key_max_count = [k for k, v in val_dict.items() if v == max_count]
    print(max_count, key_max_count)
    return max(key_max_count)
