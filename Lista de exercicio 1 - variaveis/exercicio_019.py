# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a
# velocidade de um link de Internet (em MBps), calcule e informe o tempo aproximado de
# download do arquivo usando este link (em minutos).

from colorama import Fore, Style


def calcular_tempo_download(tamanho_arquivo, velocidade_internet):
    download_segundos = tamanho_arquivo / velocidade_internet
    download_minutos = download_segundos / 60
    return download_minutos


def main():
    while True:
        try:
            tam_arquivo = float( input('Tamanho do arquivo (em megabytes MB) a '
                                       'converter: '))
            vel_internet = float(input('Velocidade do download em megabytes por '
                                       'segundo (MBps)'))
            
            if tam_arquivo <= 0 and vel_internet <= 0:
                raise ValueError('Tamanho do arquivo e velocidade da Internet devem ser '
                                 'maiores que zero.')
            else:
                download_em_minutos = calcular_tempo_download(tam_arquivo, vel_internet)
                print(f'O tempo aproximado de download é de: {download_em_minutos:.2f}')
                break
        
        except ValueError as error:
            print(f'{Fore.RED}{Style.BRIGHT}Erro: {error}{Fore.RESET}{Style.RESET_ALL}')


if __name__ == '__main__':
    main()

# tamanho_arquivo = float(input('Tamanho do arquivo (em megabytes MB) a converter: '))
# vel_download = float(input('Velocidade do download em megabytes por segundo (MBps)'))
#
# tempo_download_segundos = tamanho_arquivo / vel_download
# tempo_download_minutos = tempo_download_segundos / 60
#
# print(f'O tempo aproximado de download é de {tempo_download_minutos:.2f} minutos.')
