def clear_phone(tel):
    tel = tel.replace('+','')
    code = tel[0:2]
    telef = tel[2::]
    res = ''
    if code == "38":
        res = telef
    else:
        res = code+telef
    res = res.replace('-','')
    res = res.replace(' ','')
    if len(res)==9:
        res = '0'+res
    
    return res

def in_webinars(webinar_leads,tel):
    for lead in webinar_leads:
        if clear_phone(lead[3]) == tel and tel !='':
            #print(f"{tel}!!!")
            s=lead[0]+';'+lead[1]+';'+lead[2]+';'+lead[4]+';'+lead[5]+';'
            return s
    return 0

webinars = open("all.csv", "r") #from webinars
all_leads = open("total.csv", "r") #all

f = open("result.csv", "w")
webinar_tels =[]
webinar_leads = []
i = 0
for line in webinars:
    #print(line)
    line = line.replace('\n','')
    elements = line.split(';')
    #print(elements)
    if len (elements)>3:
        tel = elements[3]
        i += 1
        #print (i)
        #print(clear_phone(tel))
        telel = clear_phone(tel)
        webinar_tels.append(telel)

        webinar_leads.append(elements)
        #f.write(line)
print("---------------")
#print(webinar_leads)
print(len(webinar_leads))


for line in all_leads:
    #print(line)
    elements = line.split(';')
    tel = elements[1]
    #print(clear_phone(tel))
    telel = clear_phone(tel)
    #reftel.append(telel)
    print(in_webinars(webinar_leads,telel))

    if telel in webinar_tels and telel != '':
        flag = 1
    else:
        flag =0
    line = line.replace('\n','')

    line = f"{flag};{line};{in_webinars(webinar_leads,telel)}\n"
    f.write(line)
