# Elaborar um algoritmo que efetue a apresentação do valor da conversão em real (R$) de
# um valor lido em dólar (US$). O algoritmo deverá solicitar o valor da cotação do dólar
# e também a quantidade de dólares disponíveis com o usuário.

from colorama import Fore, Style


def obter_cotacao():
    while True:
        cotacao = input('Cotação do dólar hoje: ')
        try:
            cotacao = float(cotacao)
            return cotacao
        except ValueError:
            print(f'{Fore.RED}{Style.BRIGHT}Por favor, digite um valor válido para a cotação '
                  f'do dólar.{Fore.RESET}{Style.RESET_ALL}')


def obter_qtd_dolares():
    while True:
        dolares = input('Dólares (U$) disponiveis para converter em reais: (R$) ')
        try:
            dolares = float(dolares)
            return dolares
        except ValueError:
            print(f'{Fore.RED}{Style.BRIGHT}Por favor, digite um valor válido para a quantidade de '
                  f'dólares.{Fore.RESET}{Style.RESET_ALL}')

        
def converter_dolares_para_reais(cotacao, dolares):
    valor_em_reais = cotacao * dolares
    return valor_em_reais


def exibir_valor_convertido(valor_em_reais):
    print(f'O valor correspondente em reais é {Fore.GREEN}{Style.BRIGHT}R$ {valor_em_reais:.2f}'
          f'{Fore.RESET}{Style.RESET_ALL}')


def main():
    cotacao_hoje = obter_cotacao()
    quantia_dolares = obter_qtd_dolares()
    quantia_em_reais = converter_dolares_para_reais(cotacao_hoje, quantia_dolares)
    exibir_valor_convertido(quantia_em_reais)


if __name__ == '__main__':
    main()

