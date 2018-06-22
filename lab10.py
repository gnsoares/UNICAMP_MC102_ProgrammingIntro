# Programa de edição de texto. O programa lê o texto inicial e pode fazer com ele 3 modificações: Apagar, Inverter e Substituir palavras. O usuário dá o comando desejado e os argumentos desejados. O programa imprime, após o comando, a modificação feita.

texto = input()		# Leitura do texto inicial
print(texto)		# Impressão do texto inicial
comando = input()	# Comando inicial

pont = ['.',',',':','!','?']	# Lista com as pontuações que podem surgir

# Loop que garante o funcionamento do programa enquanto o usuário desejar
while comando != "Q":

	# Função Apagar
	if comando == "D":

		palavra_deletar = input()					# Leitura da palavra a ser apagada
		palavra_deletar = palavra_deletar.lower()	# A variável fica toda minúscula para comparação
		textoaux = texto.lower().split()			# O texto fica todo minúsculo para comparação

		# Remoção de todas as ocorrências da palavra desejada
		for i in range(textoaux.count(palavra_deletar)):
			textoaux.remove(palavra_deletar)
		for i in range(textoaux.count(palavra_deletar + '.')):
			textoaux.remove(palavra_deletar + '.')
		for i in range(textoaux.count(palavra_deletar + ',')):
			textoaux.remove(palavra_deletar + ',')
		for i in range(textoaux.count(palavra_deletar + ':')):
			textoaux.remove(palavra_deletar + ':')
		for i in range(textoaux.count(palavra_deletar + '!')):
			textoaux.remove(palavra_deletar + '!')
		for i in range(textoaux.count(palavra_deletar + '?')):
			textoaux.remove(palavra_deletar + '?')

		# Retornando as palavras não removidas para a sua formatação original
		textoaux2 = []
		for i in range(len(texto.split())):
			if texto.lower().split()[i] in textoaux:
				textoaux2.append(texto.split()[i])
		separador = ' '
		texto = separador.join(textoaux2)

		print(texto)	# Impressão das modificações feitas

	# Função Inverter
	elif comando == "I":

		palavra_inverter = input()					# Leitura da palavra a ser invertida
		palavra_inverter = palavra_inverter.lower()	# A variável fica toda minúscula para comparação
		textoaux = texto.lower().split()			# O texto fica todo minúsculo para comparação
		textoaux2 = texto.split()					# Lista que inverterá apenas a palavra desejada

		#Inversão de todas as ocorrências da palavra desejada
		for i in range(textoaux.count(palavra_inverter)):
			inv = ''
			pos = textoaux.index(palavra_inverter)
			textoaux[pos] = ''
			for x in textoaux2[pos]:
				inv = x + inv
			textoaux2[pos] = inv
		for j in pont:
			for i in range(textoaux.count(palavra_inverter + j)):
				inv = ''
				pos = textoaux.index(palavra_inverter + j)
				textoaux[pos] = ''
				for x in textoaux2[pos]:
					if x != j:
						inv = x + inv
				textoaux2[pos] = inv + j
		
		# Retornando as palavras não invertidas para a sua formatação original
		for i in range(len(texto.split())):
			if texto.lower().split()[i] in textoaux2:
				textoaux2[i] = texto.split()[i]
		separador = ' '
		texto = separador.join(textoaux2)

		print(texto)	#Impressão das modificações feitas

	# Função Substituir
	elif comando == "R":

		palavra_velha = input()					# Leitura da palavra a substituir
		palavra_velha = palavra_velha.lower()	# A variável fica toda minúscula para comparação
		palavra_nova = input()					# Leitura da palavra a ser substituida
		textoaux = texto.lower().split()		# O texto fica todo minúsculo para comparação

		# Substituição de todas as ocorrências da palavra desejada
		for i in range(textoaux.count(palavra_velha)):
			textoaux[textoaux.index(palavra_velha)] = palavra_nova
		for j in pont:
			for i in range(textoaux.count(palavra_velha + j)):
				textoaux[textoaux.index(palavra_velha + j)] = palavra_nova + j

		# Retornando as palavras não substituidas para a sua formatação original
		for i in range(len(texto.split())):
			if texto.lower().split()[i] in textoaux:
				textoaux[i] = texto.split()[i]
		separador = ' '
		texto = separador.join(textoaux)

		print(texto)	# Impressão das modificações feitas

	# Próximo comando
comando = input()
