from santa import Santa


def number_of_houses_delivered_to(instructions):
    santa = Santa()
    for step in instructions:
        santa.move(step)
    return santa.first_deliveries


def test_case_1():
    # > delivers presents to 2 houses: one at the starting location, and one to the east.
    assert 2 == number_of_houses_delivered_to(">")


def test_case_2():
    # ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
    assert 4 == number_of_houses_delivered_to("^>v<")


def test_case_3():
    # ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
    assert 2 == number_of_houses_delivered_to("^v^v^v^v^v")
