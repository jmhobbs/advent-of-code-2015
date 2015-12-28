from reindeerrace import Reindeer, ReindeerRace


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


def test_example_two():
    race = ReindeerRace()
    # Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
    race.racers['Comet'] = Reindeer(14, 10, 127)
    # Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
    race.racers['Dancer'] = Reindeer(16, 11, 162)

    # ...after the first second, Dancer is in the lead and gets one point.
    assert [('Dancer', 1), ('Comet', 0)] == race.race_new_scoring(1)
    assert [('Dancer', 2), ('Comet', 0)] == race.race_new_scoring(2)
    # ...after the 140th second, Comet pulls into the lead and gets his first point.
    # Of course, since Dancer had been in the lead for the 139 seconds before that,
    # he has accumulated 139 points by the 140th second.
    assert [('Dancer', 139), ('Comet', 1)] == race.race_new_scoring(140)
    # After the 1000th second, Dancer has accumulated 689 points, while poor Comet,
    # our old champion, only has 312.
    assert [('Dancer', 689), ('Comet', 312)] == race.race_new_scoring(1000)
