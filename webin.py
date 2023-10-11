'''
print("Привет")
a = 0
print(a)
print("Привет" + str(a))
pas = 'secret'
m = input("введи пароль  ")
if m == pas:
    print("YES")
print("NO")
while pas != m:
    print("no")
    m = input("попробуй еще  ")
print("YES")
'''
''' Найти число которое загадал 
'''
from random import randint 
number = randint(1, 100)  # генерация числа
print(number)
for i in range(1, 11):
    print("попытка", i)
    a = int(input("Угадай число  "))
    if number == a:
        print("YES")
        break
    elif a < number:
        print("число меньше загаданного")
    elif a > number:
        print("число больше загаданного")
