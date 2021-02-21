#Nome:Andressa Andrade Fagundes
#Data:21/02/2021
#Versao:1

import sys
import pandas as pd
import estatisticas_pandas_script as est

nomeprograma = sys.argv[0]
arquivo = sys.argv[1]

with pd.ExcelFile(arquivo) as xlsx:
    df=pd.read_excel(xlsx)

menor=str(input('Digite o nome da coluna que você deseja calcular o valor mínimo:'))
print('Minimo %s: %.2f' %(menor, est.minimo(df,menor)))

mediaa=str(input('Digite o número da coluna que você deseja calcular a média:'))
print('Media %s: %.2f' %(mediaa, est.media(df,mediaa)))

maior=str(input('Digite o nome da coluna que você deseja calcular o valor máximo: '))
print('Maximo %s: %.2f' %(maior, est.maximo(df,maior)))

somatotall=str(input('Digite o nome da coluna que voce deseja a soma total dos valores desta:'))
print('Soma total da coluna %s: %.2f' %(somatotall, est.somatotal(df,somatotall)))

x=int(input('Digite a quantidade de países com maior número de casos que você deseja visualizar:'))
print(f"{x} países em ordem decrescente de casos:" )
print(est.topx(df,x))

#normalizacao por 100mil habitantes
print('adicionando quantidade de casos por 100.000 habitantes:')
FN= df['Total_cases']*100000/df['Population']
FN=est.normalizado(df,'Total_cases','Population')
df['Total_cases_per_100mil']= FN
print(df)

xlsx.close()
