for line in handle:
    #print(line)
    elements = line.split(';')
    tel = elements[10]
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

    resline = f"{elements[0]};tel:{telel};{tels_string}\n"
    f.write(resline)