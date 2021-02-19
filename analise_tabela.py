#autora:Andressa Andrade Fagundes
#Data:18/02/2021
#Versão:1

import sys
import estatisticas_script

nomeprograma = sys.argv[0]
arquivo = sys.argv[1]
#novas listas para usar com as funcoes
lmax=[]
lmin=[]
lmed=[]
nome = []
val1 = []
val2 = []
max= int(input('Digite o número da coluna que você deseja calcular o valor máximo:'))
min= int(input('Digite o número da coluna que você deseja calcular o valor mínimo:'))
media= int(input('Digite o número da coluna que você deseja calcular a media:'))
razao = input('Digite o número da coluna com o identificador das linhas e os números das duas colunas que você deseja calcular a razão:').split(' ')

refArquivoEntrada=open(arquivo)
x=refArquivoEntrada.readline()
if ("\t") in x:
    cabeçalho = x.split("\t")
elif (",") in x:
    cabeçalho = x.split(",")
for linha in refArquivoEntrada:
    if ("\t")in linha:
        data=linha.split("\t")
        lmax.append(data[(max)-1])  #cria nova lista com elementos da coluna solicitada
        lmin.append(data[(min)-1])
        lmed.append(data[(media)-1])
        nome.append(data[int(razao[0])-1])
        val1.append(data[int(razao[1])-1])
        val2.append(data[int(razao[2])-1])
    else:
        if (",") in linha:
            data = linha.split(",")
            lmax.append(data[(max)-1])  # cria nova lista com elementos da coluna solicitada
            lmin.append(data[(min)-1])
            lmed.append(data[(media)-1])
            nome.append(data[int(razao[0])-1])
            val1.append(data[int(razao[1])-1])
            val2.append(data[int(razao[2])-1])

print('-='*10,'RESULTADO','-='*10)
print(f'Maximo {cabeçalho[(max)-1].strip()} = {(estatisticas_script.maximo(lmax))}')
print(f'Minimo {cabeçalho[(min)-1].strip()} = {(estatisticas_script.minimo(lmin))}')
print("Media %s = %.2f" % (cabeçalho[(media)-1].strip(),(estatisticas_script.media(lmed))))
print(cabeçalho[int(razao[0])-1], '\t', cabeçalho[int(razao[1])-1], '/', cabeçalho[int(razao[2])-1])
estatisticas_script.raz(nome,val1,val2)
refArquivoEntrada.close()


