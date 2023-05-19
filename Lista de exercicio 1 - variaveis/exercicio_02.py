# Faça um Programa que peça dois números e imprima a soma

from colorama import Fore, Style


def calcular_soma_numeros():
    lista_numerica = []
    soma = 0
    
    for i in range(2):
        while True:
            try:
                num = int(input('Digite o número: '))
                lista_numerica.append(num)
                soma += num
                break
            except ValueError:
                print(f'{Fore.RED}{Style.BRIGHT}'
                      f'Entrada inválida. Digite um número inteiro.'
                      f'{Fore.RESET}{Style.RESET_ALL}')
    
    return lista_numerica, soma


def main():
    lista_numerica, soma = calcular_soma_numeros()
    print(f'A Soma de {lista_numerica[0]} e {lista_numerica[1]} é: {soma}')
  
        
if __name__ == '__main__':
    main()
    