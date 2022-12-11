'''

4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

Входные и выходные данные хранятся в отдельных текстовых файлах.

aaaasssdddwwwwwwwwwwwweeeffffff -> 4a3s3d9w3w3e6f
4a3s3d9w3w3e6f-> aaaasssdddwwwwwwwwwwwweeeffffff

'''



with open('Ex4(Ввод).txt', 'r') as f:
    file_string = str(f.readline())
def RLE(string):
    result = ''
    i = 0
    while i < len(string):
        count = 1
        while i + 1 < len(string) and string[i] == string[i + 1]:
            count += 1
            i += 1
        result  += (str(count) + string[i])
        i += 1
    return  (result)

with open('Ex4(Вывод).txt' , 'w') as s:
    s.write(RLE(file_string))



with open('Ex4(Ввод).txt' , 'r') as g:
    file = "".join(g.readlines()[1:])
    print(file)
def TRY2(string):
    number1 = []
    str_2 = ''
    for i in range(0 , len(string)):
        try:
           number1.append(int(string[i]))
        except:
            str_2 += str(string[i])

    return(str_2)





def TRY(string , letter):
    g = 0
    lst = []
    result = ''
    while g < len(letter):
        for i in range(0, len(string) + 1):
            try:
                str_2 = ''
                if  isinstance(int(string[i]) , int) == True:
                    str_2 = str_2 + string[i]
                    if  isinstance(int(string[i + 1]) , int) == True:
                        str_2 = str_2 + string[i + 1]
                        result  = str(int(str_2) * letter[g])
                        #print(result)
                        lst.append(result)
                        g = g + 1
            except:
                str_2 = None
    return lst
print(TRY(file , TRY2(file)))


with open('Ex4(Вывод).txt' , 'a') as g:
    g.write(" ".join(TRY(file , TRY2(file))))


'''
res = ''
def TRY0(string):
    str_2 = ''
    for i in range(0 , len(string)):
        try:
            #while isinstance(int(file[i]) , str) != True:
                #number1.append(int(string[i]))
            #    res = res + list[i]
            str_2 =  str_2 + str(int(string[i]))
            if str_2 != '1':
                print(str_2)
            #string[i] = int(string[i])
            
        except:
            #str_2 += str(string[i])
            print(string[i] + 'b')
    #print(number1)
    #print(str_2)




#for i in range(0, len(file)):
#    if isinstance(int(file[i]) , str) == False:
#       res = res +  file[i]


#print(res)
'''

'''
i = 0
str_ = ''
number = 0
for i in range(0, len(file)):
    try:
        if isinstance(int(file[i]) , int) == False:
            str_ += file[i]
            i += 1
        else:
            i += 1
    except:
        str_ = ''

print(str_)



def TRY2(string):
    number1 = []
    str_2 = ''
    for i in range(0 , len(string)):
        try:
           number1.append(int(string[i]))
        except:
            str_2 += str(string[i])

    return(str_2)





def TRY(string , letter):
    g = 0
    lst = []
    result = ''
    while g < len(letter):
        for i in range(0, len(string) + 1):
            try:
                str_2 = ''
                if  isinstance(int(string[i]) , int) == True:
                    str_2 = str_2 + string[i]
                    if  isinstance(int(string[i + 1]) , int) == True:
                        str_2 = str_2 + string[i + 1]
                        result  = str(int(str_2) * letter[g])
                        #print(result)
                        lst.append(result)
                        g = g + 1
            except:
                str_2 = None
    return lst
print(TRY(file , TRY2(file)))


with open('Ex4(Вывод).txt' , 'a') as g:
    g.write(str(TRY(file , TRY2(file))))


'''