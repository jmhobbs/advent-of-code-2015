# -*- coding: utf-8 -*-


class LightGrid (object):
    # TODO: There is probably some bit twiddling that would be faster

    def __init__(self, width=1000, height=1000):
        self.width = width
        self.height = height
        self.grid = []
        for y in xrange(0, width):
            self.grid.append([])
            for x in xrange(0, height):
                self.grid[y].append(0)

    def parse_instruction(self, instruction):
        chunks = instruction.split(" ")
        # toggle 720,196 through 897,994
        if chunks[0] == "toggle":
            x1, y1 = chunks[1].split(",")
            x2, y2 = chunks[3].split(",")
            self.toggle(int(x1), int(y1), int(x2), int(y2))
        else:
            x1, y1 = chunks[2].split(",")
            x2, y2 = chunks[4].split(",")
            if "on" == chunks[1]:
                self.turn_on(int(x1), int(y1), int(x2), int(y2))
            else:
                self.turn_off(int(x1), int(y1), int(x2), int(y2))

    def turn_on(self, x1, y1, x2, y2):
        for y in xrange(y1, y2+1):
            for x in xrange(x1, x2+1):
                self.grid[y][x] = 1

    def turn_off(self, x1, y1, x2, y2):
        for y in xrange(y1, y2+1):
            for x in xrange(x1, x2+1):
                self.grid[y][x] = 0

    def toggle(self, x1, y1, x2, y2):
        for y in xrange(y1, y2+1):
            for x in xrange(x1, x2+1):
                self.grid[y][x] = not self.grid[y][x]

    def lights_on(self):
        counter = 0
        for y in xrange(0, self.height):
            for x in xrange(0, self.width):
                counter += self.grid[y][x]
        return counter

    def grid_to_string(self, on=u'▓', off=u'░'):
        rows = []
        for y in xrange(0, self.height):
            rows.append(u''.join(map(lambda v: on if v else off, self.grid[y])))
        return u"\n".join(rows)
