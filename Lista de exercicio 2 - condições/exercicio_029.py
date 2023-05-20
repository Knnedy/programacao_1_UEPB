# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
# e lhe contrataram para desenvolver o programa que calculará os reajustes. Faça um
# programa que recebe o salário de um colaborador e o reajuste segundo o seguinte
# critério, baseado no salário atual:

# salários até R$ 280,00 (incluindo): aumento de 20%
# salários entre R$ 280,00 e R$ 700,00: aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00: aumento de 10%

# salários de R$ 1500,00 em diante: aumento de 5%.
# Após o aumento ser realizado, informe na tela:

# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.


def calcular_aumento_salarial(salario_atual):
    if salario_atual <= 280:
        percentual_aumento = 20
    elif salario_atual <= 700:
        percentual_aumento = 15
    elif salario_atual <= 1500:
        percentual_aumento = 10
    else:
        percentual_aumento = 5
    
    valor_aumento = salario_atual * (percentual_aumento / 100)
    novo_salario = salario_atual + valor_aumento
    
    return percentual_aumento, valor_aumento, novo_salario


def main():
    while True:
        try:
            salario_sem_reajuste = float(input('Salário atual do funcionário: R$ '))
            if salario_sem_reajuste <= 0:
                raise ValueError('Entrada inválida. O salário deve ser maior que 0.')
            
            percentual, aumento, novo_salario = calcular_aumento_salarial(
                salario_sem_reajuste)
            print(f'Salario sem aumento: R${salario_sem_reajuste:.2f}')
            print(f'Percentual de aumento aplicado: {percentual}%')
            print(f'Valor do aumento R$ {aumento:.2f}')
            print(f'Novo salário após reajuste: R$ {novo_salario:.2f}')
            break
        except ValueError as e:
            print(f'Error: {e}')


if __name__ == '__main__':
    main()
