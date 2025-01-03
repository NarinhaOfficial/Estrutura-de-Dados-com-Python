n = -1
while n!=0:
	print('\t\tEstrutura de Dados com Python')
	print('1 - Pilha')
	print('2 - Fila')
	print('3 - Lista')
	print('0 - Encerrar o programa')
	n = int(input(' '))
	if n==1:
		p=-1
		op = 0
		pilha = []
		while p !=0:
			print('\t\tPilha')
			print('1 - Empilhar (push)')
			print('2 - Desempilhar (pop)')
			print('3 - Imprimir')
			print('0 - Retornar ao menu principal')
			p = int(input(''))
			if p==1:
				op = int(input('Quantos elementos deseja empilhar?'))
				for x in range(op):
					elementos = int(input(f'Digite o {x+1}º elementos: '))
					pilha.append(elementos)
				print(pilha)
			elif p == 2: 
				if len(pilha) > 0: 
					elementos = pilha.pop() 
					print(f'Elemento {elementos} removido.') 
					print(pilha) 
				else: print('A pilha está vazia.') 
			elif p == 3:
				if pilha==[]:
					print('A pilha está vazia') 
				else:
					print(pilha)
			elif p==0:
				break
			else:
				print('Opção inválida! Digite...')
	elif n==2:
		p = -1 
		op = 0 
		fila = [] 
		while p != 0: 
			print('\t\tFila')
			print('1 - Enfileirar (enqueue)') 
			print('2 - Desenfileirar (dequeue)') 
			print('3 - Imprimir') 
			print('0 - Retornar ao menu principal') 
			p = int(input('')) 
			if p == 1: 
				op = int(input('Quantos elementos deseja enfileirar? ')) 
				for x in range(op): 
					elementos = int(input(f'Digite o {x + 1}º elemento: ')) 
					fila.append(elementos) 
				print(fila)
			elif p==2:
				if len(fila) > 0: 
					elementos = fila.pop(0) 
					print(f'Elemento {elementos} removido.') 
					print(fila) 
				else: 
					print('A fila está vazia.') 
			elif p == 3:
				if fila==[]:
					print('A fila está vazia')
				else:
					print(fila)
			elif p==0:
				break
			else:
				print('Opção inválida! Digite...')
	elif n==3:
		lista = ['Antônio', 'Bernardo', 'Carlos']
		p = -1
		while p!=0:
			print('\t\tLista')
			print('1 - Inserir no início')
			print('2 - Inserir em uma posição arbitrária')
			print('3 - Inserir no final')
			print('4 - Remover do início')
			print('5 - Remover de uma posição arbitrária')
			print('6 - Remover do final')
			print('7 - Imprimir')
			print('0 - Retornar ao menu principal')
			p = int(input('')) 
			if p ==1:
				elementos = input('Inserir no início: ')
				lista.insert(0, elementos)
			elif p==2:
				posicao = int(input('Em qual posição você deseja inserir? '))
				elementos = input(f'Inserindo na {posicao}ª posição: ')
				lista.insert(posicao-1, elementos)
			elif p==3:
				elementos = input('Inserir no final: ')
				lista.append(elementos)
			elif p==4:
				if lista==[]:
					print('A lista está vazia')
				else:
					lista.pop(0)
			elif p==5:
				if lista==[]:
					print('A lista está vazia')
				else:
					posicao = int(input('De qual posição você deseja remover? '))
					lista.pop(posicao-1)
			elif p==6:
				if lista==[]:
					print('A lista está vazia')
				else:
					lista.pop()
			elif p==7:
				if lista==[]:
					print('A lista está vazia')
				else:
					print(lista)
			elif p==0:
				break
			else:
				print('Opção inválida! Digite...')
	elif n==0:
			print('Programa Encerrrado!')
	else:
		print('Opção inválida! Digite...')