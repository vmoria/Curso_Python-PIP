def Get_Population(Country_Dic):
  Population_Dic = {
    '2022': int(Country_Dic['2022 Population']),
    '2020': int(Country_Dic['2020 Population']),
    '2015': int(Country_Dic['2015 Population']),
    '2010': int(Country_Dic['2010 Population']),
    '2000': int(Country_Dic['2000 Population']),
    '1990': int(Country_Dic['1990 Population']),
    '1980': int(Country_Dic['1980 Population']),
    '1970': int(Country_Dic['1970 Population'])
  }
  Labels = Population_Dic.keys()
  Values = Population_Dic.values()
  return Labels, Values

def Population_by_Country(Data, Country): # Data is a general PARAMETER that I recieve (It `s a List with all countries) and Country is a specific PARAMETER for instance 'col'
  Result = list(filter(lambda item: item['Country/Territory'] == Country, Data)) # Filter the List Data, and return a List with the country that matches the Country parameter
  return Result