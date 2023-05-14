# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.


def obter_valor_hora():
    salario_hora = float(input('Valor ganho por hora: R$'))
    return salario_hora


def obter_horas_trabalhadas():
    horas_de_trabalho = float(input('Número de horas trabalhadas este mês: '))
    return horas_de_trabalho


def calcular_salario_mensal(salario_hora, horas_de_trabalho):
    salario_mensal = salario_hora * horas_de_trabalho
    return salario_mensal


def exibir_salario_mensal(salario_mensal):
    print(f'O seu salário mensal é R${salario_mensal:.2f}')
    
    
def main():
    valor_hora = obter_valor_hora()
    horas_de_trabalho = obter_horas_trabalhadas()
    salario_mensal = calcular_salario_mensal(valor_hora, horas_de_trabalho)
    exibir_salario_mensal(salario_mensal)
    
    
main()
