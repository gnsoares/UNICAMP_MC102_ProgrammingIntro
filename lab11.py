# Leitura e declaração das variáveis usadas
tamanho = input()				# Tamanho da matriz
altura = int(tamanho.split()[0])
largura = int(tamanho.split()[1])
iterations = int(input())			# Quantidade de dias de simulação

linha = [input() for i in range(altura)]	# Leitura da matriz
matriz = [[int(i) for i in linha[j].split()] for j in range(len(linha))]
matrizx = [[0 for i in range(largura)] for j in range(altura)] # Matriz auxiliar

# Laço que determina a simulação
for _ in range(iterations+1):
	
	#Impressão do estado atual da população
	print("iteracao %d" %_)
	for i in range(altura):
		for j in range(largura):
			print(matriz[i][j], end='')
		print()

	for i in range(altura):
		for j in range(largura):
			matrizx[i][j] = matriz[i][j]
	
	# Determinação da situação de um indivíduo baseado nos seus vizinhos
	vizinhos = []
	for i in range(altura):
		for j in range(largura):
			if i == 0 and j == 0:
				vizinhos.append(matriz[i+1][j])
				vizinhos.append(matriz[i][j+1])
				vizinhos.append(matriz[i+1][j+1])
			elif i == 0 and j == largura-1:
				vizinhos.append(matriz[i+1][j])
				vizinhos.append(matriz[i][j-1])
				vizinhos.append(matriz[i+1][j-1])
			elif i == altura-1 and j == 0:
				vizinhos.append(matriz[i-1][j])
				vizinhos.append(matriz[i][j+1])
				vizinhos.append(matriz[i-1][j+1])
			elif i == altura-1 and j == largura-1:
				vizinhos.append(matriz[i-1][j])
				vizinhos.append(matriz[i][j-1])
				vizinhos.append(matriz[i-1][j-1])
			elif i == 0 and j != 0:
				vizinhos.append(matriz[i+1][j])
				vizinhos.append(matriz[i][j+1])
				vizinhos.append(matriz[i+1][j+1])		
				vizinhos.append(matriz[i][j-1])		
				vizinhos.append(matriz[i+1][j-1])		
			elif i != 0 and j == 0:
				vizinhos.append(matriz[i+1][j])
				vizinhos.append(matriz[i][j+1])
				vizinhos.append(matriz[i+1][j+1])		
				vizinhos.append(matriz[i-1][j])		
				vizinhos.append(matriz[i-1][j+1])
			elif i == altura-1 and j != largura-1:
				vizinhos.append(matriz[i-1][j])
				vizinhos.append(matriz[i][j-1])
				vizinhos.append(matriz[i-1][j-1])		
				vizinhos.append(matriz[i][j+1])		
				vizinhos.append(matriz[i-1][j+1])		
			elif i != altura-1  and j == largura-1:
				vizinhos.append(matriz[i-1][j])
				vizinhos.append(matriz[i][j-1])
				vizinhos.append(matriz[i-1][j-1])		
				vizinhos.append(matriz[i+1][j])		
				vizinhos.append(matriz[i+1][j-1])
			else:
				vizinhos.append(matriz[i+1][j])
				vizinhos.append(matriz[i][j+1])
				vizinhos.append(matriz[i+1][j+1])		
				vizinhos.append(matriz[i-1][j])		
				vizinhos.append(matriz[i-1][j+1])
				vizinhos.append(matriz[i][j-1])		
				vizinhos.append(matriz[i+1][j-1])
				vizinhos.append(matriz[i-1][j-1])

			if matriz[i][j] == 0:
				if vizinhos.count(1) == 2:
					matrizx[i][j] = 1
			elif matriz[i][j] == 1:
				if vizinhos.count(2) > 0:
					matrizx[i][j] = 2
			elif matriz[i][j] == 2:
				if vizinhos.count(1) > 1:
					matrizx[i][j] = 0
				elif vizinhos.count(1) == 0:
					matrizx[i][j] = 0
			vizinhos = []

	for i in range(altura):
		for j in range(largura):
			matriz[i][j] = matrizx[i][j]
