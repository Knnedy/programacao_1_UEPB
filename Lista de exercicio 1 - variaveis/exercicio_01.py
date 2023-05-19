# Faça um Programa que peça um número e então mostre a mensagem:
# O número informado foi [número]

from colorama import Fore, Style


def exibir_numero(n):
    return n


def main():
    while True:
        try:
            num = int(input('Digite um número: '))
            if num <= 0:
                raise ValueError(f'{Fore.RED}{Style.BRIGHT}'
                                 f'Digite um numero maior que 0.'
                                 f'{Fore.RED}{Style.BRIGHT}')
            else:
                numero_lido = exibir_numero(num)
                print(f'O número informado foi [{numero_lido}]')
                break
        except ValueError as error:
            print(f'{Fore.RED}{Style.BRIGHT}Erro: {error}{Fore.RESET}{Style.RESET_ALL}')
            

if __name__ == '__main__':
    main()
    