# Faça um Programa que verifique se uma letra digitada é
# "F" ou "M". Conforme a letra:
# F - Feminino, M - Masculino, Sexo Inválido.

from colorama import Fore, Style


def autenticacao_sexo(auth_sexo):
    if auth_sexo == 'm':
        return 'Sexo Masculino.'
    elif auth_sexo == 'f':
        return 'Sexo Feminino.'
    else:
        return 'Sexo Inválido.'


def main():
    while True:
        try:
            sexo = str(input('Digite seu sexo, [M]asculino ou [F]eminino: ')).lower()
            if not sexo.isalpha():
                raise ValueError(f'{Fore.RED} {Style.BRIGHT}Digite apenas letras.'
                                 f'{Fore.RESET}{Style.RESET_ALL}')
            break
        except ValueError as error:
            print(f'{Fore.RED}{Style.BRIGHT}Erro:{error}{Fore.RESET}{Style.RESET_ALL}')

    autenticar_sexo = autenticacao_sexo(sexo)
    print(f'{autenticar_sexo}')
    

if __name__ == '__main__':
    main()
    