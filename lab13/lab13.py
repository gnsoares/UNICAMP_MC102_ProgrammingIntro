#!/usr/bin/env python3

#*******************************************************************************
# Funcao: atualizaTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato
#   jogo: string contendo as informações de um jogo no formato especificado no lab.
#
# Descrição:
#   Deve inserir as informações do parametro 'jogo' na tabela.
#   OBSERVAÇÃO: nesse momento não é necessário ordenar a tabela, apenas inserir as informações.
def atualizaTabela(tabela, jogo):
	
	#Divisao dos dados da partida em lista
	jogo_list = jogo.split()

	# Conversao dos numeros de gols em inteiros
	jogo_list[1] = int(jogo_list[1])
	jogo_list[-2] = int(jogo_list[-2])
	
	# Atribuicao da posicao na tabela dos jogadores envolvidos
	for i in range(len(tabela)):
		if tabela[i][0] == jogo_list[0]:
			t1 = i
		elif tabela[i][0] == jogo_list[-1]:
			t2 = i

	# Atribuicao dos pontos e numeros de vitorias
	if jogo_list[1] > jogo_list[-2]:
		tabela[t1][2] += 1
		tabela[t1][1] += 3
	elif jogo_list[-2] > jogo_list[1]:
		tabela[t2][2] += 1
		tabela[t2][1] += 3
	else:
		tabela[t1][1] += 1
		tabela[t2][1] += 1

	# Atribuicao dos gols pro e saldo de gols
	tabela[t1][4] += jogo_list[1]
	tabela[t1][3] += jogo_list[1]
	tabela[t1][3] -= jogo_list[-2]
	tabela[t2][4] += jogo_list[-2]
	tabela[t2][3] += jogo_list[-2]
	tabela[t2][3] -= jogo_list[1]

	return None

#*******************************************************************************

#*******************************************************************************
# Funcao: comparaTimes
#
# Parametros:
#   time1: informações de um time
#   time2: informações de um time
#
# Descricão:
#   retorna 1, se o time1>time2, retorna -1, se time1<time2, e retorna 0, se time1=time2
#   Observe que time1>time2=true significa que o time1 deve estar em uma posição melhor do que o time2 na tabela.
def comparaTimes(time1, time2):

	# Comparacao de pontos
	if time1[1] > time2[1]:
		return 1
	elif time2[1] > time1[1]:
		return -1
	else:
		# Comparacao de numero de vitorias
		if time1[2] > time2[2]:
			return 1
		elif time2[2] > time1[2]:
			return -1
		else:
			# Comparacao de saldo de gols
			if time1[3] > time2[3]:
				return 1
			elif time2[3] > time1[3]:
				return -1
			else:
				# Comparacao de gols pro
				if time1[4] > time2[4]:
					return 1
				elif time2[4] > time1[4]:
					return -1
				else:
					return 0

#*******************************************************************************


#*******************************************************************************
# Funcao: ordenaTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato.
#
# Descricão:
#   Deve ordenar a tabela com campeonato de acordo com as especificaçoes do lab.
#
def ordenaTabela(tabela):

	# Ordenacao
	for i in range(len(tabela)):
		for j in range(len(tabela)-1):
			if comparaTimes(tabela[j], tabela[j+1]) == -1:
				aux = tabela[j]
				tabela[j] = tabela[j+1]
				tabela[j+1] = aux
	
	return None
#*******************************************************************************


#*******************************************************************************
# Funcao: imprimeTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato.
#
# Descrição:
#   Deve imprimir a tabela do campeonato de acordo com as especificações do lab.
def imprimeTabela(tabela):

	# Impressao
	for i in range(len(tabela)):
		print(tabela[i][0] + ", %d, %d, %d, %d" %(tabela[i][1],tabela[i][2],tabela[i][3],tabela[i][4]))

	return None
#*******************************************************************************
