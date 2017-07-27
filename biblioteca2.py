def gera_nome_convite(nome):
	parte1 = nome[0:4]
	tamanho = len(nome)
	parte2 = nome[tamanho - 4: tamanho]
	return parte1 + ' ' + parte2

def envia_convite(nome):
	return 'Enviando convite para ' + nome

def processa_convite(nome):
	novo_nome = gera_nome_convite(nome)
	return envia_convite(novo_nome)