import os, datetime


def call_msra():
    terr = input('код территории: ')
    if terr == "":
        print()
        call_msra()
    comp = input('номер АРМа: ')
    if comp == "":
        print()
        call_msra()
    else:
        os.system(r'C:\Windows\System32\msra.exe /offerra kmr-' + terr + '-' + comp)
        try:
            logging(1)
        except BaseException:
            print("Ошибка при запоси в log.txt")

    print()
    call_msra()


# чтение файла log.exe и запись в него счетчика открытых АРМов
# cnt - количество добавленных в лог элементов
def logging(cnt):
    today = str(datetime.date.today())
    # проверка, что файл существует. Если нет - то создается
    try:
        outputFile = open("log.txt", "r")
    except FileNotFoundError:
        outputFile = open("log.txt", "w+")
        print("", file=outputFile)

    # запись строк файла в lines
    lines = []
    for line in outputFile:
        if line.rstrip() != "":
            lines.append(line.rstrip())
    outputFile.close()

    # проверка, что файл не пустой, и что присутствует шапка
    if len(lines) == 0:
        lines.insert(0, "Date          Count")
        lastLine = lines[-1]
    elif lines[0] != "Date          Count":
        lines.insert(0, "Date          Count")
        lastLine = lines[-1]
    else:
        lastLine = lines[-1]

    # проверка, есть ли текущая дата в файле
    # если нет, то добавляем ее со счетчиком 1
    # если есть, то считвываем и увеличиваем значение счетчика
    if lastLine.split()[0] != today:
        lines.append(today + "    1")

        f = open("log.txt", "w")
        for line in lines:
            if line != "":
                print(line, file=f)
        f.close()
    else:
        # проверка, что в счетчике на сегодня число
        try:
            oldCount = int(lastLine.split()[1])
        except ValueError:
            oldCount = 0
            print("\n Счетчик за сегодня сброшен из-за нечислового значения!\n")
        lines[-1] = today + "    " + str(oldCount + cnt)

        f = open("log.txt", "w")
        for line in lines:
            if line != "":
                print(line, file=f)
        f.close()


print('Данная программа открывает msra c параметром /offerra kmr-????-???')
call_msra()
