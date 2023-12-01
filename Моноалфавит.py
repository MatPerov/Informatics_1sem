import random
class Monoalphabet:
    alphabet = "егпжонщюэбэчмяхыцилдшарсйзвьёктф"
    keytable = "шифрвженатакдльйоячёспгмзыхбцэую"
    def __init__(self, keytable):
        lowercase_code = {self.alphabet[i]:keytable[i] for i in range(len(self.alphabet))}
        uppercase_code = {self.alphabet[i].upper():keytable[i].upper() for i in range(len(self.alphabet))}
        self._encode = dict(lowercase_code)
        self._encode.update(uppercase_code)
        lowercase_code1 = {self.alphabet[i]:keytable[i] for i in range(len(self.keytable))}
        uppercase_code1 = {self.alphabet[i].upper():keytable[i].upper() for i in range(len(self.keytable))}
        self._decode = dict(lowercase_code1)
        self._decode.update(uppercase_code1)

    def encode(self, line):
        if len(line) == 1:
            return self._encode[line] if line in self._encode else line
        else:
            return ''.join([self.encode(char) for char in line])

    def decode(self, line):
        if len(line) == 1:
            return self._decode[line] if line in self._decode else line
        else:
            return ''.join([self.decode(char) for char in line])


key = Monoalphabet.keytable[:]
cipher = Monoalphabet(key)
line = input()
while line:
    print(cipher.decode(line))
    line = input()