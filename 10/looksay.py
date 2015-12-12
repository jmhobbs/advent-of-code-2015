
class LookAndSay (object):

    def __init__(self, start):
        self.start = start

    def iterate(self):
        last = None
        counter = 0
        chain = []
        for c in self.start:
            if c != last:
                if last is not None:
                    chain.append(str(counter))
                    chain.append(last)
                last = c
                counter = 1
            else:
                counter += 1
        chain.append(str(counter))
        chain.append(last)
        self.start = ''.join(chain)
        return self.start
