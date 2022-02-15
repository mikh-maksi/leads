def clear_phone(tel):
    code = tel[0:2]
    telef = tel[2::]
    res = ''
    if code == "38":
        res = telef
    else:
        res = code+telef
    return res

handle = open("parent.csv", "r") #Основной файл
referal_file = open("referal.csv", "r")
f = open("result.csv", "w")
reftel =[]
for line in referal_file:
    #print(line)
    elements = line.split(';')
    tel = elements[1]
    print(clear_phone(tel))
    telel = clear_phone(tel)
    reftel.append(telel)
    #f.write(line)

head = f"Имя;Телефон;Участвовал ли от него в марафоне\n"
f.write(head)
arr =[]
for line in handle:
    #print(line)
    elements = line.split(';')
    tel = elements[1]
    #print(clear_phone(tel))
    telel = clear_phone(tel)
    print(reftel.count(telel))
    arr.append(telel)
    resline = f"{elements[0]};tel:{telel};{reftel.count(telel)}\n"
    f.write(resline)

handle.close()
