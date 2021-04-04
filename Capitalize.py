s = "1 w 2 r 3g"
l = s.split()
for i in l:
    s = s.replace(i, i.capitalize())
print(s)
