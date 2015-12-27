def extract_numbers_from_object(o, dead_red=False):
    if type(o) == list:
        return extract_numbers_from_array(o, dead_red)
    return extract_numbers_from_dictionary(o, dead_red)


def extract_numbers_from_dictionary(dictionary, dead_red=False):
    numbers = []
    for k, v in dictionary.items():
        if dead_red and "red" == v:
            return []
        elif type(v) == int:
            numbers.append(v)
        elif type(v) == list:
            numbers.extend(extract_numbers_from_array(v, dead_red))
        elif type(v) == dict:
            numbers.extend(extract_numbers_from_dictionary(v, dead_red))
    return numbers


def extract_numbers_from_array(array, dead_red=False):
    numbers = []
    for v in array:
        if type(v) == int:
            numbers.append(v)
        elif type(v) == list:
            numbers.extend(extract_numbers_from_array(v, dead_red))
        elif type(v) == dict:
            numbers.extend(extract_numbers_from_dictionary(v, dead_red))
    return numbers
