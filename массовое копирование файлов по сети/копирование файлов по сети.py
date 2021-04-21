# программа копирует содержимое папки "Files to copy" на АРМы в папку "C:\Статистика v3.2\ФОРМЫ"
# имена компьютеров берутся из файла "destination.txt"
# копирование происходит с заменой
# в логи записывается некоторая информация


def copyFiles(srcFolder, dstFolder):
    if os.path.isdir(srcFolder):
        # проверка: если нет папки назначения, то создаем ее
        if not os.path.exists(dstFolder):
            os.mkdir(dstFolder)
        makeList(srcFolder, dstFolder)
    elif os.path.isfile(srcFolder):
        shutil.copyfile(srcFolder, dstFolder)


def makeList(srcFold, dstFold):
    fileList = os.listdir(srcFold)

    # проверка: если нет папки назначения, то создаем ее
    if not os.path.exists(dstFold):
        os.mkdir(dstFold)

    for sbj in fileList:
        srcFile = srcFold + "\\" + sbj
        dstFile = dstFold + "\\" + sbj
        copyFiles(srcFile, dstFile)



def getPCs():
    inpFile = open("destination.txt", "r", encoding="utf-8")
    list = []
    for line in inpFile:
        if line[-1] == '\n':
            list.append(line[:-1])
        else:
            list.append(line)

        #if line.strip():  # для не записи пустых строк в множество
         #   list.append(line[:-1])

    list = set(list)
    toRemovePC = []  # сюда будут записаны имена компьютеров, путь до которых не найден
    for pc in list:
        if not os.path.exists("\\\\" + pc + "\\" + "c$"):
            toRemovePC.append(pc)

    # удаление компьютеров, путь до которых не найден из списка для обработки
    for pc in toRemovePC:
        list.discard(pc)

    errorsCatch(toRemovePC, 'noPC')

    return list


# для заполнения лога с ошибками
def errorsCatch(pc, errorType):
    logErFile = open("log_errors.txt", "a", encoding="utf-8")

    # проверка на отсутствие доступа к АРМам
    if errorType == "noPC" and len(pc) != 0:
        logErFile.write(r'Не найден компьютер *** или нет доступа по пути: \\***\с$. Компьютеры:' + '\n')
        for el in pc:
            logErFile.write(el +'\n')

    # проверка на то, что есть файлы для копирования
    if errorType == "nullList":
        logErFile.write("Нет файлов для копирования")


import shutil, os, datetime, sys
# очистка файла log_errors.txt, log.txt
open("log_errors.txt", "w+", encoding="utf-8").seek(0)
open("log.txt", "w+", encoding="utf-8").seek(0)
logFile = open("log.txt", "a", encoding="utf-8")

srcFold = "files to copy"  # отсюда будут копироваться файлы и папки на компьютеры

# проверка на то, что есть файлы для копирования, иначе выход
if len(os.listdir(srcFold)) == 0:
    errorsCatch("", "nullList")
    logFile.write("Нет файлов для копирования")
    os.startfile("log.txt")
    sys.exit()  # выход

dstPCs = getPCs()
count = 0
for pc in dstPCs:
    makeList(srcFold, "\\\\" + pc + "\\" + "C$\\Статистика v3.2\\ФОРМЫ" + "\\")
    logFile.write('копирование на компьютер "' + pc + '" завершено в ' + str(datetime.datetime.now().strftime("%H:%M")) + "\n")
    count += 1

logFile.write('\n')
logFile.write('число успешных операций копирования: ' + str(count))

os.startfile("log.txt")
logFile.close()
