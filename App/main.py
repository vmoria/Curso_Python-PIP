import c_Read_Data
import d_Charts
import e_Chart_Data


def run():
  Data = c_Read_Data.Read_CSV('Data.csv')
  
  Country = input('Type Country => ')
  
  Result = e_Chart_Data.Population_by_Country(Data, Country)

  if len(Result) > 0:
    Country = Result[0]
    Labels, Values = e_Chart_Data.Get_Population(Country)
    d_Charts.Generate_Bar_Chart(Labels, Values)
  
  Data = list(filter(lambda item: item['Continent'] == 'South America', Data)) # Filter the List Data, and return a List with the country that matches the Country parameter
  Countries = list(map(lambda X: X['Country/Territory'], Data))
  Percentages = list(map(lambda X: X['World Population Percentage'], Data))
  d_Charts.Generate_Pie_Chart(Countries, Percentages)

if __name__ == '__main__': # If the file is executed as a script, it will run the run() function 
  run()