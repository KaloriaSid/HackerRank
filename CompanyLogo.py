from collections import Counter

s = input()
comm = Counter(sorted(s)).most_common(3)

for item in comm:
    print(item[0] + " " + str(item[-1]))
