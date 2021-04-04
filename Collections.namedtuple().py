from collections import namedtuple

n, cNames = int(input()), input().split()
total = 0

for _ in range(n):
    values = namedtuple('values', cNames)
    c1, c2, c3, c4 = input().split()
    value = values(c1, c2, c3, c4)
    total += int(value.MARKS)

print('%0.2f' % (total/n))
