import math
import re


class Reindeer (object):

    def __init__(self, speed, duration, rest_length):
        self.speed = speed
        self.duration = duration
        self.rest_length = rest_length
        self.cycle_length = duration + rest_length

    def race(self, seconds):
        cycles = math.floor(seconds / float(self.cycle_length))
        remainder = seconds - cycles * self.cycle_length
        racing_seconds = min(self.duration, remainder)
        return (cycles * self.duration * self.speed) + racing_seconds * self.speed


class ReindeerRace (object):

    MATCHER = re.compile(r'([A-Za-z]+) can fly ([0-9]+) km/s for ([0-9]+) seconds, but then must rest for ([0-9]+) seconds.')

    def __init__(self):
        self.racers = {}

    def add_reindeer(self, line):
        # Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds.
        mo = self.MATCHER.match(line)
        self.racers[mo.group(1)] = Reindeer(int(mo.group(2)), int(mo.group(3)), int(mo.group(4)))

    def race(self, seconds):
        leader = []
        leader_distance = 0
        for name in self.racers:
            distance = self.racers[name].race(seconds)
            if distance > leader_distance:
                leader = [name]
                leader_distance = distance
            elif distance == leader_distance:
                leader.append(name)
        return (leader, leader_distance)

    def race_new_scoring(self, seconds):
        points = {}
        for name in self.racers:
            points[name] = 0
        for second in xrange(1, seconds + 1):
            result = self.race(second)
            for name in result[0]:
                points[name] += 1
        return sorted(zip(*zip(*points.items())), key=lambda r: r[1], reverse=True)

