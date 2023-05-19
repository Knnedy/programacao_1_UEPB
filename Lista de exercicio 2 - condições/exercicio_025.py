# Faça um programa para a leitura de duas notas parciais de um aluno. O programa
# deve calcular a média alcançada por aluno e apresentar:

# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

from colorama import Fore, Style


def calcular_media_aluno(nota1, nota2):
    media_aluno = (nota1 + nota2) / 2
    return media_aluno


def situacao_aluno(media_aluno):
    if media_aluno == 10:
        const_situacao_aluno = f'{Fore.GREEN}{Style.BRIGHT}' \
                               f'Aprovado com Distinção!' \
                               f'{Fore.RESET}{Style.RESET_ALL}'
    elif media_aluno >= 7:
        const_situacao_aluno = f'{Fore.GREEN}{Style.BRIGHT}' \
                               f'Aprovado!' \
                               f'{Fore.RESET}{Style.RESET_ALL}'
    else:
        const_situacao_aluno = f'{Fore.RED}{Style.BRIGHT}' \
                               f'Reprovado!' \
                               f'{Fore.RESET}{Style.RESET_ALL}'
    return const_situacao_aluno
    
    
def main():
    while True:
        try:
            nota_1 = float(input('Digite a primeira nota do aluno: '))
            if nota_1 < 0 or nota_1 > 10:
                raise ValueError(f'{Fore.RED}{Style.BRIGHT}'
                                 f'Entrada inválida. Digite um valor numérico entre'
                                 f' 0 e 10'
                                 f'{Fore.RESET}{Style.RESET_ALL}')
            nota_2 = float(input('Digite a segunda nota do aluno: '))
            if nota_2 < 0 or nota_2 > 10:
                raise ValueError(f'{Fore.RED}{Style.BRIGHT}'
                                 f'Entrada inválida. Digite um valor numérico entre'
                                 f' 0 e 10'
                                 f'{Fore.RESET}{Style.RESET_ALL}')
            
            media = calcular_media_aluno(nota_1, nota_2,)
            status_aluno = situacao_aluno(media)
            
            print(f'\nA média do aluno é: {media:.1f}')
            print(f'{status_aluno}')
            break
        except ValueError as error:
            print(f'{Fore.RED}{Style.BRIGHT}Erro:{error}{Fore.RESET}{Style.RESET_ALL}')


if __name__ == '__main__':
    main()
    