# Programa que determina o dia de compra/venda de blocos de ações visando maximizar o lucro, sendo o ganho com cada bloco de ações definido como o valor que se vendeu aquele bloco menos o valor que ele foi comprado. São usados como entrada os valores diários dos blocos de ações de quatro empresas e a saída é o melhor dia para comprar e vender as ações de cada empresa.

# Leitura e declaração das variáveis a serem usadas
dias = int(input())
valor = [[float(input()) for dia in range(dias)] for empresa in range(4)]
lucro = [0]*4
lucroaux = [0]*4
c = [[0 for dia in range(dias)] for empresa in range(4)]
v = [[0 for dia in range(dias)] for empresa in range(4)]
caux = [[0 for dia in range(dias)] for empresa in range(4)]
vaux = [[0 for dia in range(dias)] for empresa in range(4)]


# Cada empresa pode ser comprada em um dia de 1 a dias - 1 e vendida em um dia de 2 a dias. Por isso devem ser testadas todas as combinações possíveis para se encontrar a solução

for c1 in range(dias-1):
	for v1 in range(1,dias):
		for c2 in range(dias-1):
			for v2 in range(1,dias):
				for c3 in range(dias-1):
					for v3 in range(1,dias):
						for c4 in range(dias-1):
							for v4 in range(1,dias):
								# Cálculo dos lucros de cada empresa
								if valor[0][v1] > valor[0][c1] and v1 > c1:
									lucroaux[0] = valor[0][v1]-valor[0][c1]
								if valor[1][v2] > valor[1][c2] and v2 > c2:
									lucroaux[1] = valor[1][v2]-valor[1][c2]
								if valor[2][v3] > valor[2][c3] and v3 > c3:
									lucroaux[2] = valor[2][v3]-valor[2][c3]
								if valor[3][v4] > valor[3][c4] and v4 > c4:
									lucroaux[3] = valor[3][v4]-valor[3][c4]
							
								# Se um lucro maior for encontrado, checar se é válido como solução
								if sum(lucroaux) > sum(lucro):
																		
									if lucroaux[0] > 0:
										caux[0][c1] = 1
										vaux[0][v1] = 1
									if lucroaux[1] > 0:
										caux[1][c2] = 1
										vaux[1][v2] = 1
									if lucroaux[2] > 0:
										caux[2][c3] = 1
										vaux[2][v3] = 1
									if lucroaux[3] > 0:
										caux[3][c4] = 1
										vaux[3][v4] = 1
									
									MatrizValida = True
									# Teste das condições pedidas:
										# pode ter na carteira de aplicações um bloco por vez
										# as ações de cada empresa podem ser compradas no máximo uma vez
									if caux[0].count(1) <= 1 and caux[1].count(1) <= 1 and caux[2].count(1) <= 1 and caux[3].count(1) <= 1:
										for i in range(dias):
											if caux[0][i] + caux[1][i] + caux[2][i] + caux[3][i] > 1 or vaux[0][i] + vaux[1][i] + vaux[2][i] + vaux[3][i] > 1:
												MatrizValida = False
										for i in range(4):
											for j in range(dias-1):	
												if caux[i][j] == 1 and vaux[i][j+1] == 0:
													for k in range(4):
														if caux[k][j+1] == 1:
															MatrizValida = False
											for j in range(dias-2):	
												if caux[i][j] == 1 and vaux[i][j+1] == 0 and vaux[i][j+2] == 0:
													for k in range(4):
														for l in range(1,3):
															if caux[k][j+l] == 1:
																MatrizValida = False
											for j in range(dias-3):	
												if caux[i][j] == 1 and vaux[i][j+1] == 0 and vaux[i][j+2] == 0 and vaux[i][j+3] == 0:
													for k in range(4):
														for l in range(1,4):
															if caux[k][j+l] == 1:
																MatrizValida = False
											for j in range(dias-4):	
												if caux[i][j] == 1 and vaux[i][j+1] == 0 and vaux[i][j+2] == 0 and vaux[i][j+3] == 0 and vaux[i][j+4] == 0:
													for k in range(4):
														for l in range(1,5):
															if caux[k][j+l] == 1:
																MatrizValida = False
											for j in range(dias-5):	
												if caux[i][j] == 1 and vaux[i][j+1] == 0 and vaux[i][j+2] == 0 and vaux[i][j+3] == 0 and vaux[i][j+4] == 0 and vaux[i][j+5] == 0:
													for k in range(4):
														for l in range(1,6):
															if caux[k][j+l] == 1:
																MatrizValida = False
											for j in range(dias-6):	
												if caux[i][j] == 1 and vaux[i][j+1] == 0 and vaux[i][j+2] == 0 and vaux[i][j+3] == 0 and vaux[i][j+4] == 0 and vaux[i][j+5] == 0 and vaux[i][j+6] == 0:
													for k in range(4):
														for l in range(1,7):
															if caux[k][j+l] == 1:
																MatrizValida = False
									else:
										MatrizValida = False
									
									if MatrizValida:
										for i in range(4):
											lucro[i] = lucroaux[i]
											for j in range(dias):
												c[i][j] = caux[i][j]
												v[i][j] = vaux[i][j]		
								
								lucroaux = [0]*4
								caux = [[0 for dia in range(dias)] for empresa in range(4)]
								vaux = [[0 for dia in range(dias)] for empresa in range(4)]

# Impressão dos valores obtidos
for i in range(4):
	if max(c[i]) == 1:
		print("acao %d: compra %d, venda %d, lucro %.2f" %(i+1, c[i].index(1)+1, v[i].index(1)+1, lucro[i]))
print("Lucro: %.2f" %(sum(lucro)))
