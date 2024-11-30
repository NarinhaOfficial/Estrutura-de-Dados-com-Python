n = -1
vetor = []
menores = []
maiores = []
s = 0
m=0
def soma(s):
	for x in range(5):
		v = int(input(f'Digite o {x+1}º valor: '))
		vetor.append(v)
		s+=v
	print(s)
	return s

def media(m, s):
	m = s/5
	print(f'A média é {m}')
	for x in vetor:
		if x<m:
			menores.append(x)
		elif x > m:
			maiores.append(x)
	print(f'Os números menores do que a média são {menores}')
	print(f'Os números maiores do que a média são {maiores}')
	return m
while n!=0:
	print('\t\tExercícios – Vetores não ordenados')
	print('1. Faça um programa que leia 5 valores inteiros, armazeno-os em um vetor, calcule e apresente a soma destes valores.')
	print('2. Altere o programa anterior para calcular e apresentar a média dos valores entrados e aqueles que são maiores e menores que a média.')
	print('3. Receba uma lista de números e um número específico do usuário. Conte quantas vezes esse número aparece na lista.')
	print('4. Escreva um programa que receba uma lista e remova todos os elementos duplicados, deixando apenas os valores únicos.')
	print('5. Receba duas listas e crie uma nova lista que contenha apenas os elementos que aparecem em ambas.')
	print('6. Receba uma lista e um valor do usuário. Remova todas as ocorrências desse valor da lista.')
	print('0 - Encerrar o programa')
	n = int(input(' '))
	if n==1:
		s = soma(s)
	elif n==2:
		if vetor==[]:
			s = soma(s)
		m = media(m,s)
	elif n==3:
		contador=0
		u = int(input('Informe seu número: '))
		for x in range(5):
			v = int(input(f'Digite o {x+1}º valor: '))
			vetor.append(v)
			if u == v :
				contador+=1
		print(f'Seu número aparece na lista {contador} vezes')
	elif n==4:
		for x in range(5):
			v = int(input(f'Digite o {x+1}º valor: '))
			vetor.append(v)
		conjunto = set(vetor)
		lista = list (conjunto)
		print(lista)
	elif n==5:
		lista1 = [1, 2, 3, 4, 5]
		lista2 = [2, 4, 6, 8, 10]
		lista3 = []
		lista3 = set(lista1) & set(lista2)
		print(lista3)
	elif n==6:
		u = 3
		lista = [1, 2, 3, 4, 5]
		lista = [x for x in lista if x != u]
		print(lista)