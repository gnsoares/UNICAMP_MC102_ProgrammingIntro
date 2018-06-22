#!/usr/bin/env python3

# Funcao: print_sudoku
# Essa funcao ja esta implementada no arquivo lab20_main.py
# A funcao imprime o tabuleiro atual do sudoku de forma animada, isto e,
# imprime o tabuleiro e espera 0.1s antes de fazer outra modificacao.
# Voce deve chamar essa funcao a cada modificacao na matriz resposta, assim
# voce tera uma animacao similar a apresentada no enunciado.
# Essa funcao nao tem efeito na execucao no Susy, logo nao ha necessidade de
# remover as chamadas para submissao.
from lab20_main import print_sudoku


# O aluno pode criar outras funcoes que ache necessario

# Funcao: resolve
# Resolve o Sudoku da matriz resposta.
# Retorna True se encontrar uma resposta, False caso contrario
def resolve(resposta, x = 0, y = 0):
	""" Funcao que resolve um tabuleiro de sudoku. Altera o tabuleiro dado
		enquanto e possivel resolve-lo. Caso uma solucao tentada nao seja 
		valida retorna False.
	"""

	# Condicao de parada: Caso a funcao esteja em uma linha alem da ultima
	if x == 9:
		return True

	# Se a posicao atual ja estiver resolvida, pula diretamente para a proxima
	# chamada
	if resposta[x][y] != 0:
		# Se a posicao atual for na ultima coluna, a proxima chamada e na primeira
		# coluna da proxima linha
		if y == 8: 
			if resolve(resposta, x+1, 0):
				return True
		# Caso contrario, continua na mesma linha na proxima coluna
		else:
			if resolve(resposta, x, y+1):
				return True
		return False

	# Se a posicao atual ainda nao estiver resolvida, e preciso veririficar
	# todos os digitos que podem resolver essa posicao
	for i in range(1,10):
		# Se o valor testado for valido, continua-se as chamadas
		if isValid(i, resposta, x, y):
			resposta[x][y] = i
			if y == 8: 
				if resolve(resposta, x+1, 0):
					return True
			else:
				if resolve(resposta, x, y+1):
					return True
			# Se nao forem encontradas respostas com esse valor nessa posicao,
			# a posicao e retornada para 0 e outro valor e testado
			resposta[x][y] = 0

	print_sudoku(resposta)
	# Caso nenhum valor seja valido para essa posicao o tabuleiro nao tem solucao
	return False

def isValid(num, resposta, x, y):
	""" Funcao que verifica se um determinado numero pode ser a resposta de uma
		posicao do tabuleiro. Confere se esse numero ja esta presente na linha,
		na coluna ou no quadrado interno da posicao.
		Caso nao haja impedimentos retorna True. Caso contrario retorna False.
	"""

	# Verificacao da linha e da coluna
	for k in range(9):
		if resposta[x][k] == num:
			return False
		if resposta[k][y] == num:
			return False
	
	# Verificacao do quadrado interno						
	for i in range((x//3)*3,(x//3)*3+3):
		for j in range((y//3)*3,(y//3)*3+3):
			if resposta[i][j] == num:
				return False

	return True
										
