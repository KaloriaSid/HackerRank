from itertools import permutations

str, k = input().split()

for p in sorted(list(permutations(str, int(k)))):
    for i in range(int(k)):
        print(p[i], end='')
    print()
