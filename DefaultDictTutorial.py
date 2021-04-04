n, m = map(int, input().split())


def getValue(x):
    l = []
    for _ in range(x):
        y = input()
        l.append(y)
    return l


groupA, groupB = getValue(n), getValue(m)

for i in range(m):
    flag = 0
    for j in range(n):
        if groupB[i] == groupA[j]:
            print(j+1, end=' ')
            flag = 1
    if flag == 0:
        print('-1')
    else:
        print()
