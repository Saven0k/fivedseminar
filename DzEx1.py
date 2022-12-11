#1 Напишите программу, удаляющую из файла все слова, содержащие "абв".

with open('first.txt', 'r') as f:
    lst = list(f.readline().split())
print(lst)
end_str = filter(lambda x:  'abv' not in x.lower(), lst)
print(*end_str)