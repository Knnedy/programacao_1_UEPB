# Faça um Programa que peça dois números e imprima a soma

numeros = []
soma = 0
for i in range(2):
	num = int(input('Digite um número: '))
	numeros.append(num)
	soma += num

print(f'A soma de {numeros[0]} e {numeros[1]} é:', soma)
