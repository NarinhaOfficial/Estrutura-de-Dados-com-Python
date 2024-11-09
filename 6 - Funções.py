n = -1
while n!=0:
	print('1. Crie uma função que calcule a média de três números.')
	print('2. Defina uma função que converta Celsius para Fahrenheit.')
	print('3.Crie uma função que calcule a área de um círculo a partir do seu raio.')
	print('4.Escreva uma função is_palindrome que verifique se uma palavra é um palíndromo.')
	print('0 - Encerrar o programa')
	n = int(input(' '))

	if n==1:
		def media():
			m = (n1 + n2 + n3)/3
			print(m)
		n1 = 8; n2 = 9; n3 = 10; m=0
		media()
	elif n==2:
		def temperatura():
			t = c*1.8 + 32
			print(t)
		c = int(input('Informe a temperatura em Celsius: '))
		temperatura()
	elif n==3:
		def raio():
			a = 3.14 * r**2
			print(a)
		r = int(input('Informe o raio do círculo para calcular sua área: '))
		raio()
	elif n==4:
		lista = []
		invertida = []
		def palindromo():
			lista = list(n)
			invertida = lista[::-1]
			print(lista)
			print(invertida)
			if lista == invertida:
				print('É um palíndromo!')
			else:
				print('Não é um palíndromo')
		n = input('Informe a palavra para verificar se é um palíndromo: ')
		
		palindromo()