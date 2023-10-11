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
'''
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
