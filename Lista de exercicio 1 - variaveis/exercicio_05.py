import math

# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.


def calcular_area_circulo(raio):
    area = math.pi * raio ** 2
    return area


def calcular_circunferencia(raio):
    circunferencia = 2 * math.pi * raio
    return circunferencia


def calcular_diametro(raio):
    diametro = 2 * raio
    return diametro


raio_circulo = float(input('Digite o raio do círculo: '))

area_circulo = calcular_area_circulo(raio_circulo)
circunferencia_circulo = calcular_circunferencia(raio_circulo)
diametro_circulo = calcular_diametro(raio_circulo)

print(f'A área do círculo é: {raio_circulo:.2f}'
      f'\nA circunferência é: {circunferencia_circulo:.2f}'
      f'\nO diâmetro é: {diametro_circulo:.2f}')
