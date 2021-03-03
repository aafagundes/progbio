import sys
import pandas as pd
import xlrd
import openpyxl
import numpy as np



#1 - O programa deve ler a partir da linha de comando a planilha com os valores de CT para cada RNA de interesse
# em diferentes condições e os coeficiente m (slope) e o coeficiente b (intercept-y) da equação da curva padrão
# já calculada previamente,suponha que seu código chama “calculaQuantAbsoluta.py”.


nomeprograma = sys.argv[0]         #python
arquivo = sys.argv[1]              #calculaQuantAbsoluta.py
coefm = sys.argv[2]                #coeficiente_m
coefb= sys.argv[3]                 #coeficient_b

coeficiente_m= -3.397186047
coeficient_b= 58.53223295


#2 - Crie um dataframe nomeado como “df” para a tabela Excel passada como parâmetro;
                    #arquivo
with pd.ExcelFile(arquivo) as xlsx:
    df = pd.read_excel(xlsx)
#print(df)
#imprimindo so a coluna desejada
#print(df[['CT']])

#3 - Crie um novo dataframe nomeado como “df_q” que contém as colunas “Sample_Name”, “Target_Name”,
# “Stage” “CT” e “Quantity”, onde Quantity é calculado para cada RNA de interesse usando a Equação 2.
QT = 10**((df['CT']-58.53223295)/-3.397186047)          # Q=10((CT-b)/m)
                    #coefb             #coefm
#QT = 10**((df['CT']-'coeficiente_m')/'coeficient_b')

df['Quantity']=QT
dataNormalizado={'Sample_Name':df['Sample_Name'],'Target_Name':df['Target_Name'],'Stage':df['Stage'],'CT':df['CT'],
                 'Quantity':df['Quantity']}
df_q=pd.DataFrame(dataNormalizado,columns=['Sample_Name','Target_Name','Stage','CT','Quantity'])
#print(df_q)


#4 -   Salve df_q como uma nova planilha do Excel.
df_q.to_excel("df_q.xlsx")

#5 - Imprima na tela o df_q.
with pd.ExcelFile("df_q.xlsx") as xlsx:
    dfq = pd.read_excel(xlsx)
print(dfq)

#6- Imprima o nome da amostra (“Sample_Name”), condição (“Stage”) seu valor de CT (“CT”)
#e sua abundância (“Quantity”) que apresentou maior abundância (“Quantity”).

#print("maior numero de quantity = %f" %dfq['Quantity'].max())   # maior num da coluna

maior= dfq['Quantity'].max()

#retirar o Target_Name
dfq = dfq.drop(columns=['Target_Name'])
print('A linha com mais abundancia é:')
print(dfq[dfq['Quantity']==maior])


xlsx.close()
