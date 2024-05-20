import matplotlib.pyplot as plt

def Generate_Pie_Chart():
    Labels = ['A', 'B', 'C']
    Values = [200, 34, 120]

    fig, ax = plt.subplots()
    ax.pie(Values, labels=Labels)
    # plt.savefig('pie.png')
    plt.show()
    plt.close()