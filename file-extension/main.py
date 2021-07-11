def extract_file_name(dirty_file_name):
    dot_counter = 0
    arr = []
    for idx, i in enumerate(dirty_file_name):
        if i == "_":
            slice_file_name = dirty_file_name[idx + 1::]
            break
    for char in slice_file_name:
        arr.append(char)
        if char == ".":
            dot_counter += 1

            if dot_counter == 2:
                el = arr[:-1]
                break
    return "".join(el)
