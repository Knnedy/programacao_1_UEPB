# Faça um Programa que converta metros para centímetros

from colorama import Fore, Style


def converter_metros_para_cm(metros):
    centimetros = metros * 100
    return centimetros


def main():
    while True:
        try:
            metro = float(input('Quantos metros deseja coverter para centimetros: '))
            if metro <= 0:
                raise ValueError(f'{Fore.RED}{Style.BRIGHT}'
                                 f'Entrada inválida. Digite um valor numérico.'
                                 f'{Fore.RESET}{Style.RESET_ALL}')
            break
        except ValueError as error:
            print(f'{Fore.RED}{Style.BRIGHT}Error: {error}{Fore.RED}{Style.RESET_ALL}')
            print(f'{Fore.RED}{Style.BRIGHT}Tente novamente{Fore.RED}{Style.RESET_ALL}')
            
    converter_metros = converter_metros_para_cm(metro)
    print('{:.2f} metro(s) convertido(s) para centimentro(s) é igual a: {:.2f}'
          .format(metro, converter_metros))
    
    
if __name__ == '__main__':
    main()
    