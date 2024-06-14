'''
list = []
print(list)

print(list)
print(*list)
for i in list:
    print(i)

print(len(list))

list.append(102)
print(list)

for i in range(5):
    list.append(i)
    print(*list)

    ??????
    
t = (3, 3, 4,)
print(type(t))

fib1 = 1
fib2 = 1
 
n = input("Номер элемента ряда Фибоначчи: ")
n = int(n)
 
i = 0
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
 
print("Значение этого элемента:", fib2)


# Генератор списков
list_1 = []
for i in range(1, 101):
    if i % 2 == 0:
        list_1.append(i)
print(list_1)
# Или
list_1 = [i for i in range(1, 50) if i % 2 ==0]
print(list_1)

# Сдвиг в списке

list1 = [5, 4, 6, 7, -10]
k = int(input())
k = k % len(list1)

list_res = []

for i in range(k):
    list_res.append(list1[len(list1) - 1 - i])
print(list_res)

for i in range(len(list1) - k):
    list_res.append(list1[i])
print(list_res)

#Колличество раз когда больше

list1 = [0, -1, 5, 2, 3, 6]
count = 0

for i in range(1, len(list1)):
    if list1[i] > list1[i - 1]:
        count +=1
print(count)

a = int(input('Введите число a \n'))
b = int(input('Введите числ b \n'))

def f(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b < 0:
        return 1 / f(a, -b)
    else:
        return a * f(a, b-1)

res = f(a, b)
print(res)

'''

# Найти дружественные числа
k = int(input('Введите число ' ))
list1 = list()
for i in range(k):
    summ = 0
    for j in range(1, i//2 +1):
        if i % j == 0:
            summ += j
    list1.append(tuple([i, summ]))
for i in range(len(list1)):
    for j in range(i, len(list1)):
        if i != j and list1[i][0] == list1[j][1] and list1[i][1] == list1[j][0]:
            print(*list1[i])
        
    print("Такого числа нет")
