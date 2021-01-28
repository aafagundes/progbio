#Escreva um programa em Python que lê uma sequência de DNA fornecida pelo usuário e identifica a presença de homopolímeros e a respectiva posição na sequência.
def sequencia(b):
    if b == "":
        return 'sequencia vazia'
    x = b.upper()
    for m in x:
        if str(m) != "A" and str(m) != "T" and str(m) != "C" and str(m) != "G":
            return "A sequencia inserida não é um DNA"
    c = 0
    d = 0
    u = ''
    s = ()
    j = []
    pos = 0
    lista = []
    for g in x:
        j.append(g)
    for i in j:
        c = 0
        while d < len(j):
            u = j[d]
            if u != i:
                break
            c += 1
            d+=1
        if c > 2:
            s = (str(i), int(c), int(pos)+1)
            c = 0
            lista.append(s)
        pos += 1
        if pos > len(j):
            break

    return lista

l = input('Digite uma sequencia de DNA:')

gt = sequencia(l)
print(gt)
