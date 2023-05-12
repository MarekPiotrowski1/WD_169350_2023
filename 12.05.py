import pandas as pd
df=pd.read_excel('imiona.xlsx')

#df_od_k=df[df['Imie'].str[0]=='K']
#uni=df_od_k['Imie'].unique()
#print(len(uni))

result = df.groupby(['Imie','Plec'])['Liczba'].sum().reset_index()
k=result[result['Plec']=='K'].reset_index()
maxindex=k['Liczba'].idxmax()
k_imie=k.iloc[maxindex]['Imie']
print(k_imie)
resuls = df.groupby(['Imie','Plec'])['Liczba'].sum().reset_index()
m=result[result['Plec']=='M'].reset_index()
maxindexm=m['Liczba'].idxmax()
M_imie=m.iloc[maxindexm]['Imie']
print(M_imie)


#zad3
data=df[(df['Rok']>=2010)& (df['Rok']<=2015)]
grupa=data.groupby('Plec')['Liczba'].sum()
grupa.plot.bar()
plt.show()
