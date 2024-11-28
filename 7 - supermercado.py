lista = []
n=-1
while n!=0:
	print('1. Crie um programa que permite ao usuário adicionar itens a uma lista de compras, verificar se um item está na lista e remover itens. A lista não precisa estar ordenada.')
	print('2. Crie uma função que verifica se dois vetores (listas) possuem os mesmos elementos, independentemente da ordem.')
	n = int(input(' '))

	if n==1:
		a = -1
		while a!=0:
			print('1 - Adicionar')
			print('2 - Buscar')
			print('3 - Remover')
			print('4 - Mostrar lista')
			print('0 - Voltar ao menu inicial')
			a = int(input(' '))
			if a==1:
				elementos = int(input('Quantos produtos você deseja inserir? '))
				for x in range(elementos):
					adicionar = input('Insira o item que deseja adicionar: ')
					lista.append(adicionar)
			elif a==2:
				verificar = input('Digite o nome do item que deseja verificar na lista: ')
				print(verificar in lista)
			elif a==3:
				remover = input('Qual item você deseja remover? ')
				lista.remove(remover)
			elif a==4:
				print(lista)
			else:
				print('Dígito incorreto! Tente novamente!')
	elif n==2:
		lista = (1, 2, 3, 4, 5)
		lista2 = (5, 4, 3, 2, 1)
		if set(lista) == set(lista2):
			print('Possuem os mesmos elementos!')
		else:
			print('Não possuem os mesmos elementos!')