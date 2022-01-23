import sys
import timeit
import time


def knapsack():
    cases = []

    for line in sys.stdin:
        cap, numofobjects = map(int, line.split())
        values = []
        weights = []
        values.append(0)
        weights.append(0)

        for i in range(numofobjects):
            vp, wp = map(int, input().split())
            values.append(vp)
            weights.append(wp)

        cases.append((cap, values, weights))

    for case in cases:
        n = len(case[1]) - 1

        W = case[0]

        vals = case[1]

        wts = case[2]

        M = [[]]

        for w in range(W + 1):
            M[0].append(0)

        for i in range(1, n + 1):
            M.append([])
            prev = M[i - 1]
            line = M[i]
            for w in range(W + 1):

                if wts[i] > w:
                    line.append(prev[w])
                else:
                    line.append(max(prev[w], vals[i] + prev[w - wts[i]]))

        i = n
        j = W
        res = []
        while i > 0 and j > 0:
            if M[i][j] == M[i - 1][j]:
                i -= 1
            else:
                res.append(i - 1)
                j = j - wts[i]
                i -= 1

        l = len(res)
        print(l)
        for i in range(l):
            print(res.pop(), end=" ")

        print()


