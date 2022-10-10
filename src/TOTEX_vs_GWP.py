import output
import matplotlib.pyplot as plt


FolderName_l = ["Run0", "Run1", "Run2"]

Data_l  = []
TOTEX_l = []
GWP_l   = []

for fileName in FolderName_l :
    Data_l.append(output.outData("./data/"+fileName))


for run in Data_l :
    TOTEX_l.append(run.TOTEX.getValue())
    GWP_l.append(run.GWP_total.getValue())

plt.plot(TOTEX_l, GWP_l)
plt.show()


