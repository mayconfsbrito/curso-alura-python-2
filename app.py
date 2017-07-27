# -*- coding: UTF-8 -*-

import re	

def procurar(nomes):
	print 'Digite o nome a procurar:'
	nome_a_procurar = raw_input()

	if(nome_a_procurar in nomes):
		print 'Nome %s encontrado na posição %d' % (nome_a_procurar, nomes.index(nome_a_procurar))
	else:
		print 'Nome %s não encontrado' % (nome_a_procurar)
		
def procurar_regex(nomes):
	print 'Digite a expressão regular:'
	regex = raw_input()
	nomes_concatenados = ' '.join(nomes)
	resultado = re.findall(regex, nomes_concatenados)
	print resultado

def alterar(nomes):
	print 'Qual nome você gostaria de alterar?'
	nome = raw_input()

	if(nome in nomes):
		index = nomes.index(nome)
		print 'Qual será o novo nome?'
		novo_nome = raw_input()
		nomes[index] = novo_nome

def remover(nomes):
	print 'Qual nome você gostaria de remover?'
	nome = raw_input()
	nomes.remove(nome)

def listar(nomes):
	print 'Listando nomes:'
	for nome in nomes:
		print nome

def cadastrar(nomes):
	print 'Digite: o nome:'
	nome = raw_input()
	nomes.append(nome)

def menu():
	nomes = []
	escolha = ''
	while(escolha != '0'):
		print 'Digite: \n1 - cadastrar\n2 - listar\n3 - remover\n4 - alterar\n5 - procurar\n6 - procurar regex\n0 - terminar'
		escolha = raw_input()

		if(escolha == '1'):
			cadastrar(nomes)

		if(escolha == '2'):
			listar(nomes)

		if(escolha == '3'):
			remover(nomes)

		if(escolha == '4'):
			alterar(nomes)

		if(escolha == '5'):
			procurar(nomes)

		if(escolha == '6'):
			procurar_regex(nomes)

menu()