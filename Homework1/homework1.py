############################################################
# Section 2: Working with Lists
############################################################

def extract_and_apply(l, p, f):
    return [f(x) for x in l if p(x)]

def concatenate(seqs):
    return [x for y in seqs for x in y]

def transpose(matrix):
    final = []
    if len(matrix) > 0:
        i = 0
        while i < len(matrix[0]):
            row = []
            for x in range(len(matrix)):
                row.append(matrix[x][i])
            i += 1
            final.append(row)
    return final

############################################################
# Section 3: Sequence Slicing
############################################################

def copy(seq):
    return seq[:]

def all_but_last(seq):
    return seq[:len(seq) - 1]

def every_other(seq):
    return seq[::2]

############################################################
# Section 4: Combinatorial Algorithms
############################################################

def prefixes(seq):
    for i in range(len(seq) + 1):
        yield seq[:i]

def suffixes(seq):
    for i in range(len(seq) + 1):
        yield seq[i:]

def slices(seq):
    result = []
    for i in range(len(seq)):
        result.append(seq[i:i + 1])
        yield seq[i:i + 1]
        if seq[i:] not in result and len(seq[i:]) > 0:
            result.append(seq[i:])
            yield seq[i:]
        if seq[:i] not in result and len(seq[:i]) > 0:
            result.append(seq[:i])
            yield seq[:i]

############################################################
# Section 5: Text Processing
############################################################

def normalize(text):
    text = text.lower()
    text = " ".join(text.split())
    return text

def no_vowels(text):
    vowels = ["a", "e", "i", "o", "u"]
    return "".join([x for x in text if not x.lower() in vowels])

def digits_to_words(text):
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    return " ".join([nums[int(x)] for x in text if x.isdigit()])

def to_mixed_case(name):
    words = name.lower().split("_")
    final = ""
    for word in words:
        if final != "":
            final = final + word.capitalize()
        else:
            final = final + word
    return final

############################################################
# Section 6: Polynomials
############################################################

class Polynomial(object):

    def __init__(self, polynomial):
        self.tup = tuple(polynomial)

    def get_polynomial(self):
        return self.tup

    def __neg__(self):
        poly = list(self.tup)
        for i, x in enumerate(poly):
            x = list(x)
            x[0] = -x[0]
            poly[i] = tuple(x)
        return Polynomial(poly)

    def __add__(self, other):
        poly = list(self.tup)
        for x in other.tup:
            poly.append(x)
        return Polynomial(poly)

    def __sub__(self, other):
        poly = list(self.tup)
        neg = -other
        for x in neg.tup:
            poly.append(x)
        return Polynomial(poly)

    def __mul__(self, other):
        poly = []
        for x in self.tup:
            for y in other.tup:
                poly.append((x[0] * y[0], x[1] + y[1]))
        return Polynomial(poly)

    def __call__(self, x):
        return sum([coeff*(x**exp) for coeff,exp in self.tup])

    def simplify(self):
        temp = list(self.tup)
        dic = {}
        for x in temp:
            if x[1] not in dic.keys():
                dic[x[1]] = 0
            dic[x[1]] += x[0]
        temp = [(v, k) for k, v in dic.items()]
        for x in temp:
            if x[0] == 0:
                temp.remove(x)
        temp.sort(key = lambda temp: temp[1], reverse = True)
        if len(temp) == 0:
            temp = [(0,0)]
        self.tup = tuple(temp)

    def __str__(self):
        polyReadable = ""
        for x in self.tup:
            if polyReadable == "":
                if x[0] < 0:
                    polyReadable = "-"
            else:
                if x[0] < 0:
                    polyReadable = polyReadable + " - "
                elif x[0] >= 0:
                    polyReadable = polyReadable + " + "
            if abs(x[0]) != 1 or x[1] == 0:
                polyReadable = polyReadable + str(abs(x[0]))
            if x[1] != 0:
                polyReadable = polyReadable + "x"
                if x[1] != 1:
                    polyReadable = polyReadable + "^" + str(x[1])
        return polyReadable
