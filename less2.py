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
'''
#Колличество раз когда больше

list1 = [0, -1, 5, 2, 3, 6]
count = 0

for i in range(1, len(list1)):
    if list1[i] > list1[i - 1]:
        count +=1
print(count)