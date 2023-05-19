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
            numero1 = int(input('Número 1: '))
            numero2 = int(input('Número 2: '))
            if numero1 < 0 and numero2 < 0:
                raise ValueError(f'{Fore.RED}{Style.BRIGHT}'
                                 f'Digite um numero maior ou igual a 0'
                                 f'{Fore.RED}{Style.BRIGHT}')
            else:
                maior_numero = calcular_maior_numero(numero1, numero2)
                
                print(f'{maior_numero}')
                break
        
        except ValueError as error:
            print(f'{Fore.RED}{Style.BRIGHT}Erro: {error}{Fore.RESET}{Style.RESET_ALL}')
            
    
if __name__ == '__main__':
    main()
    