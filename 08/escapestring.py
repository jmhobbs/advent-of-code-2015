import base64


class EscapedString (object):

    def __init__(self, string):
        self.string = string

    def unescape(self):
        real = []
        escape_sequence = None

        for c in self.string[1:-1]:
            if not escape_sequence:
                if "\\" == c:
                    escape_sequence = [c]
                else:
                    real.append(c)
            elif len(escape_sequence) == 2:
                escape_sequence.append(c)
            elif len(escape_sequence) == 3:
                real.append(chr(int(escape_sequence[2] + c, 16)))
                escape_sequence = None
            else:
                if len(escape_sequence) == 1:
                    if "x" == c:
                        escape_sequence.append(c)
                    else:
                        real.append(c)
                        escape_sequence = None
        return ''.join(real)

    @property
    def string_length(self):
        return len(self.unescape())

    @property
    def code_length(self):
        return len(self.string)
