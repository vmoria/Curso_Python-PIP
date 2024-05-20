import matplotlib.pyplot as PLT # Import the matplotlib module in PACKAGES

def Generate_Bar_Chart(Labels, Values):
  Fig, Ax = PLT.subplots()
  Ax.bar(Labels, Values)
  PLT.show() # With CTRL C it stops the show order
  # PLT.savefig('Bar.png')
  PLT.close()

def Generate_Pie_Chart(Labels, Values):
  Fig, Ax = PLT.subplots()
  Ax.pie(Values, labels=Labels)
  Ax.axis('equal')
  PLT.show()
  # PLT.savefig('Pie.png')
  PLT.close()

if __name__ == '__main__':
  # Labels = ['a', 'b', 'c']
  # Values = [100, 200, 80]
  Generate_Bar_Chart(Labels, Values)
  # # Generate_Pie_Chart(Labels, Values)