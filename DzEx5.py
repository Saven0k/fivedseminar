'''
5* Дан список чисел. Найдите все возрастающие последовательности. Порядок элементов менять нельзя.

*Пример:*

[1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
'''

lst = [1, 5, 2, 3, 4, 6, 1, 7]

def psoled(lst):
    result = []
    for i in range(0, len(lst) + 2):
        if lst[i] < lst[i + 1]:
            result.append(lst[i])
        else:
            i = i + 1
    return result


print(psoled(lst))













