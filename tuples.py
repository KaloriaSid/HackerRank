n = int(input().strip())
list = input().split()
for i in range(n):
    list[i] = int(list[i])
t = tuple(list)
print(str(hash(t)))
