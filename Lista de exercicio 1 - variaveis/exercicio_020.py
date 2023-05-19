# Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores de forma que a
# variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor
# da variável A. Apresentar os valores trocados.

from colorama import Fore, Style


def trocar_valores(a, b):
    aux = a
    a = b
    b = aux
    return a, b


def main():
    while True:
        try:
            valor_a = int(input('Valor de A: '))
            valor_b = int(input('Valor de B: '))
            
            if valor_a <= 0 and valor_b <= 0:
                raise ValueError(f'{Fore.RED}{Style.BRIGHT}'
                                 f'As variáveis A e B devem ser maiores que 0.'
                                 f'{Fore.RESET}{Style.RESET_ALL}')
            else:
                print(f'\nValor original de A: {valor_a}')
                print(f'valor original de B: {valor_b}')
                
                valor_a, valor_b = trocar_valores(valor_a, valor_b)
                
                print(f'Valor da variável [A] trocado: {valor_a}')
                print(f'Valor da variável [B] trocado: {valor_b}')
                break
        
        except ValueError as error:
            print(f'{Fore.RED}{Style.BRIGHT}Erro: {error}{Fore.RESET}{Style.RESET_ALL}')


if __name__ == '__main__':
    main()


# a = 1
# b = 2
#
# aux = a
# a = b
# b = aux
# print('Valor de a: ', a)
# print('Valor de B: ', b)
