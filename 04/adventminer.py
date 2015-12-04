import hashlib


class AdventMiner (object):

    def __init__(self, seed, zeros=5):
        self.seed = seed
        self.counter = 1
        self.zeros = zeros

    def run(self):
        comparison = "0" * self.zeros
        while True:
            h = hashlib.md5("%s%d" % (self.seed, self.counter)).hexdigest()
            if h[:self.zeros] == comparison:
                return self.counter
            self.counter += 1
