from colorama import Fore, Style

# A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações sem juros.
# Faça um algoritmo que receba um valor de uma compra e mostre o valor das prestações.


def calcular_valor_prestacao(valor_total):
    valor_prestacao = valor_total / 5
    return valor_prestacao


def exibir_valor_prestacao(valor_prestacao):
    print(f'Cada prestação terá o valor de {Fore.GREEN}{Style.BRIGHT}'
          f'R${valor_prestacao:.2f}{Fore.RESET}{Style.RESET_ALL}')


def main():
    while True:
        try:
            valor_compra = float(input('Digite o valor total da compra: '))
            if valor_compra <= 0:
                raise ValueError(f'{Fore.RED}{Style.BRIGHT}O valor total da compra deve'
                                 f'ser maior que zero.{Fore.RESET}{Style.RESET_ALL}')
            break
        except ValueError as error:
            print(f'{Fore.RED}{Style.BRIGHT}Erro: {error}{Fore.RESET}{Style.RESET_ALL}')
            print('Tente novamente.\n')
            
    valor_parcela = calcular_valor_prestacao(valor_compra)
    exibir_valor_prestacao(valor_parcela)
    
    
if __name__ == '__main__':
    main()
    