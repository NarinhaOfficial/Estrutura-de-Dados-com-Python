import time
n=-1
listas = []
while n!=0:
	print('1 - Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.')
	print('2. Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.')
	print('3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.')
	print('4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.')
	print('5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os númerospares no vetor PAR e os números ÍMPARES no vetor ímpar. Imprima os três vetores.')
	print('6. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.')
	print('7. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.')
	print('8. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.')
	print('9. Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos  quadrados dos elementos do vetor.')
	print('10. Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20	elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.')
	
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
	elif n==6:
		listas = []
		for alunos in range(3):
			soma = 0
			media = 0
			for notas in range(4):
				n = float(input(f'Informe a {notas+1}ª nota: '))
				soma += n
			media = soma/4
			if media >= 7:
				listas.append(media)
		print(f'O número de alunos com média maior ou igual a 7 é: {len(listas)}')
		print(listas)
	elif n==7:
		soma = 0
		produto = 1
		numeros = []
		for x in range(5):
			n = int(input(f'Informe o {x+1}º número: '))
			soma+=n
			produto*=n
			numeros.append(n)
		print(f'Soma: {soma}\nMultiplicação: {produto}\n{numeros}')

	elif n==8:
		idade = []
		altura = []
		for x in range(5):
			i = int(input('Idade: '))
			a = float(input('Altura: '))
			idade.append(i)
			altura.append(a)
		idade.reverse()
		altura.reverse()
		print(idade)
		print(altura)
	elif n==9:
		import random
		n = [random.randint(1,100) for _ in range(10)]
		quadrado = 0
		soma = 0
		for indice in n:
			quadrado = indice**2
			soma += quadrado
		print(n)
		print(quadrado)
		print(f'A soma dos quadrados é: {soma}')
	elif n==10:
		par = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
		impar = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
		acumulador = 0
		junto = []
		while par != []:
			acumulador = impar.pop()
			junto.append(acumulador)
			acumulador = par.pop()
			junto.append(acumulador)
		junto.reverse()
		print(junto)