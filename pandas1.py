import numpy as np
import pandas as pd

a = pd.read_excel('imiona.xlsx')
print(a[(a.Imie=='MAREK')])

e=a.loc[(a.Rok >= 2000) & (a.Rok <= 2005)]['Liczba'].sum()
d=a.groupby('Rok')['Liczba'].sum()
print(e)

g= a.loc[a.groupby('Plec')['Liczba'].idxmax()]['Imie']
print(g)