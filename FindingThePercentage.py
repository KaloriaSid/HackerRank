n = int(input().strip())
info = {}

for i in range(n):
    x = input().strip().split()
    info[x[0]] = x[1:4]

name = input().strip()
numbers = info.get(name)

for i in range(len(numbers)):
    numbers[i] = float(numbers[i])

print('%0.2f' % (sum(numbers) / len(numbers)))
