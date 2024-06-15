'''
max = int(input("Введите максимальное число массива: ")) 
min = int(input("Введите минимальное число массива: ")) 
list_1 = [-5, 9, 0, 30, -1, -2, 1, 4, -2, 10, 2, 0, -9, 80, 10, -9, 0, -5, -5, 7]

for i in range(len(list_1)): 
    if min <= list_1[i] <= max: 
        print(i)


a1 = int(input("Введите первый элемент массива: "))
d = int(input("Введите разность элементов массива: ")) 
n = int(input("Введите количество элементов массива: "))

for i in range(n): 
    print(a1 + i * d)



def print_operation_table(operation, num_rows = 6, num_columns = 6): 
    for i in range(1, num_rows + 1): 
        a = [] 
        for j in range(1, num_columns + 1): 
            a.append(str(operation(i, j))) 
            print(" ".join(f"{e:<4}" for e in a)) 
    print_operation_table(lambda x, y: x * y)

'''


import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})

one_hot_encoded = pd.get_dummies(data, columns=['whoAmI'])

print(one_hot_encoded.head())