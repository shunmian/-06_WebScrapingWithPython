from urllib.request import urlopen
import csv
from io import StringIO

csvFileHandler = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv")

csvString = csvFileHandler.read().decode("ascii",'ignore')

#创建StringIO实例(内存中读写字符串),该实例和fileHandler类似,因此可以在使用fileHandler的地方使用StringIO实例。
memory = StringIO(csvString)
csvReader = csv.DictReader(memory)
for row in csvReader:
    print(row)

# Output:
# {'Name': "Monty Python's Flying Circus", 'Year': '1970'}
# {'Name': 'Another Monty Python Record', 'Year': '1971'}
# {'Name': "Monty Python's Previous Record", 'Year': '1972'}

