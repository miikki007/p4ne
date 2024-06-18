from matplotlib import pyplot
from openpyxl import load_workbook

def getvalue(x):
    return x.value

wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']

list_x = list(map(getvalue, sheet['A'][1:]))
list_y = list(map(getvalue, sheet['C'][1:]))
list_t = list(map(getvalue, sheet['D'][1:]))

pyplot.plot(list_x, list_y)
pyplot.plot(list_x, list_t)

pyplot.show()