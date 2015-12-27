def extract_numbers_from_object(o):
    if type(o) == list:
        return extract_numbers_from_array(o)
    return extract_numbers_from_dictionary(o)


def extract_numbers_from_dictionary(dictionary):
    numbers = []
    for _, v in dictionary.items():
        if type(v) == int:
            numbers.append(v)
        elif type(v) == list:
            numbers.extend(extract_numbers_from_array(v))
        elif type(v) == dict:
            numbers.extend(extract_numbers_from_dictionary(v))
    return numbers


def extract_numbers_from_array(array):
    numbers = []
    for v in array:
        if type(v) == int:
            numbers.append(v)
        elif type(v) == list:
            numbers.extend(extract_numbers_from_array(v))
        elif type(v) == dict:
            numbers.extend(extract_numbers_from_dictionary(v))
    return numbers
