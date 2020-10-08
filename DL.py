

li = []

def dpsum(n):
    li.append(0)
    for i in range(1, n+1):
        li.append(li[i-1] + i)

    print(li[n])

dpsum(6)