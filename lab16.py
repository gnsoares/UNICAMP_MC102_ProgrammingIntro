#  Funcao: removePalavras
# 
#  Parametros:
#    s: string contendo o texto de entrada
#    vs: lista de strings com as palavras a serem removidas
# 
#  Descricao:
#    Deve-se remover as palavras de s que estiverem listadas em vs.
#    Ao final, s nao deve conter espacos extras.
#
# Retorno:
#   string s sem as palavras de vs.

def removePalavras(s, vs):
	# Obtencao de uma lista com os termos da string de entrada
	rP = s.split()

	# Remocao item a item enquanto as palavras a serem removidas estiverem presentes
	for i in vs:
		while i in rP:
			rP.remove(i)

	# Conversao da lista com as palavras removidas para string
	sep = ' '
	return sep.join(rP)

#  Funcao: pagsResposta
#
# Parametros:
#   paginas: lista de strings cada uma representando uma pagina
#   termosBusca: lista de strings com os termos a serem buscados
#
# Descricao:
#	Deve verificar se cada página em paginas contém todos os termos
#	de busca em termosBusca. Se a paginas[i] contiver todos os termos
#	então deve-se atribuir 1 para resp[i] e 0 caso não contenha pelo
#	menus um dos termos de busca.
#
# Retorno:
#   lista a ser preenchida como resposta, de dimensao numPag.

def pagsResposta(palavrasPagina, termosBusca):	
	pR = []
	# Para cada pagina cada termo de busca e checado:
	#	Se um dos termos de busca nao estiver presente, o valor na lista de retorno dessa pagina = 0 e nao sao conferidos os proximos termos
	#	Se todos os termos estiverem presentes, o valor na lista de retorno dessa pagina = 1
	for i in palavrasPagina:
		for j in termosBusca:
			if not(j in i.split()):
				pR.append(0)
				break
		else:
			pR.append(1)
	return [_ for _ in pR]
	

#  Funcao: linksResposta
#
# Parametros:
#   links: matriz quadrada binária representando links entre as paginas 
#   resp: lista obtido apos execucao de pagsResposta
#
# Descricao:
#   Deve-se preencher uma lista numLinks da seguinte maneira: para cada
#   posicao i (0 <= i < numPags), se resp[i] == 1, então numLinks[i] deve conter
#   o numero de links de outras paginas resposta para i. Caso resp[i] == 0,
#   entao numLinks[i] deve ser -1.
#
# Retorno
#   lista numLinks a ser preenchida como resposta, de tamanho numPag

def linksResposta(links,resp):
	lR = []
	# Para cada pagina o valor da resposta e checado:
	# 	Se for 0, recebe -1 links
	#	Se nao for 0, e feita a contagem de links de paginas com resposta diferente de 0
	for i in range(len(resp)):
		if resp[i] == 0:
			lR.append(-1)
		else:
			total = 0
			for j in range(len(resp)):
				if resp[j] != 0:
					total += links[j][i]
			lR.append(total)
	return [_ for _ in lR]
