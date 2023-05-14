# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

lista_notas = []
media_notas = soma = 0

for i in range(4):
	entrada_notas = float(input(f'Digite a {i+1}º nota: '))
	lista_notas.append(entrada_notas)
	soma += entrada_notas
	media_notas = soma / len(lista_notas)

print(f'A média é: {media_notas:.2f}')
