# -*- coding: UTF-8 -*-

class Perfil(object):
	'Classe padrao para perfis de usuarios'

	def __init__(self, nome, telefone, empresa):
		if(len(nome) < 3):
			raise ArgumentoInvalidoError('Nome deve ter pelo menos 3 caracteres')
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa
		self.__curtidas = 0

	def imprimir(self):
		print "Nome: %s, Telefone: %s, Empresa: %s" % (self.nome, self.telefone, self.empresa)

	def curtir(self):
		self.__curtidas+=1

	def get_curtidas(self):
		return self.__curtidas

	@classmethod
	def gerar_perfis(classe, nome_arquivo):
		arquivo = open(nome_arquivo, 'r')
		perfis = []
		for linha in arquivo:
			valores = linha.split(',')
			if(len(valores) is not 3):
				raise ValueError('Uma linha no arquivo %s deve possuir 3 valores' % nome_arquivo)
			perfis.append(classe(*valores))
		arquivo.close()
		return perfis

class Perfil_Vip(Perfil):
	'Classe padrao para perfis VIP\'s de usuarios'

	def __init__(self, nome, telefone, empresa, apelido = ''):
		super(Perfil_Vip, self).__init__(nome, telefone, empresa)
		self.apelido = apelido

	def get_creditos(self):
		return super(Perfil_Vip, self).get_curtidas() * 10

class Data(object):
	'Classe auxiliar para auxilio de datas'

	def __init__(self, dia, mes, ano):
		self.dia = dia
		self.mes = mes
		self.ano = ano

	def imprimir(self):
		print "%s/%s/%s" % (self.dia, self.mes, self.ano)

class Pessoa(object):
	'Classe par definicao de pessoas para calculo de IMC'

	def __init__(self, nome, peso, altura):
		self.nome = nome
		self.peso = float(peso)
		self.altura = float(altura)

	def calcular_imc(self):
		return self.peso/(self.altura ** 2)

	def imprimir_imc(self):
		print "IMC de %s: %s" % (self.nome, self.calcular_imc())

class Retangulo(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__area = x * y

    def obter_area(self):
        return self.__area

class ArgumentoInvalidoError(Exception):
	def __init__(self, mensagem):
		self.mensagem = mensagem

	def __str__(self):
		return repr(self.mensagem)