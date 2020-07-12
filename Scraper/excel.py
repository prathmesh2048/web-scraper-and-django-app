from xlrd import open_workbook
import pandas as pd

df = pd.read_excel('details.xlsx')  # can also index sheet by name or fetch all sheets
mylist = df['business-name href'].tolist()
print(mylist)
print(len(mylist))