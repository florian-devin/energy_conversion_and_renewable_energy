import output
import matplotlib.pyplot as plt
import os
 

def getFoldersName(path) :
    return os.listdir(path)


FolderName_l = getFoldersName("I:\\Telechargements\\20_10\\")

Data_l  = []
TOTEX_l = []
GWP_l   = []

for fileName in FolderName_l :
    Data_l.append(output.outData("I:\\Telechargements\\20_10\\"+fileName))


for run in Data_l :
    TOTEX_l.append(run.TOTEX.getValue())
    GWP_l.append(run.GWP_total.getValue())

plt_with_nuc = plt.plot(TOTEX_l, GWP_l, "y*")
FolderName_l = getFoldersName("I:\\Telechargements\\20_10_without_nuclear\\")

Data_l  = []
TOTEX_l = []
GWP_l   = []

for fileName in FolderName_l :
    Data_l.append(output.outData("I:\\Telechargements\\20_10_without_nuclear\\"+fileName))

print(GWP_l)

for run in Data_l :
    TOTEX_l.append(run.TOTEX.getValue())
    GWP_l.append(run.GWP_total.getValue())
plt_without_nuc = plt.plot(TOTEX_l, GWP_l, "b*")
plt.xlabel("TOTEX")
plt.ylabel("GWP")
plt.legend(['With nuclear', 'Without nuclear'])
plt.show()
