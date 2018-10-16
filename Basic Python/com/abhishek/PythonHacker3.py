from cmath import polar
str1 = 1+2j
str2 = complex(str1)
print(str2)
polar = polar(str2)
print (polar[0])
print (polar[1])

import math
a = int(input())
b = int(input())
print(str(int(round(math.degrees(math.atan2(a,b)))))+"°")