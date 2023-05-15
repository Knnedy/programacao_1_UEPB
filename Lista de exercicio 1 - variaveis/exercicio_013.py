# Faça um algoritmo que receba o preço de custo de um produto e mostre o valor de
# venda. Sabe-se que o preço de custo receberá um acréscimo de acordo com um
# percentual informado pelo usuário

from colorama import Fore, Style


def calcular_valor_venda(custo_produto, percent_acrescimo):
    valor_venda = custo_produto * (1 + percent_acrescimo / 100)
    return valor_venda


def main():
    while True:
        try:
            preco_custo = float(input('Digite o preço de custo do produto: '))
            percentual_acrescimo = float(input('Digite o percentual de acréscimo '
                                               'desejado: '))
            if preco_custo <= 0:
                raise ValueError(f'{Fore.RED}{Style.BRIGHT}O valor total da compra deve'
                                 f'ser maior que zero.{Fore.RESET}{Style.RESET_ALL}')
            break
        except ValueError as error:
            print(f'{Fore.RED}{Style.BRIGHT}Erro: {error}{Fore.RESET}{Style.RESET_ALL}')
            print('Tente novamente.\n')
    
    valor_final_produto = calcular_valor_venda(preco_custo, percentual_acrescimo)
    print(f'O valor de venda é: {Fore.GREEN}{Style.BRIGHT}R${valor_final_produto:.2f}'
          f'{Fore.RESET}{Style.RESET_ALL}')
    
    
if __name__ == '__main__':
    main()
    