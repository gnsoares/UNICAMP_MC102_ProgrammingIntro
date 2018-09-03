#!/usr/bin/env python3

ALTURA_TABULEIRO = 10
LARGURA_TABULEIRO = 10

# Funcao: atualiza_posicao
#
# Parametros:
#      l: largura do bloco que ira cair
#      a: altura do bloco que ira cair
#      x: posicao horizontal inicial do bloco que ira cair
#   desl: deslocamento horizontal a ser aplicado ao bloco (positivo para direita, negativo para a esquerda) 
#    rot: 1 se deve rotacionar o bloco, 0 caso contrario 
#
# Retorno:
#   Nova largura, altura e posicao horizontal.
#
def atualiza_posicao(l, a, x, desl, rot):
	# Rotação é checada primeiro. Caso for rotacionado, largura e altura trocam seus valores
	if rot == 1:
		l = l + a
		a = l - a
		l = l - a

	# No deslocamento, a peça não pode sair do tabuleiro
	if x + desl <= LARGURA_TABULEIRO - l and x + desl >= 0:
		 x = x + desl
	elif x + desl > LARGURA_TABULEIRO - l:
		x = LARGURA_TABULEIRO - l
	elif x + desl < 0:
		x = 0
	return l, a, x 

# Funcao: encontra_y
#
# Parametros:
#    mat: matriz representando o tabuleiro 
#      l: largura do bloco que ira cair
#      x: posicao horizontal do bloco que ira cair
#
# Retorno:
#   altura final y do canto inferior esquerdo do bloco apos
#   este descer o maximo possivel
#
def encontra_y(mat, l, x):

	# y recebe 10 caso a peça não consiga se encaixar. Com isso, não será gerada uma matriz válida
	y = 10

	# Encontra y
	for i in range(ALTURA_TABULEIRO-1,-1,-1):
		if max(mat[i]) == 0:
			y = i
		else:
			yVale = True
			for j in range(x,x+l):
				if mat[i][j] == 1:
					yVale = False
			if yVale:
				y = i
			else:
				break
	return y

# Funcoes: posicao_final_valida
#
# Parametros:
#      a: altura do bloco que caiu
#      y: altura final do bloco que caiu
#
# Retorno:
#   1 se o bloco naquela posicao estiver contido dentro do tabuleiro, ou 0 caso contrario.
#
def posicao_final_valida(a, y):

	if y + a > ALTURA_TABULEIRO:
		return False
	else:
		return True

# Funcoes: posiciona_bloco
#
# Parametros:
#    mat: matriz do tabuleiro 
#      l: largura do novo bloco
#      a: altura do novo bloco
#      x: posicao horizontal do novo bloco
#      y: altura final do novo bloco
#
#      Deve preencher com 1s as novas posições ocupadas pelo bloco que caiu
# Retorno:
#   NULL
#
def posiciona_bloco(mat, l, a, x, y):

	for i in range(y, y+a):
		for j in range(x, x+l):
			mat[i][j] = 1
	return None

# Funcoes: atualiza_matriz
# 
#    mat: matriz do tabuleiro 
#
#         Deve remover as linhas totalmente preenchidas do tabuleiro copiando
#         linhas posicionadas acima.
# Retorno:
#   retorna o numero de linhas totalmente preenchidas que foram removidas apos
#   a atualizacao do tabuleiro.
#
def atualiza_matriz(mat):

	# Quantidade de pontos caso nenhuma linha seja eliminada
	p = 0

	# Enquanto houver linhas apenas de 1s elas serão removidas
	while mat.count([1]*LARGURA_TABULEIRO) != 0:
		for i in range(ALTURA_TABULEIRO):
			if min(mat[i]) == 1:
				for j in range(ALTURA_TABULEIRO):
					for k in range(LARGURA_TABULEIRO):
						if i + j + 1 < ALTURA_TABULEIRO:
							mat[i+j][k] = mat[i+j+1][k]		

				# A última linha recebe 0s para que o valor dela não seja copiado diversas vezes
				mat[ALTURA_TABULEIRO-1] = [0]*LARGURA_TABULEIRO
				
				# Para cada remoção de linha, 1 ponto adicionado
				p += 1
	return p
