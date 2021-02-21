#modulos tac3

def maximo(dataframe,coluna):
    max= dataframe[coluna].max()
    return max

def minimo(dataframe,coluna):
    min= dataframe[coluna].min()
    return min

def media(dataframe,coluna):
    med=dataframe[coluna].mean()
    return med

def somatotal(dataframe,coluna):
    soma=dataframe[coluna].sum()
    return soma

def topx(dataframe,numero):
    top=dataframe[:(numero)]
    return top

def normalizado(dataframe,tc,popul):
    novocasos=dataframe[tc]*100000/dataframe[popul]
    return novocasos
