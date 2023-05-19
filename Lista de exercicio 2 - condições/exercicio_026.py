# Faça um Programa que leia três números e mostre o maior deles.


def encontrar_maior_numero():
    while True:
        try:
            a = float(input('digite o primeiro número: '))
            b = float(input('digite o segundo número: '))
            c = float(input('Digite o terceiro número: '))
            
            maior = a
            if b > maior:
                maior = b
            if c > maior:
                maior = c
            
            print(f'O maior número é: {maior}')
            break
        except ValueError:
            print('Entrada inválida, Digite apenas números.')
            

def main():
    encontrar_maior_numero()
    
    
if __name__ == '__main__':
    main()
    