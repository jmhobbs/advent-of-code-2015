import re


class SantaPasswordGenerator (object):

    def __init__(self, seed):
        self.password = seed

    def iterate(self):
        index = 0
        while True:
            index -= 1
            if index < 0:
                index = len(self.password) - 1
            c = self.password[index]
            if c == 'z':
                self.password = self.password[:index] + 'a' + self.password[index+1:]
            else:
                self.password = self.password[:index] + chr(ord(c) + 1) + self.password[index+1:]
                break
        return self.password


DOUBLE_CHECK = re.compile(r'(.)\1+')


def ElfPasswordCheck(string):
    if 'i' in string or 'o' in string or 'l' in string:
        return False

    first_double = DOUBLE_CHECK.search(string)
    if not first_double:
        return False

    second_double = DOUBLE_CHECK.search(string[first_double.start()+2:])
    if not second_double:
        return False

    a = ord('a')
    for i in xrange(0, 24):
        triple = chr(a+i) + chr(a+i+1) + chr(a+i+2)
        if triple in string:
            return True

    return False
