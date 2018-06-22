# Funçoes auxiliares:
	# getSubordinates: retorna em forma de lista do python os indices dos suborninados
	# SelectionSort: retorna uma lista qualquer em ordem crescente

def getSubordinates(mat, numFun, k, out=[]):
	""" Essa funcao recebe como parametros a estrutura hierarquica da empresa em forma
		de matriz, o numero total de funcionarios, o indice do funcionario desejado e
		uma lista que sera usada para guardar a saida.

		Ela usa recursao. Cada chamada da funcao guarda os subordinados diretos do
		funcionario pedido na chamada atual. Para cada subordinado encontrado, a funcao
		e chamada novamente. A condicao de parada e quando o funcionario pedido for o
		mais baixo da empresa.															""" 

	if k == numFun:
		return None
	else:
		for i in range(len(mat[k])):
			if mat[k][i] == '1':
				out.append(i)
				getSubordinates(mat, numFun, i, out)
		return out

def SelectionSort(vec):
	""" Essa funcao usa o metodo Selection Sort para ordenar crescentemente numeros em
		uma lista passada como parametro e retorna uma lista com os valores ordenados	"""

	for i in range(len(vec)-1):
		for j in range(i,len(vec)):
			if vec[j] == min(vec[i:len(vec)]):
				vec[j], vec[i] = vec[i], vec[j]
	return vec

if __name__ == "__main__":

	# A lista n guarda o numero de funcionarios e o funcionario a ser dada a lista de subordinados
	n = [int(i) for i in input().split()]
	# A matriz table guarda estrutura hierarquica da empresa em forma de matriz
	table = [[i for i in input().split()] for i in range(n[0])]
	
	# A lista ans guarda a resposta
	ans = [i for i in getSubordinates(table, n[0], n[1])]
	ans = [n[1]] + SelectionSort(ans)

	# Impressao do resultado
	print(' '.join(str(i) for i in ans))