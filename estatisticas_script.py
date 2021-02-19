# Módulo Python denominado “estatisticas_script.py”

def maximo(lista):
    valores = [float(str(val.strip()).replace(",",".")) for val in lista]
    OrdemDecrescente = sorted(valores, reverse=True)
    return OrdemDecrescente[0]


def minimo(lista):
    valores = [float(str(val.strip()).replace(",",".")) for val in lista]
    OrdemCrescente = sorted(valores)
    return OrdemCrescente[0]


def media(lista):
    SomaValores = 0
    valores = [float(str(val.strip()).replace(",",".")) for val in lista]
    for numero in valores:
        SomaValores+=numero
    med=SomaValores/len(valores)
    return med

def raz(nome, val1, val2):
    for i in range(len(val1)):
        if float(str(val2[i].strip()).replace(",", ".")) > 0:
            print(nome[i].strip(), ' ', float(str(val1[i].strip()).replace(",", ".")) / float(str(val2[i].strip()).replace(",", ".")))
        else:
            print('Erro: Divisao por 0 encontrada')
