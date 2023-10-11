'''
m = int(input("Введите число:"))
a = m // 100
b = m % 100 // 10
c = m % 10
res = a + b + c
print(res)

m = int(input("Введите число журавликов:"))
p = m // 6
k = p *4
print(p, k, p)

n = int(input("Введите номер билета:"))
a = n // 1000
print(a)
b = a // 100
c = a % 100 // 10
d = a % 10
leftres = b + d + c
print("сумма левой части=" , leftres)
a = n % 10
print(a)
n = n // 10
b = n % 10
print(b)
n = n // 10
c = n % 10
print(c)


righres = a + b + c
print("сумма правой части=" ,righres)
if (leftres == righres):
    print("YES")
else:
    print("NO")
'''
a = 3
b = 2
c = 1
if c < a * b and ((c % a == 0) or (c % b == 0)):
    print('yes')
else:
    print('no')