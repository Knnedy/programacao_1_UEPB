# Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de
# vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha
# 15% de comissão sobre suas vendas efetuadas, informar o seu nome, o salário fixo e
# salário no final do mês.

from colorama import Fore, Style


def calcular_comissao(total_vendas):
    return total_vendas * 0.15  # 15% de comissão sobre as vendas


def calcular_salario_final(salario_fixo, comissao):
    return salario_fixo + comissao


def ler_dados_vendedor():
    while True:
        try:
            nome_vendedor = input("Digite o nome do vendedor: ")
            salario_fixo = float(input("Digite o salário fixo do vendedor: "))
            total_vendas = int(input("Digite o total de vendas efetuadas no mês: "))
            
            if salario_fixo < 0 or total_vendas < 0:
                raise ValueError(
                    f'{Fore.RED}{Style.BRIGHT}'
                    f'O salário fixo e o total de vendas devem maior que 0.'
                    f'{Fore.RESET}{Style.RESET_ALL}')
            
            return nome_vendedor, salario_fixo, total_vendas
        except ValueError as error:
            print(f'{Fore.RED}{Style.BRIGHT}Error: {error}{Fore.RED}{Style.RESET_ALL}')
            print(f'{Fore.RED}{Style.BRIGHT}Tente novamente{Fore.RED}{Style.RESET_ALL}')


def exibir_resultado(nome_vendedor, salario_fixo, salario_final):
    print('Nome do vendedor:', nome_vendedor)
    print('Salário fixo: R${:.2f}'.format(salario_fixo))
    print("Salário no final do mês: R${:.2f}".format(salario_final))

    
def main():
    try:
        nome_vendedor, salario_fixo, total_vendas = ler_dados_vendedor()
        comissao = calcular_comissao(total_vendas)
        salario_final = calcular_salario_final(salario_fixo, comissao)
        exibir_resultado(nome_vendedor, salario_fixo, salario_final)
    except KeyboardInterrupt:
        print('\nPrograma interrompido pelo usuário!')
        
        
if __name__ == '__main__':
    main()
    