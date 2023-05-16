# Escreva um programa que leia três números inteiros e positivos (A, B, C) e calcule
# seguinte expressão:
# D = (R + S) / 2
# onde
# R = (A + B)
# S = (B + C)

from colorama import Fore, Style


def calcular_d(a, b, c):
    r = a + b
    s = b + c
    d = (r + s) / 2
    return d


def main():
    while True:
        try:
            a = int(input("Digite o valor de A: "))
            b = int(input("Digite o valor de B: "))
            c = int(input("Digite o valor de C: "))
            if a < 0 and b < 0 and c < 0:
                raise ValueError(f'{Fore.RED} {Style.BRIGHT}Digite apenas números'
                                 f'positivos.{Fore.RESET}{Style.RESET_ALL}')
            break
        except ValueError as error:
            print(f'{Fore.RED} {Style.BRIGHT}Erro: {error} {Fore.RESET} {Style.RESET_ALL}')
            
    resultado = calcular_d(a, b, c)
    print(f'O resultado da expressão é: {resultado}')
    

if __name__ == '__main__':
    main()
    