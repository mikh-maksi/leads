# Списком просматриваем все файлы. В Файлах в 4 столбце телефоны. А дальше - специальные условия для каждого списка
# Экспортим в отдельные файлы
# Основным файлом, с которым просматриваем все остальные является файл reg.csv
# Директорию прописываем в directory = 'C:/work/leads/round8/csv'
# В файле in_zoho - лежат лиды из ЗОХО, в файле in_bot - лежат лиды в боте. Нужно вывести тех, кто есть в ЗОХО, но нет в боте.
# 1 - выводим всех из бота. 2 - выводим всех из ЗОХО. 


handle = open("C:/work/leads/round9/in_zohot.csv", "r") #Основной файл
bot_file = open("C:/work/leads/round9/csv/bot.csv", "r") #бот

f = open("C:/work/leads/round9/result.csv", "w")

reftel =[]
tels =[]

#Формируем массив событий, в которых можно было участвовать
for line in bot_file:
    print(line)
    
'''
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
print(reftel)
filesListHead = ''
for flnm in filenames:
    filesListHead = filesListHead +";" +flnm

head = f"Имя;Телефон{filesListHead}\n"
f.write(head)
arr =[]

'''





# просматриваем основной файл и проверяем его на соответствие массивам
print()
'''

for line in handle:
    print(line)
    elements = line.split(';')
    print(elements)
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

    #if nocopy(arr,telel)==1:
    resline = f"{elements[0]};tel:{telel};{tels_string}\n"
    print(resline)
    f.write(resline)


'''
handle.close()
