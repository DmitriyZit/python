
#print("Введети сколько нужно проехать:")
#n = int(input())
#m = int(input("Сколько проезжает за день:"))
#m = 700
#res = (n + (m-1)) // m
#print(res, 'день')
#print(((-n) // m)*(-1))
'''
print("Сколько людей в 1 классе")
a = int(input())
print("Сколько людей в 2 классе")
b = int(input())
print("Сколько людей в 3 классе")
c = int(input())
a = (((-a) // 2)*(-1))
b = (((-b) // 2)*(-1))
c = (((-c) // 2)*(-1))
print("Нужно закупить", (a + b + c), "парты")
print(f"Колличество парт = {a + b + c}")
'''
m = int(input("Введите год:"))
if ((m % 4 == 0) and (m % 100 != 0)) or (m % 400 == 0):
    print("YES")
else:
    print("NO")