# Faça um Programa que peça dois números e imprima a soma

lista_numeros = []
soma = 0
for i in range(2):
	num = int(input('Digite um número: '))
	lista_numeros.append(num)
	soma += num

print(f'A soma de {lista_numeros[0]} e {lista_numeros[1]} é:', soma)
