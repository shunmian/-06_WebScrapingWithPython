import os
import csv

def getCSVPath(directory,filename):
    if not os.path.exists(directory):
        os.makedirs(directory)
    return os.getcwd()+"/"+directory+"/" + filename

path = getCSVPath("CSV","test.cv")
try:
    csvFile = open(path,'w+')
    writer=csv.writer(csvFile)
    writer.writerow(('number', 'number puls 2', 'number times 2'))
    for i in range(10):
        writer.writerow((i,i+2,i*2))
finally:
    csvFile.close()

#Output:
# number,number puls 2,number times 2
# 0,2,0
# 1,3,2
# 2,4,4
# 3,5,6
# 4,6,8
# 5,7,10
# 6,8,12
# 7,9,14
# 8,10,16
# 9,11,18
