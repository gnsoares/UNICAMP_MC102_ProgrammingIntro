def hit(mat, x, y):
	""" Funcao do ataque:
			Remove o navio atacado do tabuleiro.
			Usa recursao. Troca a posicao atual para agua e chama a funcao
			para as posicoes adjacentes ate encontrar uma posicao de agua 
			que para a chamada de novas funcoes.
			Retorna a matriz com o navio removido.
	"""
	if mat[x][y] == '-':
		return mat
	else:
		mat[x][y] = '-'
		mat = hit(mat, max(0,x-1),y)
		mat = hit(mat, x,max(0,y-1))
		mat = hit(mat, min(len(mat)-1,x+1),y)
		mat = hit(mat, x,min(y+1,len(mat[x])-1))
	return mat

if __name__ == "__main__":

	# Leitura das dimensoes e do tabuleiro de cada jogador
	dim = [int(i) for i in input().split('x')]
	table = [[[i for i in input()] for j in range(dim[0])] for k in range(2)]

	turn = 1	# Variavel que guarda o turno
	while True:
		# Obtencao das coordenadas do ataque
		x, y = tuple(int(i) for i in input().split(','))
		x -= 1
		y -= 1

		# Chamada da funcao do ataque
		if table[turn%2][x][y] == '@':
			table[turn%2] = hit(table[turn%2],x,y)

		# Atribuicao da variavel a ser usada na impressao
		if turn%2 == 1:
			player = 1
		else:
			player = 2

		# Impressao da jogada
		print("Ataque em ({},{}) do jogador {}\n{}".format(x+1,y+1,player,'\n'.join(''.join(['{}'.format(i) for i in row]) for row in table[turn%2])))

		# Verificacao se o jogador atacado esta sem navios
			# Caso afirmativo, o loop de jogadas e encerrado
		isTheEnd = True
		for i in range(dim[0]):
			for j in range(dim[1]):
				if table[turn%2][i][j] == '@':
					isTheEnd = False
		if isTheEnd:
			break

		# Incremento do turno
		turn += 1