# Faça um algoritmo que receba um valor que foi depositado e exiba o valor com
# rendimento após um mês. Considere fixo o juro da poupança em 0,70% a. m.

from colorama import Fore, Style


def calcular_rendimento(valor_depositado):
    juro_poupanca = 0.0070
    dias_no_mes = 30
    rendimento = valor_depositado * juro_poupanca * dias_no_mes
    return rendimento


def calcular_valor_total(valor_depositado):
    rendimento = calcular_rendimento(valor_depositado)
    valor_total = valor_depositado + rendimento
    return valor_total


def main():
    while True:
        try:
            valor_do_deposito = float(input('Digite o valor depositado: '))
            if valor_do_deposito <= 0:
                raise ValueError(f'{Fore.RED}{Style.BRIGHT}O valor deve ser maior que '
                                 f'zero.{Fore.RESET}{Style.RESET_ALL}')
            break
        except ValueError as error:
            print(f'{Fore.RED}{Style.BRIGHT}Erro: {error}{Fore.RESET}{Style.RESET_ALL}')
            print('Tente novamente.\n')
    
    valor_total = calcular_valor_total(valor_do_deposito)
    print(f'O valor total após um mês é de {Fore.GREEN}{Style.BRIGHT}R$ {round(valor_total, 2)}'
          f'{Fore.RESET}{Style.RESET_ALL}')
    

if __name__ == '__main__':
    main()
    