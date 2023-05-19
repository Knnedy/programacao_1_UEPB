# Faça um programa que pergunte o preço de três produtos e informe qual produto você
# deve comprar, sabendo que a decisão é sempre pelo mais barato.


def obter_preco_produto(nome_produto):
    while True:
        try:
            preco_prod = float(input(f'Digite o preço do {nome_produto}: '))
            if preco_prod <= 0:
                raise ValueError('Digite um valor maior que 0.')
            return preco_prod
        except ValueError:
            print('Entrada inválida, digite um valor numérico!')
            

def obter_nome_produto(numero_produto):
    return numero_produto


def encontrar_produto_mais_barato():
    nome_p1 = str(input('Digite o nome do produto 1: '))
    nome_p2 = str(input('Digite o nome do produto 2: '))
    nome_p3 = str(input('Digite o nome do produto 3: '))
    
    obter_nome_produto(nome_p1)
    obter_nome_produto(nome_p2)
    obter_nome_produto(nome_p3)
    
    preco_p1 = obter_preco_produto(nome_p1)
    preco_p2 = obter_preco_produto(nome_p2)
    preco_p3 = obter_preco_produto(nome_p3)

    if preco_p1 < preco_p2 and preco_p1 < preco_p3:
        return preco_p1
    elif preco_p2 < preco_p1 and preco_p2 < preco_p3:
        return preco_p2
    else:
        return preco_p3
    
    
def main():
    produto_mais_barato = encontrar_produto_mais_barato()
    print(f'O Produto mais barato custa: {produto_mais_barato}')
    
    
if __name__ == '__main__':
    main()
