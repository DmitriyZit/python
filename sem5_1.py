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


list1 =  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]

set1 = set()
for i in list1:
    
    for j in i:
        print(j)
        set1.add(i[j])
print(set1)

list1 = [0, 5, 3, 8, 9]
count = 0

for i in range(1, len(list1)):
    if list1[i] > list1[i - 1]:
        count +=1
print(count)


list_1 = [3, 2, 3, 3, 5]
k = 3

res = 0
for i in range(len(list_1)):
    if list_1[i] == k:
    
        res += 1
print(res)


list_1 = [3, 2, 3, 3, 5]
k = 5

for i in range(len(list_1)):
    if list_1[i] == k:
        print(list_1[i])



list_1 = [13, 22, 3, 4, 5, 9, 10] 
k = 6

num = 0

#for i in range(len(list_1)):
#   if list_1[i] == k:
#        print(list_1[i])

for i in range(0, len(list_1)): 
    if list_1[i] < k: 
        num = -k 
        print(num)
        
    else: 
        num = num + 0
    if list_1[i] >= k and list_1[i] - k <= num - k: 
        num = list_1[i] 
        print(num)
        
    elif list_1[i] <= k and num - k <= list_1[i] - k: 
        num = list_1[i] 
        
print(num)

'''
list_1 = [1, 2, 3, 4, 5] 
k = 5
num = list_1[0]
#print(num)
for i in range(len(list_1)): 
    if abs(list_1[i] - k) < abs(num - k): 
        num = list_1[i] 
        print(num)
    else:
        

        print(num)
        
