def Get_Population():
  Keys = ['col', 'bol']
  Values = [300, 400]
  return Keys, Values

A = 'Hola' # Global Variable Declaration

def Population_by_Country(Data, Country): # Data is a general PARAMETER that I recieve (It `s a List with all countries) and Country is a specific PARAMETER for instance 'col'
  Result = list(filter(lambda item: item['Country'] == Country, Data)) # Filter the List Data, and return a List with the country that matches the Country parameter
  return Result