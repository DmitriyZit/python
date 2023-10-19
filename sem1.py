"""
import math
n = int(input("????????? ???? ???? ? ????: "))
m = int(input("????????? ??????????: "))
res = m / n
print(math.ceil(res))

m = int(input("введите число: "))
i = 0
while  m != 0:
    print(m // 10)
    m = m // 10
    i += 1
print(i)
"""
import math
n = int(input("Введитите путь авто в день: "))
m = int(input("Введитите расстояние: "))
res = m / n
print(math.ceil(res))

m = int(input("Введите число: "))
i = 0
while  m != 0:
    print(m // 10)
    m = m // 10
    i += 1
print(i)
"""
# високосный год
n = int(input("Введитите год: "))
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print("YES")
else:
    print("NO")
