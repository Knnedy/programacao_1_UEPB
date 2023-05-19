# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

from colorama import Fore, Style


def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media


def main():
    notas = []
    for i in range(4):
        while True:
            try:
                nota = float(input(f'Digite a {i + 1}º nota: '))
                notas.append(nota)
                break
            except ValueError:
                print(f'{Fore.RED}{Style.BRIGHT}'
                      f'Entrada inválida. Digite um valor numérico.'
                      f'{Fore.RESET}{Style.RESET_ALL}')
    
    media_notas = calcular_media(notas)
    print(f'A média das notas é {media_notas:.2f}')


if __name__ == '__main__':
    main()

# for i in range(4):
# 	entrada_notas = float(input(f'Digite a {i+1}º nota: '))
# 	lista_notas.append(entrada_notas)
# 	soma += entrada_notas
# 	media_notas = soma / len(lista_notas)
#
# print(f'A média é: {media_notas:.2f}')
