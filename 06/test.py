from grid import LightGrid


def test_on():
    lg = LightGrid(3, 3)
    lg.turn_on(0, 0, 2, 2)
    assert lg.lights_on() == 9


def test_on_some():
    lg = LightGrid(6, 6)
    lg.turn_on(2, 2, 3, 3)
    assert lg.lights_on() == 4
