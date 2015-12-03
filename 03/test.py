from santa import Santa, SantaAndRoboSanta

###############################
# Problem 1


def number_of_houses_delivered_to(instructions, klass=Santa):
    santa = klass()
    for step in instructions:
        santa.move(step)
    return santa.first_deliveries


def test_case_1_1():
    # > delivers presents to 2 houses: one at the starting location, and one to the east.
    assert 2 == number_of_houses_delivered_to(">")


def test_case_1_2():
    # ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
    assert 4 == number_of_houses_delivered_to("^>v<")


def test_case_1_3():
    # ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
    assert 2 == number_of_houses_delivered_to("^v^v^v^v^v")


###############################
# Problem 2


def test_case_2_1():
    # ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
    assert 3 == number_of_houses_delivered_to("^v", SantaAndRoboSanta)


def test_case_2_2():
    # ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
    assert 3 == number_of_houses_delivered_to("^>v<", SantaAndRoboSanta)


def test_case_2_3():
    # ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
    assert 11 == number_of_houses_delivered_to("^v^v^v^v^v", SantaAndRoboSanta)
