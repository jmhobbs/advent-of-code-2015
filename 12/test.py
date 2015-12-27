from elfaccounting import extract_numbers_from_dictionary, extract_numbers_from_array


def test_flat_objects():
    # [1,2,3] and {"a":2,"b":4} both have a sum of 6.
    assert [1, 2, 3] == extract_numbers_from_array([1, 2, 3])
    assert [2, 4] == extract_numbers_from_dictionary({"a": 2, "b": 4})
    # [] and {} both have a sum of 0.
    assert [] == extract_numbers_from_array([])
    assert [] == extract_numbers_from_dictionary({})


def test_nesting():
    # [[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
    assert [3] == extract_numbers_from_array([[[3]]])
    assert [4, -1] == extract_numbers_from_dictionary({"a":{"b":4},"c":-1})
    # {"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
    assert [-1, 1] == extract_numbers_from_dictionary({"a":[-1,1]})
    assert [-1, 1] == extract_numbers_from_array([-1,{"a":1}])
