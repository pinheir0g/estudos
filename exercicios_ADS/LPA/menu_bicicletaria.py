# Estoque de uma biciletaria, usuário consegue ver, adicionar, editar e remover um item no estoque

def cadastrar_peca(codigo):
    """
    Função para cadastrar uma peça e armazenar numa lista de dicionários;
    :param codigo: Contador para adicionar um novo código para cada peça;
    :return Lista de dicionários com os dados das peças
    """
    pecas = {}  # Dicionário com os dados das peças
    nome = input('Nome da peça: ')
    fabricante = input('Fabricante da peça: ')
    valor = float(input('Valor da peça: '))

    # Adiciona as informações no dicionário
    pecas['codigo'] = codigo
    pecas['nome'] = nome
    pecas['fabricante'] = fabricante
    pecas['valor'] = valor
    # Adiciona os dicionários criados em uma lista
    return lista_produtos.append(pecas)


def consultar_peca():
    """
    Função para consultar as peças cadastradas na lista de produtos;
    :return Peças cadastradas
    """
    while True:
        print("""Escolha a opção desejada:
1 - Consultar Todas as Peças
2 - Consultar peças por Código
3 - Consultar Peças por Fabricante
4 - Retornar""")
        try:  # Try para tratar caso não seja recebido valores numéricos
            print('=' * 45)
            opcao = int(input('>> '))
            # Verifica qual a opção escolhida
            if opcao == 1:
                print('-' * 25)
                # Itera a lista de produtos e exibe todas as peças encontradas
                for pecas in lista_produtos:
                    for k, v in pecas.items():
                        print(f'{k}: {v}')
                    print('-'*25)
            elif opcao == 2:
                codigo = int(input('Digite o Código da Peça: '))
                print('-' * 25)
                # Itera a lista de produtos e exibe a peça selecionada por código
                for pecas in lista_produtos:
                    if codigo == pecas['codigo']:
                        for k, v in pecas.items():
                            print(f'{k}: {v}')
                        print('-'*25)
            elif opcao == 3:
                fabri = input('Digite o Fabricante da Peça: ')
                print('-'*25)
                # Itera a lista de produtos e exibe a peça selecionada pelo fabricante
                for pecas in lista_produtos:
                    if fabri == pecas['fabricante']:
                        for k, v in pecas.items():
                            print(f'{k}: {v}')
                        print('-'*25)
            elif opcao == 4:
                break
            else:
                print('Opção inválida!')
        except ValueError:
            print('Apenas números são aceitos!')


def remover_peca():
    """
    Função para removar uma peça cadastrada na lista
    """
    while True:
        try:  # Try para tratar caso não seja recebido valores numéricos
            codigo = int(input('Digite o código da peça a ser excluida: '))
            # Itera a lista de produtos e remove a selecionada pelo código
            for pecas in lista_produtos:
                if codigo == pecas['codigo']:
                    lista_produtos.remove(pecas)
                    print('Peça excluida com sucesso!')
                    break
            else:
                print('Código não encontrado')
            break
        except ValueError:
            print('Apenas números são aceitos')


lista_produtos = []  # variavel com a lista de produtos
codigo_produto = 0  # variavel contadora, para criar um código de cada produto

# Programa Principal

print('Bem vindo a Bicicletaria do Gustavo Viana Pinheiro')

while True:
    print('=' * 45)
    print("""Escolha a opção desejada: 
1 - Cadastrar peça
2 - Consultar peça
3 - Remover peça
4 - Sair""")
    try:
        print('=' * 45)
        op = int(input('>> '))
        # Verifica qual opção escolhida
        if op == 1:
            print('Você selecionou a opção Cadastrar Peça')
            print('=' * 45)
            codigo_produto += 1
            print(f'Código da Peça: {codigo_produto}')
            cadastrar_peca(codigo_produto)
        elif op == 2:
            print('Você selecionou a opção Consultar Peças')
            print('=' * 45)
            consultar_peca()
        elif op == 3:
            print('Você selecionou a opção Remover Peça')
            print('=' * 45)
            remover_peca()
        elif op == 4:
            break
        else:
            print('Opção inválida!')
    except ValueError:
        print('Apenas números são aceitos!')
