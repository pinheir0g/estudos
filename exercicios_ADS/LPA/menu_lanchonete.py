# Menu de uma lanchonete, onde o usuário consegue realizar pedidos.
aluno = "Gustavo Viana Pinheiro"

# Lista de produtos e preços
produtos = [
    {'codigo': 100, 'prod': 'Cachorro-Quente', 'valor': 9},
    {'codigo': 101, 'prod': 'Cachorro-Quente-Duplo', 'valor': 11},
    {'codigo': 102, 'prod': 'X-Egg', 'valor': 12},
    {'codigo': 103, 'prod': 'X-Salada', 'valor': 13},
    {'codigo': 104, 'prod': 'X-Bacon', 'valor': 14},
    {'codigo': 105, 'prod': 'X-Tudo', 'valor': 17},
    {'codigo': 200, 'prod': 'Refrigerante Lata', 'valor': 5},
    {'codigo': 201, 'prod': 'Chá Gelado', 'valor': 4},
]

print(f"Bem vindo a Lanchonete do {aluno}")
print('=' * 43)
print(f'{"Cardápio":^43}')
print('=' * 43)
print("""
| Código |       Descrição        | Valor |
|  100   |    Cachorro Quente     |  9,00 |
|  101   |  Cachorro quente Duplo | 11,00 |
|  102   |          X-Egg         | 12,00 |
|  103   |       X-Salada         | 13,00 |
|  104   |        X-Bacon         | 14,00 |
|  105   |        X-Tudo          | 17,00 |
|  200   |    Refrigerante Lata   |  5,00 |
|  201   |      Chá Gelado        |  4,00 |
""")
tot = 0  # Variavel para calcular o total do preço.

while True:
    try:  # Try para tratar erro caso seja digitado um valor não numérico.1

        # Recebe o codigo do produto.
        cd = int(input('Código do Produto desejado: '))

        # Itera sobre a lista dos itens.
        for prod in produtos:
            # Verifica se existe o código digitado.
            if cd == prod['codigo']:
                print(f'Você pediu um {prod["prod"]} no valor de R$ {prod["valor"]:.2f}')
                tot += prod["valor"]  # Calculo do valor total.
                break
        else:
            print('Opção inválida!')
            continue

    except ValueError:
        print('Apenas números são aceitos')
        continue

    while True:
        # While para ver se usuário quer mais alguma coisa com tratamento se digitar errado.
        print('Deseja mais alguma coisa?')
        print('1 - Sim')
        print('0 - Não')
        op = int(input())
        if op == 0:
            break
        elif op == 1:
            break
        else:
            print('Opção inválida')
    # Encerra o programa caso o usuário não queira mais nada.
    if op == 0:
        print(f'Total a ser pago: R$ {tot:.2f}')
        break
