import math

ab, bc = int(input()), int(input())

angle = math.atan2(ab, bc)

print(str(round(math.degrees(angle))) + chr(176))
