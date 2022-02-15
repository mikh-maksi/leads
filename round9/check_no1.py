handle = open("C:/work/leads/round9/in_zohot.csv", "r") #Основной файл
bot_file = open("C:/work/leads/round9/csv/bot.csv", "r") #бот

f = open("result.csv", "w")
f.write(line)
reftel =[]
tels =[]

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

    #print(res)
    try:
        if res[l-1]=='\n':
            res=res[:l-1]
    except IndexError:
        print("--!--")
        res=res
    #if res[0:1] != 0:
    #    res = "0"+res
    return res

bot_numbers =[]
#Формируем массив событий, в которых можно было участвовать
for line in bot_file:
    elements = line.split(';')
    try:
        tel = elements[3]
    except IndexError:
        print("--!+!--")
        tel = ""
    if tel !='':
        telel = clear_phone(tel)
        bot_numbers.append(telel)

#print(bot_numbers)

zoho_numbers =[]
#Формируем массив событий, в которых можно было участвовать
for line in handle:
    elements = line.split(';')
    try:
        tel = elements[3]
    except IndexError:
        print("--!+!--")
        tel = ""
    if tel !='':
        telel = clear_phone(tel)
        zoho_numbers.append(telel)

#print(zoho_numbers)

arr = []
count = 0
for tel in zoho_numbers:
    telel = clear_phone(tel)
    arr.append(telel)
    for tel_bot in bot_numbers:
        if (telel in tel_bot) and telel!='' and not(nocopy(arr,telel)>1):
            resline = f"{elements[0]};tel:{telel};\n"
            print(resline)
            f.write(resline)
            count+=1
print(count)
