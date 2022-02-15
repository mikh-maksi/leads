# Списком просматриваем все файлы. В Файлах в 4 столбце телефоны. А дальше - специальные условия для каждого списка
# Экспортим в отдельные файлы

def nocopy(arr,tel):
    n = 0
    for t1 in arr:
        if t1 == tel:
            n +=1
    return n

def clear_phone(tel):
    
    plus = tel[0:1]
    afterplus = tel[1::]
    if plus =='+':
        tel = afterplus
        #print(tel)
    
    code = tel[0:2]
    telef = tel[2::]
    res = ''
    if code == "38":
        res = telef
    else:
        res = code+telef
    l = len(res)

    print(res)
    try:
        if res[l-1]=='\n':
            res=res[:l-1]
    except IndexError:
        print("--!--")
        res=res
    #if res[0:1] != 0:
    #    res = "0"+res
    return res

handle = open("highfive.csv", "r") #Основной файл

#filenames = []
#filenames.append("web0509")
#filenames.append("web0809")
#filenames.append("web1109")
#filenames.append("web2009")
#filenames.append("Minecraft_probe")
#filenames.append("GameDev_probe")
#filenames.append("Python_probe")
#filenames.append("finweb22")
#filenames.append("finweb33")
#filenames.append("gd2908")

import os
directory = 'C:/work/leads/round6_HighFive_check/csv'
filenames = os.listdir(directory)



events = []
for fl in filenames:
    print(fl)
    event = open(f"csv/{fl}", "r")
    events.append(event)

f = open("result.csv", "w")

reftel =[]
tels =[]

#Формируем массив событий, в которых можно было участвовать
count = 0
for eventfl in events:
    reftel =[]
    flnm = filenames[count]+"_tel.csv"
    print(flnm)
    count +=1
    for line in eventfl:
        #print(line)
        elements = line.split(';')
        try:
            tel = elements[3]
        except IndexError:
            print("--!+!--")
            tel = ""

        #print(clear_phone(tel))
        telel = clear_phone(tel)
        #print(telel)
        reftel.append(telel)
       # eventTel = open(f"}_tel.csv", "w")
       # eventTel.write(f"{telel}\n")
    tels.append(reftel)

filesListHead = ''
for flnm in filenames:
    filesListHead = filesListHead +";" +flnm

head = f"Имя;Телефон{filesListHead}\n"
f.write(head)
arr =[]







# просматриваем основной файл и проверяем его на соответствие массивам
print()


for line in handle:
    #print(line)
    elements = line.split(';')
    tel = elements[3]
    #print(clear_phone(tel))
    telel = clear_phone(tel)
    #print(telel)
    #print(reftel.count(telel))
    arr.append(telel)
    tels_string =''
    
    for tel_arr in tels:
        if telel in tel_arr:
            tels_string +="1;"
        else:
            tels_string +="0;"
    if nocopy(arr,telel)==1:
        resline = f"{elements[0]};tel:{telel};{tels_string}\n"
        f.write(resline)



handle.close()
