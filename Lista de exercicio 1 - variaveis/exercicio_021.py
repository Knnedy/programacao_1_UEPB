# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
# no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são
# descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um
# programa que nos dê:

#     a) salário bruto.
#     b) quanto pagou ao INSS.
#     c) quanto pagou ao sindicato.
#     d) o salário líquido.
#     e) calcule os descontos e o salário líquido, conforme a tabela abaixo:<br>
#         Salário Bruto : R$IR (11%) : R$INSS (8%) : R$S
#         Sindicato ( 5%) : R$ <br>
#         Salário Liquido : R$ <br>
# Obs.: Salário Bruto - Descontos = Salário Líquido.

from colorama import Fore, Style


def calcular_salario_bruto(sal_hora, hrs_mensais):
    return sal_hora * hrs_mensais
    

def calcular_imposto_renda(salario_bruto):
    return salario_bruto * 0.11


def calcular_desconto_sindicato(salario_bruto):
    return salario_bruto * 0.05
    

def calcular_inss(salario_bruto):
    return salario_bruto * 0.08


def calcular_salario_liquido(salario_bruto, imposto_renda, inss, sindicato):
    return salario_bruto - imposto_renda - inss - sindicato


def main():
    while True:
        try:
            salario_hora = float(input('Salário por hora: R$'))
            horas_mensais = float(input('Horas mensais: '))
        
            if salario_hora <= 0 and horas_mensais <= 0:
                raise ValueError(f'{Fore.RED}{Style.BRIGHT}O salário por hora e as horas '
                                 f'mensais devem ser maiores que 0'
                                 f'{Fore.RED}{Style.BRIGHT}')
            else:
                salario_bruto = calcular_salario_bruto(salario_hora, horas_mensais)
                desconto_imposto_renda = calcular_imposto_renda(salario_bruto)
                desconto_inss = calcular_inss(salario_bruto)
                desconto_sindicato = calcular_desconto_sindicato(salario_bruto)
                salario_liquido = calcular_salario_liquido(salario_bruto,
                                                           desconto_imposto_renda,
                                                           desconto_inss,
                                                           desconto_sindicato)
                
                print(f'Salário Bruto         : R${salario_bruto:.2f}')
                print(f'IR (11%)              : R${desconto_imposto_renda:.2f}')
                print(f'INSS (8%)             : R${desconto_inss:.2f}')
                print(f'Sindicato (5%)        : R${desconto_sindicato:.2f}')
                print('----------------------------------')
                print(f'SALÁRIO LIQUIDO       : R${salario_liquido:.2f}')
                break
            
        except ValueError as error:
            print(f'{Fore.RED}{Style.BRIGHT}Erro: {error}{Fore.RESET}{Style.RESET_ALL}')
    

if __name__ == '__main__':
    main()
    