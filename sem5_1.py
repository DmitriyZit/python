'''
list1 = [1, 5, 5, 7, 9, 66, 77]
#print(len(set(list1)))
print("Введите сдвиг")
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

list1 =  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]

set1 = set()
for i in list1:
    
    for j in i:
        print(j)
        set1.add(i[j])
print(set1)