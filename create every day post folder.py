import os, datetime, time
from pathlib import Path


def getCurDate():
    if len(str(datetime.datetime.now().day)) == 1:
        curDay = '0' + str(datetime.datetime.now().day)
    else:
        curDay = datetime.datetime.now().day

    if len(str(datetime.datetime.now().month)) == 1:
        curMon = '0' + str(datetime.datetime.now().month)
    else:
        curMon = datetime.datetime.now().month
    curYear = datetime.datetime.now().year

    if datetime.datetime.now().weekday() < 5:
        if len(str(curMon)) == 1:
            return str(curDay) + '.0' + str(curMon) + '.' + str(curYear)[2:]
        else:
            return str(curDay) + '.' + str(curMon) + '.' + str(curYear)[2:]


def getPath():
    path = 'Y:\\17. Управление правовой статистики\\!!!ЭЛЕКТРОННАЯ ПОЧТА\\2020\\'
    return path


def getMonth():
    months = {1: "1.январь", 2: "2.февраль", 3: "3.март",
              4: "4.апрель", 5: "5.май", 6: "6.июнь",
              7: "7.июль", 8: "8.август", 9: "9.сентябрь",
              10: "10.октябрь", 11: "11.ноябрь", 12: "12.декабрь"}
    return months[datetime.datetime.now().month]


def log(dateCh, pathCh):
    fileCheck = open("C:\\Users\\user\\Desktop\\Работа\\2020\\Python\\for Excel\\checkPostFolder.txt", 'w', encoding='utf8')
    print(dateCh, file=fileCheck)
    print()
    if Path.exists(pathCh):
        print("Path was created!", file=fileCheck)
        print("Path: ", pathCh, file=fileCheck)
        print("Date: ", dateCh, file=fileCheck)
    else:
        print("path wasn't created! ", file=fileCheck)
    print()


def all():
    host = "10.47.5.13"
    response = os.system("ping " + host + " -n 1") #ping 1-м пакетом
    if response == 0:
        path = Path(getPath() + getMonth() + "\\")
        if not Path.exists(path):
            Path.mkdir(path)

        finalPath = Path(getPath() + "\\" + getMonth() + "\\" + getCurDate())
        print(finalPath)
        if not Path.exists(finalPath):
            Path.mkdir(finalPath)
            time.sleep(10)
            all()
        else:
           # testFolderPath = Path(getPath() + "\\" + getMonth() + "\\" + getCurDate() + "\\test")
           # Path.mkdir(testFolderPath)
            return
    else:
        time.sleep(20)
        all()


all()
log(getCurDate(), Path(getPath() + "\\" + getMonth() + "\\" + getCurDate()))
