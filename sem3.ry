list_1 = [1,2,3,4,5,6]
#list = [1,1,2,0,-1,3,4,4]
'''
print(list)
for i in list:
    print(i)

print()
print(list_1[1])
print()
print((set(list)))
print(len(set(list)))
print(len(set(list_1)))

k = 3
for i in range(k):
    e = list_1.pop()
    list_1.insert(0, e)
print(list_1)
k = k % len(list_1)
print('Другое решение')
print(list_1[-k:] + list_1[:-k])

Задача No21. Решение в группахНапишите программу для печати
всех уникальных значений в словаре. 
Input:  [{"V": "S001"}, {"V": "S002"}, 
{"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "},
{" VIII ":" S007 "}] Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
'''
dict_1 ={'v' : 'olss'}
dict = [{"V": "S001"}, {"V": "S002"}, 
{"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "},
{" VIII ":" S007 "}]
'''  
for key in dict_1:
    print(key)
    print(dict_1[key])
 
for dbl in dict.items():
    print(dbl)

#напрямую значения
for val in dict.values():
    print(val)
'''
all_val = []
for new_dict in dict:
    #print(new_dict)
    for val in new_dict.values():
        all_val.append(val)
print(all_val)
print(set(all_val))