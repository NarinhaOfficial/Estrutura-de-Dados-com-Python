n=-1
while n!=0:
	print('\t\t\tMENU COM 10 QUESTÕES')
	print('2. Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos.')
	print('3. Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos têm 10 elementos cada. Imprimir todos os conjuntos.')
	print('4. Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois valores X e Y quaisquer correspondentes a duas posições no vetor. Ao final seu programa deverá escrever a soma dos valores encontrados nas respectivas posições X e Y.')
	print('5. Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.')
	print('6. Faça um programa que receba do usuário um vetor com 10 posições. Em seguida deverá ser impresso o maior e o menor elemento do vetor.')
	print('7. Escreva um programa que leia 10 números inteiros e os armazene em um vetor. Imprima o vetor, o maior elemento e a posição que ele se encontra.')
	print('8. Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos na 	ordem inversa.')
	print('9. Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre na tela os valores')
	print('12. Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos juntamente com o maior, o menor e a média dos valores.')
	print('13. Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se encontram o maior e o menor valor.')
	print('0 - Encerrar o programa')
	n = int(input(''))

	if n==2:
		lista = []
		for x in range(6):
			v = int(input(f'Digite o {x+1}º valor: '))
			lista.append(v)
		print(lista)

	elif n==3:
		conjuntos = set()
		quadrado = []
		for x in range(10):
			v = float(input(f'Digite o {x+1}º valor: '))
			conjuntos.add(v)
		print(conjuntos)
		for x in conjuntos:
			q = 0
			q = x**2
			quadrado.append(q)
		print(f'O quadrado dos números são:\n{quadrado}')
	elif n==4:
		lista=[]
		a = 0; b=0
		for x in range(8):
			v = int(input(f'Informe o valor do vetor na posição {x}: '))
			lista.append(v)
		x=-1
		while x<0 or x>7:
			x = int(input('Escolha uma posição de 0 a 7: '))
			if x<0 or x>7:
				print('Valor incorreto! Tem que ser entre 0 e 7!')
			else:
				print(f'O valor da posição x é {x}')
		y=-1
		while y<0 or y>7:
			y = int(input('Escolha uma posição de 0 a 7: '))
			if y<0 or y>7:
				print('Valor incorreto! Tem que ser entre 1 e 7!')
			else:
				print(f'O valor da posição y é {y}')
		a = lista[x]
		b = lista[y]
		print(f'A soma de {a} + {b} é: {a+b}')
	elif n==5:
		vetor = [1, 2, 3, 4, 5, 6, 7]
		contador = 0
		for x in vetor:
			contador+=1
		print(f'O número de pares do vetor é {contador//2}')
	elif n==6:
		vetor = []
		for x in range(10):
			v = int(input(f'Informe o {x+1}º elemento do vetor: '))
			vetor.append(v)
		maior = v; menor = v
		print(vetor)
		for x in vetor:
			if x > maior:
				maior = x
			if x < menor:
				menor = x
		print(f'O maior valor é {maior}\nO menor valor é {menor}')	
	elif n==7:
		vetor = []
		for x in range(10):
			v = int(input(f'Informe o {x+1}º elemento do vetor: '))
			vetor.append(v)
		maior = v; 
		print(vetor)
		for x in vetor:
			if x > maior:
				maior = x
		print(f'O maior elemento é: {maior}\nE a posição em que ele se encontra é: {vetor.index(maior)}')
	elif n==8:
		vetor = [1, 2, 3, 4, 5, 6, 7]
		print(vetor)
		vetor.reverse()
		print(vetor)
	elif n==9:
		vetor = []
		x = 0
		while len(vetor)<6:
			v = int(input(f'Informe o {x+1}º elemento do vetor: '))
			if v%2==0:
				vetor.append(v)
				x+=1
			else:
				print('Os números precisam ser par!')
		print(vetor)
	elif n==12:
		vetor = []
		soma = 0;
		for x in range(5):
			v = int(input(f'Informe o {x+1}º elemento do vetor: '))
			vetor.append(v)
		maior = v; menor = v
		print(vetor)
		for x in vetor:
			soma+=x
			if x > maior:
				maior = x
			if x < menor:
				menor = x
		print(f'Os valores lidos são {vetor}\nO maior valor é {maior}\nO menor valor é {menor}\nA média é {soma/5}')	
	elif n==13:
		vetor = []
		for x in range(5):
			v = int(input(f'Informe o {x+1}º elemento do vetor: '))
			vetor.append(v)
		maior = v; menor = v
		print(vetor)
		for x in vetor:
			if x > maior:
				maior = x
			if x < menor:
				menor = x
		print(vetor)
		print(f'O maior número é {maior} e sua posição é {vetor.index(maior)}')
		print(f'O menor número é {menor} e sua posição é {vetor.index(menor)}')