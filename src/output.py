class outData :
    def __init__(self, pathToCsvFolder) :
        self.extractPerformanceData(pathToCsvFolder)

    def extractPerformanceData(self, pathToCsvFolder) :
        csv_performance_f = open(pathToCsvFolder + "/performance.csv")
        unit = csv_performance_f.readline().split("\t")[1][7:-2]

        self.CAPEX              = Data(float(csv_performance_f.readline().split("\t")[1][:-1]), unit)
        self.OPEX               = Data(float(csv_performance_f.readline().split("\t")[1][:-1]), unit)
        self.TOTEX              = Data(float(csv_performance_f.readline().split("\t")[1][:-1]), unit)
        csv_performance_f.readline()
        csv_performance_f.readline()
        self.GWP_construction   = Data(float(csv_performance_f.readline().split("\t")[1][:-1]), unit)     
        self.GWP_op             = Data(float(csv_performance_f.readline().split("\t")[1][:-1]), unit)
        self.GWP_total          = Data(float(csv_performance_f.readline().split("\t")[1][:-1]), unit)

        csv_performance_f.close()
    

    

class Data :
    def __init__(self, value = -1, unit = -1) :
        self.__value  = value
        self.__unit   = unit

    def getValue(self) :
        return(self.__value)

    def getUnit(self) :
        return(self.__unit)
    

