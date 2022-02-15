# Списокм просматриваем все файлы. В Файлах в 4 столбце телефоны. А дальше - специальные условия для каждого списка
# Экспортим в отдельные файлы


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
    if res[0:1] != 0:
        res = "0"+res
    return res

handle = open("teen22_parents_part1.csv", "r") #Основной файл

filenames = []
filenames.append("web0509")
filenames.append("web0809")
filenames.append("web1109")
filenames.append("web2009")
filenames.append("FameDev_probe")
filenames.append("Minecraft_probe")
filenames.append("FameDev_probe")
filenames.append("Python_probe")

events = []
for fl in filenames:
    print(fl)
    event = open(f"{fl}.csv", "r")
    events.append(event)

f = open("result.csv", "w")

reftel =[]


#Формируем массив событий, в которых можно было участвовать
count = 0
for eventfl in events:

    flnm = filenames[count]+"_tel.csv"
    print(flnm)
    count +=1
    for line in eventfl:
        #print(line)
        elements = line.split(';')
        tel = elements[3]
        #print(clear_phone(tel))
        telel = clear_phone(tel)
        #print(telel)
        reftel.append(telel)
       # eventTel = open(f"}_tel.csv", "w")
       # eventTel.write(f"{telel}\n")


head = f"Имя;Телефон;Участвовал ли от него в марафоне\n"
f.write(head)
arr =[]


# просматриваем основной файл и проверяем его на соответствие массивам
for line in handle:
    #print(line)
    elements = line.split(';')
    tel = elements[1]
    #print(clear_phone(tel))
    telel = clear_phone(tel)
   # print(reftel.count(telel))
    arr.append(telel)
    resline = f"{elements[0]};tel:{telel};{reftel.count(telel)}\n"
    f.write(resline)

handle.close()
