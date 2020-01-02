import operator

def palindrome(a):
    if str(a) == str(a)[::-1]:
        return "yes"
    return "no"

def nearPrime(a):
    val = 0
    for i in range(2, int(a) - 1):
        if (int(a)/i) % 1 == 0 and int(a)/i != i:
            val += 1
            if val > 2:
                return "no"
    return "yes"

def upNum(a):
    a = list(a)
    val = None
    for x in a:
        if val == None or int(x) >= val:
            val = int(x)
        else:
            return "no"
    return "yes"

def downNum(a):
    a = list(a)
    val = None
    for x in a:
        if val == None or int(x) <= val:
            val = int(x)
        else:
            return "no"
    return "yes"

def upDownNum(a):
    a = list(a)
    val = None
    i = -1
    for x in a:
        i += 1
        if val == None or int(x) >= val:
            val = int(x)
        elif downNum(str.join("", a[i:len(a)])) == "yes":
            return "yes"
        else:
            return "no"
    return "no"
    
def getScore(a, pal, nprime, nice):
    val = int(a)
    if pal:
        val *= 2
    if nprime:
        val *= 2
    if nice:
        val *= 3
    return val

Scores = {}
Nums = str.split(input("Enter an integer: "), ",")
for num in Nums:
    pal = False
    nprime = False
    nice = False
    if palindrome(num) == "yes":
        pal = True
    if nearPrime(num) == "yes":
        nprime = True
    if upNum(num) == "yes" or downNum(num) == "yes" or upDownNum(num) == "yes":
        nice = True
    score = getScore(num, pal, nprime, nice)
    if num not in Scores:
        Scores[num] = score
    else:
        Scores[str(num) + "Dupe"] = score

SortedScores = sorted(Scores.items(), key = operator.itemgetter(1))
for x in SortedScores:
    print(str(x[0]) + "," + str(x[1]))