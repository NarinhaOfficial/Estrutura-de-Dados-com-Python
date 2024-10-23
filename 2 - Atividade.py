n=-1
string = 'Aprender Python é muito divertido'
while n!=0:
	print('Dada a string: Aprender Python é muito divertido. Faça o seguinte:')
	print('1 - Conte quantos caracteres existem na string')
	print('2 - Transforme toda a frase para letras maíusculas')
	print('3 - Substitua a palavra divertido por fácil')
	print('4 - Verifique se a palavra Python está presente na frase')
	print('0 - Encerrar o programa')
	n = int(input(''))

	if n==1:
		space = string.count(' ')
		total = len(string)
		print(f'Existem {total - space} caractere')
	elif n==2:
		print(f'{string.upper()}')
	elif n==3:
		print(f'{string.replace('divertido', 'fácil')}')
	elif n==4:
		print(f'{'Python' in string}')
	elif n==0:
		print('Programa finalizado com sucesso!')
	else:
		print('Tecla inválida! Tente novamente ou pressione 0 para finalizar!')