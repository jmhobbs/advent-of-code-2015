from reindeerrace import Reindeer


def test_reindeer_sanity():
    rudolph = Reindeer(5, 4, 10)
    assert 20 == rudolph.race(4)
    assert 20 == rudolph.race(6)
    assert 20 == rudolph.race(14)
    assert 25 == rudolph.race(15)


def test_comet_example():
    # Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
    comet = Reindeer(14, 10, 127)
    # Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
    dancer = Reindeer(16, 11, 162)
    # After one second, Comet has gone 14 km, while Dancer has gone 16 km.
    assert 14 == comet.race(1)
    assert 16 == dancer.race(1)
    # After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km.
    assert 140 == comet.race(10)
    assert 160 == dancer.race(10)
    # On the eleventh second, Comet begins resting (staying at 140 km), and Dancer continues on for a total distance of 176 km.
    assert 140 == comet.race(11)
    assert 176 == dancer.race(11)
    # On the 12th second, both reindeer are resting.
    assert 140 == comet.race(12)
    assert 176 == dancer.race(12)
