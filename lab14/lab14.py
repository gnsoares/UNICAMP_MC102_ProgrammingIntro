import math

# Funcao de checagem se a lista de alunos esta ordenada
	# Confere se os dois primeiros valores estao em ordem crescente ou decrescente
	# Se quaisquer outros dois valores consecutivos estiverem em ordem diferente retorna 0
	# Senao a lista esta ordenada e retorna 1 caso crescente ou -1 caso decrescente
def DACcheck(mat):
	if mat[1] > mat[0]:
		for i in range(len(mat)-1):
			if mat[i+1] < mat[i]:
				return 0
		return 1
	elif mat[1] < mat[0]:
		for i in range(len(mat)-1):
			if mat[i+1] > mat[i]:
				return 0	
		return -1

# Funcao de impressao
	# Confere se a lista esta preenchida
	# Caso verdadeiro imprime cada elemento sem quebra de linha e com espaco entre eles
	# Termina a impressao com uma quebra de linha
def DACprint(mat):
	if mat != []:
		for i in mat:
			print(i, end=' ')
		print()
	return None

# Funcao de ordenacao crescente usando o metodo Selection Sort
def DACsortIncreasing(mat):
	for i in range(len(mat) - 1):
		for j in range(i, len(mat)):
			if mat.index(min(mat[i:len(mat)])) > j:
				mat[mat.index(min(mat[i:len(mat)]))], mat[j] = mat[j], mat[mat.index(min(mat[i:len(mat)]))]
	return None

# Funcao de ordenacao decrescente usando o metodo Selection Sort
def DACsortDecreasing(mat):
	for i in range(len(mat) - 1):
		for j in range(i, len(mat)):
			if mat.index(max(mat[i:len(mat)])) > j:
				mat[mat.index(max(mat[i:len(mat)]))], mat[j] = mat[j], mat[mat.index(max(mat[i:len(mat)]))]
	return None

# Funcao de busca binaria
	# Confere se a lista esta ordenada
		# Caso verdadeiro imprime mensagem de erro
		# Caso falso continua execucao
	# A busca e binaria e executada e a cada passo a posicao da busca e impressa
		# No momento que a posicao desejada e encontrada, e impressa a posicao e a funcao e interrompida
		# Se o numero de passos exceder a complexibilidade e impressa mensagem de erro
def DACfind(RA, mat):
	if DACcheck(mat) == 0:
		print('Vetor nao ordenado!')
	elif DACcheck(mat) == 1:
		beg = 0
		end = len(mat) - 1
		while beg <= end:
			ref = (beg + end)//2
			print(ref, end=' ')
			if mat[ref] == RA:
				print()
				print("%d esta na posicao: %d" %(RA, ref))
				return None
			elif mat[ref] > RA:
				end = min(ref - 1, len(mat) - 1)
			elif mat[ref] < RA:
				beg = max(0,ref + 1)
		print()
		print("%d nao esta na lista!" %(RA))
	elif DACcheck(mat) == -1:
		beg = 0
		end = len(mat) - 1
		while beg <= end:
			ref = (beg + end)//2
			print(ref, end=' ')
			if mat[ref] == RA:
				print()
				print("%d esta na posicao: %d" %(RA, ref))
				return None
			elif mat[ref] < RA:
				end = min(ref - 1, len(mat) - 1)
			elif mat[ref] > RA:
				beg = max(0,ref + 1)
		print()
		print("%d nao esta na lista!" %(RA))
	return None

# Funcao de inclusao de alunos
	# Se o aluno ja estiver matriculado e impressa mensagem de erro
	# Se a lista tiver no seu valor maximo e impressa mensagem de erro
	# Caso seja possivel incluir o aluno a execucao continua
		# Confere se a lista esta ordenada e de que maneira
		# Aluno matriculado no fim da lista
		# Caso a lista estivesse ordenada, e repetida a ordenacao anterior com o novo aluno
def DACinsert(RA, mat):
	if len(mat) >= 150:
		print('Limite de vagas excedido!')
	elif mat.count(RA) == 1:
		print('Aluno ja matriculado na turma!')
	else:
		sortKind = DACcheck(mat)
		mat.append(RA)
		if sortKind == 1:
			DACsortIncreasing(mat)
		elif sortKind == -1:
			DACsortDecreasing(mat)
	return None

# Funcao de remocao
	# Se a lista estiver vazia e impressa mensagem de erro
	# Se o aluno nao pertencer a turma e impressa mensagem de erro
	# Caso contrario a remocao e feita
def DACremove(RA, mat):
	if mat == []:
		print('Nao ha alunos cadastrados na turma!')
	elif mat.count(RA) == 0:
		print('Aluno nao matriculado na turma!')
	else:
		mat.remove(RA)
	return None

# Leitura da lista inicial de alunos
StudList = [int(i) for i in input().split()]

# Inicializacao da variavel de comando
command = [0]

# Execucao dos comandos desejados
while command[0] != 's':

	if command[0] == 'p':
		DACprint(StudList)
	elif command[0] == 'c':
		DACsortIncreasing(StudList)
	elif command[0] == 'd':
		DACsortDecreasing(StudList)
	elif command[0] == 'b':
		DACfind(int(command[1]), StudList)
	elif command[0] == 'i':
		DACinsert(int(command[1]), StudList)
	elif command[0] == 'r':
		DACremove(int(command[1]), StudList)

	# Leitura do proximo comando
	command = input().split()
