"""
print("введите 1 число")

n = int(input())
print("введите 2 число")
m = int(input())

print((m + n - 1)//n )

print("введите число учеников в 1 классе")
a = int(input())
a = (a + 1) // 2

print("введите число учеников во 2 классе")
b = int(input())
b = (b + 1) // 2

print("введите число учеников в 3 классе")
c = int(input())
c = (c + 1) // 2

res = a + b + c

print(res)


print("введите N")
i = int(input())

print("введите N1")
j = int(input())

if i - j == 0:
    print("не можем")
else:
    print(j + i - 1)
"""
print("введите ГОД")
i = int(input())
if i % 4 == 0 and i % 100 != 0 or i % 100 == 0:
    print("YES")
else:
    print("NO")