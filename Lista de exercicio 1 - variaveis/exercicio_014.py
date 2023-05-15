# Escrever um algoritmo para determinar o consumo médio de um automóvel sendo fornecida
# a distância total percorrida pelo automóvel e o total de combustível gasto.

from colorama import Fore, Style


def obter_consumo_medio(distancia, combustivel):
    consumo_medio_combustivel = distancia / combustivel
    return consumo_medio_combustivel


def main():
    while True:
        try:
            distancia_percorrida = float(input('Informe a distância percorrida em Km: '))
            combustivel_gasto = float(input('Informe o total gasto de combustível: '))
            if distancia_percorrida <= 0:
                raise ValueError(f'{Fore.RED}{Style.BRIGHT}O valor total da compra deve'
                                 f'ser maior que zero.{Fore.RESET}{Style.RESET_ALL}')
            break
        except ValueError as error:
            print(f'{Fore.RED}{Style.BRIGHT}Erro: {error}{Fore.RESET}{Style.RESET_ALL}')
            print('Tente novamente.\n')
    
    total_consumo_medio = obter_consumo_medio(distancia_percorrida, combustivel_gasto)
    print(f'O consumo médio do automóvel é de: {total_consumo_medio:.2f} litros por Km'
          f' percorrido.')
    
    
if __name__ == '__main__':
    main()
    