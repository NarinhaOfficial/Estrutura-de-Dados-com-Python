import math
import time
n=-1
while n!=0:
	print('1. Elaborar um programa Python para verificar se um número é par ou ímpar.')
	print('2. Elaborar um programa Python para calcular as raízes da equação do segundo grau.')
	print('3. Elaborar um programa Python para verificar se uma string é um palíndromo.')
	print('4. Escreva um programa que peça ao usuário para inserir um número (inteiro ou decimal) como uma string e converta-o para o tipo correto (int ou float).')
	print('5. Escreva um programa que peça ao usuário para inserir diferentes tipos de dados (número inteiro, número decimal, texto, valor booleano). O programa deve identificar e exibir o tipo de dado inserido.')
	print('0 - Encerrar o programa')
	n = int(input(''))

	if n==1:
		teste = int(input('Entre com um número: '))
		if teste%2 != 0:
			print('O número digitado é ímpar')
		else:
			print('O número digitado é par')
		time.sleep(5)
	elif n==2:
		teste = int(input('Entre com um número: '))
		print(f'A raiz quadrada é {math.sqrt(teste)}')
		time.sleep(5)
	elif n==3:
		teste = input('Entre com a palavra: ').strip().upper().split()
		juntando = ''.join(teste)
		invertendo = juntando[::-1]
		print(teste)
		print(juntando)
		print(invertendo)
		if juntando == invertendo:
			print('É um palíndromo')
		else:
			print('Não é um palíndromo')
	elif n==4:
		teste = input('Escreva um número: ')
		try:
			numero = float(teste)
			if numero.is_integer():
				print(f'O número é: {int(numero)}')
			else:
				print(f'O número é: {numero}')
		except ValueError:
			print('Entrada inválida!')
	elif n==5:
		teste = input('Pressione qualquer tecla ou digite algo: ')
		if teste.isnumeric():
			print('O que você digitou é um número')
		elif teste == 'True' or teste == 'False':
			print('O que você digitou é um booleano')
		elif teste.isalpha():
			print('O que você digitou é uma string')
		elif teste.isalnum():
			print('O que você digitou é um alfanumérico')
		elif bool(teste):
			print('O que você digitou é um booleano')
		else:
			print('.')
	else:
		print('Entrada inválida!')