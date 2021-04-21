import subprocess, sys, os, datetime


# открытие одного АРМ
def open_in_explorer():
    print()
    terr = input('код территории: ')
    if terr == 'exit':
        close()
    elif terr == 'open':
        open_from_file()
        open_in_explorer()
    elif terr == '':
        open_in_explorer()

    comp = input('номер АРМа: ')
    if comp == 'exit':
        close()
    elif comp == 'open':
        open_from_file()
    elif comp == '':
        open_in_explorer()
    else:
        if os.path.exists(r'\\kmr-' + terr + '-' + comp + r'\c$'):
            subprocess.call(['explorer.exe', r'\\kmr-' + terr + '-' + comp + r'\c$'])
            print('открыто ' + r'\\kmr-' + terr + '-' + comp + r'\c$')
            logging(1)
        else:
            print('не удалось открыть ' + r'\\kmr-' + terr + '-' + comp + r'\c$')

    open_in_explorer()


def close():
    sys.exit()


# открытие списка АРМов из файла ARMs.txt
def open_from_file():
    inpFile = open('ARMs.txt', 'r')

    # чтение из файла
    arm_names = []
    for line in inpFile:
        if line.strip():
            if line[-1] == '\n':
                arm_names.append(line[:-1])
            else:
                arm_names.append(line)

    # проверка доступности АРМов
    opened_arms = []
    not_opened_arms=[]
    for arm in arm_names:
        if os.path.exists(r'\\' + arm + r'\c$'):
            opened_arms.append(arm)
        else:
            not_opened_arms.append(arm)

    count = 0
    # открываем только те, до которых есть доступ
    for arm in opened_arms:
        subprocess.call(['explorer.exe', r'\\' + arm + r'\c$'])
        count += 1

    if count != 0:
        try:
            logging(count)
        except BaseException:
            print("Ошибка при запоси в log.txt")

    # вывод информации о том, какие открылись, а какие - нет
    print()
    print('открыты АРМы:')
    for arm in opened_arms:
        print(arm, end='\n')
    print()
    print('не удалось открыть АРМы:')
    for arm in not_opened_arms:
        print(arm, end='\n')

    print()


# чтение файла log.exe и запись в него счетчика открытых АРМов
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



print(r'Данная программа открывает путь \\kmr-????-???\c$')
print('open - для открытия АРМов из файла ARMs.txt; exit - для выхода')
open_in_explorer()
