# Faça um Programa que peça um valor e mostre
# na tela se o valor é positivo ou negativo.

from colorama import Fore, Style


def verificar_positivo_negativo(n):
    if n > 0:
        return 'Positivo!'
    elif n < 0:
        return 'Negativo!'
    else:
        return 'Neutro!'


def main():
    while True:
        try:
            valor = float(input('Digite o número: '))
            resultado = verificar_positivo_negativo(valor)
            if valor > 0:
                print()
                print('*' * 11)
                print(f'{Fore.GREEN}{Style.BRIGHT} {resultado}'
                      f'{Fore.RESET}{Style.RESET_ALL}')
                print('*' * 11)
            else:
                print()
                print('*' * 11)
                print(f'{Fore.RED}{Style.BRIGHT} {resultado}'
                      f'{Fore.RESET}{Style.RESET_ALL}')
                print('*' * 11)
            break
        except ValueError:
            print(f'{Fore.RED}{Style.BRIGHT}'
                  f'Entrada inválida. Digite um valor numérico.\n'
                  f'{Fore.RESET}{Style.RESET_ALL}')
        

if __name__ == '__main__':
    main()
    