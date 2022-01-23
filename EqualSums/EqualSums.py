
def parse():
    num_of_testcases = int(input())
    sets = []
    for s in range(num_of_testcases):
        set = list(map(int, input().split()))
        sets.append(set[1:])
    print(sets)

    curSet = sets[1]
    sumlist = []
    tempSum = 0

    for num in curSet:
        tempSum = tempSum + num
        sumlist.append(tempSum)
        print(tempSum)

    i = 0

    for num in sumlist:
        if num == curSet[i]:
            return True
        i += 1

    return False

    print(sumlist)
print(parse())