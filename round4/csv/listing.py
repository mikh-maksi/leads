import os
directory = 'C:/work/leads/round4/csv/csv'
files = os.listdir(directory)
print(files)

filenames = []
filenames.append("web0509")
filenames.append("web0809")
filenames.append("web1109")
filenames.append("web2009")
filenames.append("Minecraft_probe")
filenames.append("GameDev_probe")
filenames.append("Python_probe")
filenames.append("finweb22")
filenames.append("finweb33")
filenames.append("gd2908")

print(filenames)
s = ''
for flnm in filenames:
    s = s +";" +flnm

print(s)