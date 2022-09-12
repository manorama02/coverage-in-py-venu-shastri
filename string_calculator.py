def checkempty(str):
    return str==""
def get_number_list(str):
    return [int(n) for n in str.split(",")]
def add(given_string):
    if checkempty(given_string):
        return 0
    numbers_list = get_number_list(given_string)
    return sum(numbers_list)
