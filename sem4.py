''
Задача №25. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

l = 'a d f gh j k u y d c'.split(' ')
st = set('jhcfkijskjf')
s = list('hiscjsics')
print(l)
print(st)
print(s)
'''

st = 'a a a b c a a d c d d'.split()
print(st)
#print(*st)
s = ''
for i  in range(len(st)):
    s = st[:i]
    #print(f'st[i] + _')
    #if n[i] not in s
    if s.count(st[i]) == 0:
        print(st[i], end=' ')
        
    else:
        print(f'{st[i]}_{s.count(st[i]) +1}',end=' ')
    
    #print(st[i], end =' ')
    #print(f'st[i] + _')

Семинар 4. Словари, множества и профилирование
Задача №27. Общее обсуждение
Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов или символами конца строки.Определите,
сколько различных слов содержится в этом тексте.
Input: She sells sea shells on the sea shore;The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore,I'm sure that the shells are sea
shore shells. Output: 19

tex = 'She sells sea shells on the sea shore. The shellst hat she sells are sea shells m sure. So if she sells sea shells on the sea shore,I that the shells are sea shore shells'.split()
print(tex)
text = 'She sells sea shells on the sea shore. The shellst hat she sells are sea shells m sure. So if she sells sea shells on the sea shore,I that the shells are sea shore shells'
print(tex)
'''
t = (len(set(input().split())))
print(t)

'''
count = 0
for i in range(len(text)):
    print(i)
    #if i == ' ':
    #count +=1
print(count)


еминар 4. Словари, множества и профилирование
Задача №29. Решение в группах
Ваня и Петя поспорили, кто быстрее решит
следующую задачу: “Задана последовательность
неотрицательных целых чисел. Требуется определить
значение наибольшего элемента
последовательности, которая завершается первым
встретившимся нулем (число 0 не входит в
последовательность)”. Однако 2 друга оказались не
такими смышлеными. Никто из ребят не смог до
конца сделать это задание. Они решили так: у кого
будет меньше ошибок в коде, тот и выиграл спор. За
помощью товарищи обратились к Вам, студентам.

print('Введите число')
n = int(input())
'''
m = 0
n = 1
while (n != 0):
    print('Введите число')
    n = int(input())
    if n > m:
        m = n
        print('tt')
print(m)

#маржовые операторы

m = 0
while (n := int(input())) != 0:
    if n >m:
        m = n
print(m)

    
