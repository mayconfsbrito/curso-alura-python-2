from models import *

# arquivo = None
# try:
# 	arquivo = open('perfis.csv', 'r')
# 	valores = arquivo.readline().split(':')
# 	Perfil(*valores)
# 	print('arquivo foi aberto')
# 	arquivo.close()
# except (IOError, TypeError) as error: 
# 	print('Deu Erro %s' % error)	
# finally:
# 	if(arquivo is not None):
# 		print('Fechando arquivo')
# 		arquivo.close()

perfis = Perfil.gerar_perfis('perfis.csv')