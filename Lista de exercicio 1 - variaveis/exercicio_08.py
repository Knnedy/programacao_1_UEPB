# Faça um Programa que peça a temperatura em graus Farenheit,transforme e
# mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9)

def obter_temperatura_farenheit():
    f = float(input('Digite a temperatura em Farenheit: '))
    return f


def converter_farenheint_para_celsius(f):
    celsius = (5 * (f - 32) / 9)
    return celsius


def exibir_temperatura_convertida(celsius):
    print(f'Temperatura convertidada para Celsius: {celsius:.2f}')


def main():
    temp_farenheint = obter_temperatura_farenheit()
    temp_celsius = converter_farenheint_para_celsius(temp_farenheint)
    exibir_temperatura_convertida(temp_celsius)
    

main()
