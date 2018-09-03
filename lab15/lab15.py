#!/usr/bin/env python3

# Funcao: pertence
#
# Parametros:
#   conj: vetor contendo o conjunto de entrada
#    num: elemento a ser verificado pertinencia
#
# Retorno:
#   True se num pertence a conj e False caso contrario
#
def pertence(conj, num):
    # Usa o operador in para verificar a pertinencia
    return num in conj

# Funcao: contido
#
# Parametros:
#   conj1: vetor contendo um conjunto de entrada
#   conj2: vetor contendo um conjunto de entrada
#
# Retorno:
#   True se conj1 esta contido em conj2 e False caso contrario
#
def contido(conj1, conj2):
    # Se qualquer um dos elementos do conj1 nao estiver em conj2, nao esta contido
    # Se todos estiverem, esta contido
    for i in conj1:
        if not(i in conj2):
            return False
    return True

# Funcoes: adicao e subtracao
#
# Parametros:
#   conj: vetor contendo o conjunto que tera incluso ou removido o elemento
#    num: elemento a ser adicionado ou removido
#
def adicao(conj, num):
    # Se o elemento nao pertencer ao conjunto, ele e adicionado
    if not(num in conj):
        conj.append(num)
    return None

def subtracao(conj, num):
    # Se o elemento pertencer ao conjunto, ele e removido
    if num in conj:    
        conj.remove(num)
    return None

# Funcoes: uniao, intersecao e diferenca
#
# Parametros:
#     conj1: vetor contendo o conjunto de entrada do primeiro operando
#     conj2: vetor contendo o conjunto de entrada do segundo operando
#
# Retorno:
#   Vetor contendo o conjunto de saida/resultado da operacao
#
def uniao(conj1, conj2):
    # Todos os elementos do conj1 sao adicionados
    # Todos os elementos do conj2 que ainda nao presentes sao adicionados
    uni_conj = []
    for i in conj1:
        uni_conj.append(i) 
    for i in conj2:
        if not(i in uni_conj):
            uni_conj.append(i)
    return [j for j in uni_conj]

def intersecao(conj1, conj2):
    # Todos os elementos de cada conjunto sao adicionados
    # Os elementos que so aparecem uma vez estao em apenas em um conjunto
    # Os elementos que aparecem duas vezes (o maximo) estao nos dois
    # Cada valor distinto e removido uma vez sobrando apenas os da intersecao
    int_conj = []
    for i in conj1:
        int_conj.append(i)
    for i in conj2:
        int_conj.append(i)        
    for i in uniao(conj1, conj2):
        int_conj.remove(i)
    return [j for j in int_conj]

def diferenca(conj1, conj2):
    # Da uniao dos dois conjuntos, sao removidos todos os elementos presentes no conj2
    # Dessa maneira, ficam apenas os elementos que estao no conj1 e nao no conj2
    dif_conj = uniao(conj1, conj2)
    for i in conj2:
        dif_conj.remove(i)
    return [j for j in dif_conj]

def uniao_disjunta(conj1, conj2):
    # Da uniao dos dois conjuntos, sao removidos todos os elementos presentes no intersecao
    # Dessa maneira, ficam apenas os elementos que so estao em cada um dos seus conjuntos
    ud_conj = uniao(conj1, conj2)
    for i in intersecao(conj1, conj2):
        ud_conj.remove(i)
    return [j for j in ud_conj]
