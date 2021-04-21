# программа выдает результат такого типа. Нужно для заполнения файлов при создании отчетов в АРМ Статистика
#t3 u3 v3 w3 x3
#t4 u4 v4 w4 x4
#t5 u5 v5 w5 x5
#t6 u6 v6 w6 x6

import string
outputf = open('output.txt', 'w', encoding='utf8')
dz = string.ascii_lowercase
abcde = [i for i in dz]
startLetter = input("С какой буквы начинаем: ")
countRows = int(input("Сколько граф надо: "))
startString = int(input("С какой строки начинаем: "))
countStrings = int(input("Сколько строк надо: "))
for i in range(26):
    letter = str(abcde[0]) + str(abcde[i])
    abcde.append(letter)
abcdeFin = abcde[abcde.index(startLetter):]
abcdeFin = abcdeFin[:countRows]

for i in range(countStrings):
    for j in range(len(abcdeFin)):
        print(abcdeFin[j], i + startString, sep='', end=' ', file=outputf)
    print(file=outputf)
