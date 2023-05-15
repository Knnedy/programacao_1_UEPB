#  Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre
# em graus Fahrenheit.

def obter_temperatura_celsius():
    c = float(input('Digite a temperatura em Celsius: '))
    return c


def converter_celsius_para_fahrenheit(c):
    fahrenheit = (c * 9 / 5) + 32
    return fahrenheit


def exibir_temperatura_covertida(fahrenheit):
    print(f'Temperatura convertida para Fahrenheit: {fahrenheit:.2f}')
    
    
def main():
    temp_celsius = obter_temperatura_celsius()
    temp_fahrenheit = converter_celsius_para_fahrenheit(temp_celsius)
    exibir_temperatura_covertida(temp_fahrenheit)
    
    
main()
