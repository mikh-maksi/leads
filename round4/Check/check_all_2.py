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
    if res[0:1] != "0":
        res = "0"+res
    return res

handle = open("teen22_parents_part1.csv", "r") #Основной файл

filenames = []
#filenames.append("web0509")
#filenames.append("web0809")
#filenames.append("web1109")
filenames.append("web2009")
#filenames.append("FameDev_probe")
#filenames.append("Minecraft_probe")
#filenames.append("FameDev_probe")
filenames.append("Python_probe")

events = []
for fl in filenames:
    print(fl)
    event = open(f"{fl}.csv", "r")
    events.append(event)

f = open("result.csv", "w")




#Формируем массив событий, в которых можно было участвовать
count = 0
redtels=[]
for eventfl in events:
    reftel =[]
    flnm = filenames[count]+"_tel.csv"
    print(flnm)
    count +=1
    eventTel = open(f"{flnm}", "w")
    for line in eventfl:
        #print(line)
        elements = line.split(';')
        tel = elements[3]
        #print(clear_phone(tel))
        telel = clear_phone(tel)
        #print(telel)
        telel = telel[:-1]
        reftel.append(telel)
        redtels.append(reftel)
        eventTel.write(f"{telel}\n")


head = f"Имя;Телефон;Участвовал ли от него в марафоне\n"
f.write(head)
arr =[]


# просматриваем основной файл и проверяем его на соответствие массивам
for line in handle:
    #print(line)
    elements = line.split(';')
    tel = elements[5]
    #print(clear_phone(tel))
    telel = clear_phone(tel)
    telel = telel[:-1]
   # print(reftel.count(telel))
    arr.append(telel)
    #print(telel)
    resline = f"{elements[0]};{reftel.count(telel)};tel:{telel}\n;"
    f.write(resline)
print(arr)
handle.close()
