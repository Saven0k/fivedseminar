'''
# Используем map
1. В файле находится N натуральных чисел, записанных через пробел.
Среди чисел не хватает одного, чтобы выполнялось условие
A[i] - 1 = A[i-1]. Найдите это число.

5 6 7 8 9 10 12 13


past_el = None

with open('first.txt') as f:
    for i in map(int, f.read().split( )):
        if past_el is None:
            past_el = i
        else:
            if i != past_el + 1:
                print(past_el + 1)
            past_el = i

quit()

# Используем filter
2. Напишите программу, удаляющую из текста все слова, содержащие "абв".



a = "привет абв пока абвг"
end_str = " ".join(list(filter(lambda x: not 'aбв' in x, a.split())))
print(end_str)

print(" ".join(list(filter(lambda x: not 'абв' in x, "привет абв пока абвг".split()))))




3. Дан список чисел. Создайте список, в который попадают числа, описываемые
возрастающую последовательность. Порядок элементов менять нельзя.
 
*Пример:*

[1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
'''

lst = [1, 5, 2, 3, 4, 6, 1, 7]
res = []
i = 0
k = 0
for j, item in enumerate(lst):
    res.append([item])
    print(res)
    for i in range(j ,len(lst) - 1):
        if lst[i] > res[j][k]:
            res[j].append(lst[i])
            k += 1
    k = 0
print(res)


'''
array = [1, 5, 2, 3, 4, 6, 1, 7]

for i in range(len(array)):
arr_n = [1]
arr_n[0] = array[0]
for j in range(i, len(array)):
if array[j] > arr_n[-1]:
arr_n.append(array[j])

print(arr_n)
'''

















