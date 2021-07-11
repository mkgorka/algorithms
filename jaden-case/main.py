def to_jaden_case(string):
    for i in string:
        print(i)
        if i == "a":
            new_letter = i.upper()
            replaced =  string.replace(i, new_letter)
        replaced.join("")
    print(replaced)



to_jaden_case("How can mirrors be real if our eyes aren't real")