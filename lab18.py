# Classe que armazena os dados de uma imagem
class pic:
	def __init__(self):
		self.file = ''
		self.format = ''
		self.size = []
		self.max = ''
		self.matrix = []

# Classe que armazena o arquivo, o divisor e a matriz nucleo usados na convolucao 
class md:
	def __init__(self):
		self.file = ''
		self.div = 0
		self.matrix = []

import sys

# Leitura dos arquivos de entrada
PATH_IMG = sys.argv[1]
PATH_MD = sys.argv[2]
# Obtencao dos dados da imagem original
or_pic = pic()
or_pic.file = open(PATH_IMG,"r")
or_pic.format = or_pic.file.readline()
or_pic.size = [int(i) for i in or_pic.file.readline().split()]
or_pic.max = int(or_pic.file.readline())
or_pic.matrix = [[int(i) for i in or_pic.file.readline().split()] for j in range(or_pic.size[1])]
# Obtencao dos paramentros da convolucao
param = md()
param.file = open(PATH_MD,"r")
param.div = int(param.file.readline())
param.matrix = [[int(i) for i in param.file.readline().split()] for j in range(3)]
# Atribuicao dos dados da imagem depois da convolucao
new_pic = pic()
new_pic.format = or_pic.format
new_pic.size = or_pic.size
new_pic.max = or_pic.max

# Execucao da convolucao
for i in range(or_pic.size[1]):
	row = []
	for j in range(or_pic.size[0]):
		if i == 0 or i == or_pic.size[1]-1 or j == 0 or j == or_pic.size[0]-1:
			row.append(or_pic.matrix[i][j])
		else:
			value = 0
			for k in range(len(param.matrix)):
				for l in range(len(param.matrix[0])):
					value += param.matrix[k][l]*or_pic.matrix[i-1+k][j-1+l]
			value //= param.div
			value = max(0,value)
			value = min(or_pic.max,value)
			row.append(value)
	new_pic.matrix.append(row)

# Impressao do texto do arquivo da imagem depois da convolucao
print(str(new_pic.format)+' '.join([str(i) for i in or_pic.size])+'\n'+str(or_pic.max)+'\n'+'{}'.format('  \n'.join([' '.join(['{}'.format(i) for i in row]) for row in new_pic.matrix]))+'  ')