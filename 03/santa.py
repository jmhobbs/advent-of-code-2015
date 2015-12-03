class Santa (object):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.grid = {}
        self.first_deliveries = 0
        self.deliver()

    def deliver(self):
        if self.x not in self.grid:
            self.grid[self.x] = {self.y: 0}
        elif self.y not in self.grid[self.x]:
            self.grid[self.x][self.y] = 0

        if self.grid[self.x][self.y] == 0:
            self.first_deliveries += 1

        self.grid[self.x][self.y] += 1

    def move(self, step):
        if step == ">":
            self.x += 1
        elif step == "<":
            self.x += -1
        elif step == "^":
            self.y += 1
        elif step == "v":
            self.y += -1
        self.deliver()
