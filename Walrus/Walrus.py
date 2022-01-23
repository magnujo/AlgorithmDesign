
w = []
for i in range(int(input())):
    s = input()
    w.append(int(s))

print(w)
def OPT(i, weight, plates):

    if i == 0:
        return plates[0]

    res1 = OPT(i-1, weight, plates)-1000

    if (OPT(i-1, weight, plates)-)
    return min(abs(OPT(i-1, weight, plates)-1000), abs((OPT(i-1, weight, plates)+plates[i-1])-1000))

print(OPT(len(w)-1, 1000, w))


def itOPT()