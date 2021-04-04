from collections import Counter

x = int(input())
shoeSizes = list(input().split())
avail = Counter(shoeSizes)
n = int(input())
totalAmount = 0

for _ in range(n):
    desiredSize, amount = input().split()
    value = avail[desiredSize]
    if value > 0:
        totalAmount += int(amount)
        value -= 1
        avail[desiredSize] = value

print(totalAmount)
