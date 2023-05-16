# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo.
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo


def calcular_produto_dobro_metade(num1, num2):
    return (2 * num1) * (num2 / 2)


def calcular_soma_tiplo(num1, num2):
    return (3 * num1) + num2


def calcular_cubo(num):
    return num ** 3


def ler_numero_inteiro(mensagem):
    while True:
        try:
            num = int(input(mensagem))
            return num
        except ValueError:
            print('Valor inválido. Digite um número inteiro válido.')


def ler_numero_real(mensagem):
    while True:
        try:
            num = float(input(mensagem))
            return num
        except ValueError:
            print('Valor inválido. Digite um número inteiro válido.')
            

def main():
    inteiro1 = ler_numero_inteiro('Digite o primeiro intiero: ')
    inteiro2 = ler_numero_inteiro('Digite o segundo inteiro: ')
    numero_real = ler_numero_real('Digite o número REAL')

    # calculo dos resultados
    produto = calcular_produto_dobro_metade(inteiro1, inteiro2)
    soma = calcular_soma_tiplo(inteiro1, numero_real)
    cubo = calcular_cubo(numero_real)
    
    print(f'O produto do dobro do primeiro com metade do segundo é:{produto}')
    print(f'A soma do triplo do primeiro com o terceiro é: {soma}')
    print(f'O terceiro número elevado ao cubo é: {cubo}')
    
    
if __name__ == '__main__':
    main()
    