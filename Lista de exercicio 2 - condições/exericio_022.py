# Faça um Programa que peça dois números e imprima o maior deles.

from colorama import Fore, Style


def calcular_maior_numero(num1, num2):
    if num1 > num2:
        return f'\nO maior é: {num1}'
    elif num2 > num1:
        return f'\nO maior é: {num2}'
    else:
        return '\nOs dois são iguais'
    
    
def main():
    while True:
        try:
            n1 = int(input('Número 1: '))
            n2 = int(input('Número 2: '))
            if n1 < 0 and n2 < 0:
                raise ValueError(f'{Fore.RED}{Style.BRIGHT}'
                                 f'Digite um numero maior ou igual a 0'
                                 f'{Fore.RED}{Style.BRIGHT}')
            else:
                maior_numero = calcular_maior_numero(n1, n2)
                
                print(f'{maior_numero}')
                break
        
        except ValueError as error:
            print(f'{Fore.RED}{Style.BRIGHT}Erro: {error}{Fore.RESET}{Style.RESET_ALL}')
            
    
if __name__ == '__main__':
    main()
    