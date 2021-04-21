print('Необходимо номера дел из файлов excel сохранить в текстовые файлы с именами: ')
print('форма 5.txt и форма 1.txt. Кавычки удалить заранее!')
print('Результат будет выведен в соответствующий файл')
input()


#чтение в списки из файлов
with open("форма 5.txt") as file:
    f5Data = [row.strip() for row in file]

with open("форма 1.txt") as file:
    f1Data = [row.strip() for row in file]


#номера, которые есть в ПРОШЛОМ году, но которых нет в ТЕКУЩЕМ году
unicFromF5Prev = []
i = 0
for el in f5Data:
    if not el in f1Data:
        unicFromF5Prev.insert(i,el)
    i += 1


#номера, которые есть в ТЕКУЩЕМ году, но которых нет в ПРОШЛОМ году
unicFromF1Prev = []
i = 0
for el in f1Data:
    if not el in f5Data:
        unicFromF1Prev.insert(i,el)
    i += 1


#удаление повторяющихся элементов
unicFromF5 = list(set(unicFromF5Prev))
unicFromF1 = list(set(unicFromF1Prev))


print(unicFromF5)
print(unicFromF1)


#запись в файл 2х множеств
outputFile = open('результат.txt','w', encoding='utf-8')
outputFile.write('дела, которые есть в форме 1 и нет в форме 5:')
outputFile.write('\n')
for el in unicFromF1:
    outputFile.write(el)
    outputFile.write('\n')

outputFile.write('\n')

outputFile.write('дела, которые есть в форме 5 и нет в форме 1:')
outputFile.write('\n')
for el in unicFromF5:
    outputFile.write(el)
    outputFile.write('\n')
outputFile.close()
