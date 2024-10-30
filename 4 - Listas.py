import time
#lista_numeros.append(6) adiciona no final
#lista_numeros.insert(2, 99) adiciona o 99 na posição 2
#lista_numeros.extend([7, 8, 9]) adiciona vários elementos no final da lista
#ultimo = lista_numeros.pop() remove, mas também retorna. É tipo o ctrl x
#lista_numeros.clear() deixa a lista vazia
lista = [] 
completa = []
lista2 = []
for x in range(10):
	lista.append(x+1)
n=-1
while n!=0:
	print('MENU')
	print('1 - Crie uma lista contendo os números de 1 a 10 e imprima o quadrado de cada número.')
	print('2 - Adicione o número 11 ao final da lista e remova o número 5.')
	print('3 - Reordene a lista em ordem decrescente.')
	print('4 - Crie uma matriz (lista de listas) e acesse o valor na segunda linha e terceira coluna.')
	print('0 - Encerrar o programa')
	n = int(input(''))
	if n==1:
		quadrados = [x**2 for x in lista]
		print(quadrados)
		time.sleep(5)
	elif n==2:
		lista.append(11)
		lista.remove(5)
		print(lista)
		time.sleep(5)
	elif n==3:
		lista.reverse()
		print(lista)
	elif n==4:
		for x in range(3):
			lista2 = []
			for z in range(3):
				i = int(input('Preencha a matriz: '))
				lista2.append(i)
			completa.append(lista2)
		print(completa)
		print(f'O valor da segunda linha e terceira coluna é: {completa[1][2]}')
		time.sleep(5)
	elif n==0:
		break
	else:
		print('Tecla inválida!')