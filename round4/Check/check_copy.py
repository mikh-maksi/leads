# Списокм просматриваем все файлы. В Файлах в 4 столбце телефоны. А дальше - специальные условия для каждого списка
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







f = open("result.csv", "r")
res = open("nocopy.csv","w")
reftel =[]
tels =[]

#Формируем массив событий, в которых можно было участвовать

for line in f:
    #print(line)
    elements = line.split(';')
    try:
        tel = elements[1]
    except IndexError:
        print("--!+!--")
        tel = ""
    #print(clear_phone(tel))
    telel = clear_phone(tel)
    #print(telel)
    reftel.append(telel)
   # eventTel = open(f"}_tel.csv", "w")
   # eventTel.write(f"{telel}\n")
print(reftel)
print(len(reftel))

for t1 in reftel:
    n=0
    for t2 in reftel:
        if t1 == t2:
            n +=1
    print(n)

