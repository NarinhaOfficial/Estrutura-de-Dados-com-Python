import time
n=-1
listas = []
while n!=0:
	print('1 - Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.')
	print('2. Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.')
	print('3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.')
	print('4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.')
	print('5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os númerospares no vetor PAR e os números ÍMPARES no vetor ímpar. Imprima os três vetores.')
	n = int(input(' '))

	if n==1:
		for x in range(5):
			v = int(input('Informe um número: '))
			listas.append(v)
		print(listas)
		time.sleep(3)
	elif n==2:
		for x in range(10):
			v = float(input('Informe um número: '))
			listas.append(v)
		listas.reverse()
		print(listas)
		time.sleep(3)
	elif n==3:
		soma = 0
		for indice in range(4):
			notas = float(input(f'Informe a {indice+1}ª nota: '))
			listas.append(notas)
			soma+=notas
		print(f'Notas: {listas}')
		print(f'Média: {soma/4}')
		time.sleep(3)
	elif n==4:
		i=0
		vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
		consoantes = []
		for x in range(10):
			v = input('Digite um caracter: ')
			if v not in vogais:
				i+=1
				consoantes.append(v)
		print(i)
		print(consoantes)
	elif n==5:
		par = []
		impar = []
		for x in range(20):
			n = int(input(f'Informe o {x+1}º número: '))
			if n%2==0:
				par.append(n)
			else:
				impar.append(n)
		print(f'Números pares:\n {par}')
		print(f'Números ímpares:\n {impar}')

