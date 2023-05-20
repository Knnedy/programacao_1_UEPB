# Faça um programa que pergunte o preço de três produtos e informe qual produto você
# deve comprar, sabendo que a decisão é sempre pelo mais barato.


def obter_dados_produto(numero_produto):
    while True:
        nome_produto = input(f'Digite o nome do produto {numero_produto}: ')
        if not nome_produto.isalpha():
            print('Nome do produto inválido. Digite apenas letras.')
        else:
            while True:
                try:
                    preco_prod = float(input(f'Digite o preco do produto '
                                             f'{nome_produto}: '))
                    print()
                    if preco_prod < 0:
                        raise ValueError('O preço não pode ser negativo.')
                    return nome_produto, preco_prod
                except ValueError as e:
                    print(f'Entrada inválida: {e}')
                
      
def encontrar_produto_mais_barato():
    numero_produtos = 3
    produtos = []
    
    for i in range(numero_produtos):
        nome_produto, preco_produto = obter_dados_produto(i + 1)
        produtos.append((nome_produto, preco_produto))
    
    menor_preco = produtos[0][1]
    for produto in produtos:
        if produto[1] < menor_preco:
            menor_preco = produto[1]
        
    produto_mais_barato = []
    for produto in produtos:
        if produto[1] == menor_preco:
            produto_mais_barato.append(produto[0])
            
    return produto_mais_barato


def main():
    prod_mais_baratos = encontrar_produto_mais_barato()
    if len(prod_mais_baratos) == 1:
        print(f'O produto mais barato é: {prod_mais_baratos[0]}\n')
        

if __name__ == '__main__':
    main()
