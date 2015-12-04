import hashlib


class AdventMiner (object):

    def __init__(self, seed):
        self.seed = seed
        self.counter = 1

    def run(self):
        while True:
            h = hashlib.md5("%s%d" % (self.seed, self.counter)).hexdigest()
            if h[:5] == "00000":
                return self.counter
            self.counter += 1
