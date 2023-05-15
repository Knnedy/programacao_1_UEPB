# Faça um Programa que calcule a área de um quadrado, em
# seguida mostre o dobro desta área para o usuário.

def quadrado(lado):
    area = lado ** 2
    return area


lado_quadrado = int(input('Digite o lado do quadrado: '))
area_quadrado = quadrado(lado_quadrado)
print(f'A área do quadrado é: {area_quadrado:.2f}')
