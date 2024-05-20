import c_Read_Data
import d_Charts
import e_Chart_Data
# import pandas as Pd

def run():
  Data = c_Read_Data.Read_CSV('Data.csv')
  # SUSPENDIDO POR EL USO DE PANBAS
  Data = list(filter(lambda item: item['Continent'] == 'South America', Data)) # Filter the List Data, and return a List with the country that matches the Country parameter
  
  Countries = list(map(lambda X: X['Country/Territory'], Data))
  Percentages = list(map(lambda X: X['World Population Percentage'], Data))
  '''
  # Df = DataFrame
  Df = Pd.read_csv('Data.csv') # With this it isn`t necessary c_Read_Data Module
  Df = Df[Df['Continent'] == 'South America'] # this is the same code as line 8
  Countries = Df['Country'].values # This is the same code as line 9
  Percentages = Df['World Population Percentage'].values # This is the same code as line 10
  '''
  d_Charts.Generate_Pie_Chart(Countries, Percentages)

  Country = input('Type Country => ')
  print(Country)

  Result = e_Chart_Data.Population_by_Country(Data, Country)

  if len(Result) > 0:
    Country = Result[0]
    Labels, Values = e_Chart_Data.Get_Population(Country)
    d_Charts.Generate_Bar_Chart(Labels, Values)

if __name__ == '__main__': # If the file is executed as a script, it will run the run() function 
  run()