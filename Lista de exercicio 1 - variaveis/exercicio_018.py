# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo
# que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) – 58.
from colorama import Fore, Style


def calcular_peso_ideal(altura):
    peso_ideal = (72.2 * altura) - 58
    return peso_ideal


def calcular_diferenca_peso(peso_atual, peso_ideal):
    peso_excedente = peso_atual - peso_ideal
    return peso_excedente
    

def main():
    while True:
        try:
            estatura = float(input('Informe sua estatura: '))
            peso_atual = float(input('Informe seu peso atual: '))
            if estatura <= 0 and peso_atual <= 0:
                raise ValueError(f'{Fore.RED} {Style.BRIGHT}Digite apenas números'
                                 f'positivos.{Fore.RESET}{Style.RESET_ALL}')
            break
        except ValueError as error:
            print(f'{Fore.RED}{Style.BRIGHT}Erro: {error}{Fore.RESET}{Style.RESET_ALL}')
            
    seu_peso_ideal = calcular_peso_ideal(estatura)
    diferenca_peso = calcular_diferenca_peso(peso_atual, seu_peso_ideal)
    
    print(f'O seu peso ideal é: {seu_peso_ideal:.2f}')
    print(f'Você está {Fore.RED}{Style.BRIGHT}{diferenca_peso:.2f}Kg'
          f'{Fore.RESET}{Style.RESET_ALL} acima do peso ideal.')
    

if __name__ == '__main__':
    main()
    