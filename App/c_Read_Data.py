import csv

def Read_CSV(Path):
  with open(Path, 'r') as CSV_File:
    Reader = csv.reader(CSV_File, delimiter=',') # Delimiter - It separates the data in the csv file
# the Reader is an ITERABLE
    Header = next(Reader) # It reads the first row of the csv file - The Titles - THE KEYS
    Data = [] # To create a List with all the dictionaries
    for Row in Reader:
      Iterable = zip(Header, Row) # It creates a tuple of the Header and the Row
      Country_Dict = {Key: Value for Key, Value in Iterable}
      Data.append(Country_Dict) # It adds the dictionary to the list
    return Data
  
if __name__ == '__main__':
  Data = Read_CSV('./11_App_Module/Data.csv')
  print(Data[0])

'''
# PLAYGROUND - Tu reto es implementar la función read_csv que lee el archivo CSV y calcula el total de gastos de la empresa.
import csv
def read_csv(path):
   # Tu código aquí 👇
   with open(path, 'r') as csvfile:
      total = sum(int(r[1]) for r in csv.reader(csvfile))
   return total
response = read_csv('./data.csv')
print(response)
'''