import math


a = float(22)
b = float(3)
c = float(9)

if a < 1 :
    x = 0

elif a >= 1 and a <= 10:
    x = b**2 - 4 + (c / 2)

elif a > 10 and a <= 20:
    x = a**2 * math.sqrt(c)

elif a > 20:
    x = a + (20 % 3) - math.sqrt(b)

print(x)