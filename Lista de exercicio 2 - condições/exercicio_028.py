# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou
# V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
# ou "Valor Inválido!", conforme o caso.

def verificar_horario_estudos(turno_escola):
    if turno_escola == 'm':
        return 'Bom dia'
    elif turno_escola == 'v':
        return 'Boa tarde'
    elif turno_escola == 'n':
        return 'Boa noite'
   

def main():
    while True:
        try:
            horario_estudos = input('Em que turno voce estuda: '
                                    '[M]atutino, [V]erpertino ou [N]oturno?').lower()
            if not horario_estudos.isalpha():
                raise ValueError('Entrada inválida, digite apenas letras.')
            
            turno = verificar_horario_estudos(horario_estudos)
            print(turno)
            break
        except ValueError as e:
            print(f'Error: {e}')


if __name__ == '__main__':
    main()
