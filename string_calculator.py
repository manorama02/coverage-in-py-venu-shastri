def add(given_string):
    if given_string == "":
        return 0
    numbers_list = given_string.split(",")
    if len(numbers_list) == 1:
        return int(numbers_list[0])
    elif len(numbers_list) == 2:
        return int(numbers_list[0]) + int(numbers_list[1])
