from seating import parse_line


def test_parse_lines():
    assert ('Alice', -2, 'Bob') == parse_line('Alice would lose 2 happiness units by sitting next to Bob.')
    assert ('Bob', 5, 'David') == parse_line('Bob would gain 5 happiness units by sitting next to David.')
