n=-1
while n!=0:
	print('1 - Faça um programa que mostre a mensagem Alô mundo na tela')
	print('2 - Faça um programa que pela um número e mostre a mensagem o númeo informado foi...')
	print('3 - Faça um programa que peça 2 números e imprima a soma')
	print('4 - Média de 4 notas')
	print('5 - converção de metros para centímetros')
	print('6 - Peça o raio de um círculo, calcule e mostre sua área')
	print('7 - Calcule a área de um quadrado e mostre o dobro dessa área')
	print('8 - Quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês')
	n = int(input(''))
	if n==1:
		print('Alô mundo')
	elif n==2:
		numero = input('Digite um número: ')
		print(f'O número informado foi: {numero}')
	elif n==3:
		n1 = int(input('Digite um número: '))
		n2 = int(input('Digite um número: '))
		print(f'{n1+n2}')
	elif n==4:
		n1 = int(input('Digite a 1ª nota: '))
		n2 = int(input('Digite a 2ª nota: '))
		n3 = int(input('Digite a 3ª nota: '))
		n4 = int(input('Digite a 4ª nota: '))
		print(f'{(n1+n2+n3+n4)/4}')
	elif n==5:
		m = int(input('Digite o valor em metros: '))
		print(f'{m*100}')
	elif n==6:
		r = float(input('Informe o raio: '))
		print(f'A área do círculo é: {3.14*(r**2)}')
	elif n==7:
		q = float(input("Informe a área do quadrado para saber o seu dobro: "))
		print(f'A área é: {q**2} e seu dobro é: {(q**2)*2}')
	elif n==8:
		
	elif n==0:
		print('Programa encerrado!')
		break
	