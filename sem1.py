"""
import math
n = int(input("????????? ???? ???? ? ????: "))
m = int(input("????????? ??????????: "))
res = m / n
print(math.ceil(res))
"""
m = int(input("введите число: "))
i = 0
while  m != 0:
    print(m // 10)
    m = m // 10
    i += 1
print(i)
