def clear_phone(tel):
    code = tel[0:2]
    telef = tel[2::]
    res = ''
    if code == "38":
        res = telef
    else:
        res = code+telef
    return res

webinars = open("all.csv", "r") #from webinars
all = open("total.csv", "r") #all

f = open("result.csv", "w")
reftel =[]
for line in webinars:
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
