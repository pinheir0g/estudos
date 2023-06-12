# Programa para calcular descontos em produtos, conforme mais produtos adquirir mais desconto ganha

aluno = "Gustavo Viana Pinheiro"

print(f"Bem vindo ao Atacadão do {aluno}")
try:  # Try para tratar erro caso seja digitado um valor não numérico.

    # Recebe o valor do produto.
    valor = float(input('Valor do Produto: '))

    # Recebe a quantidade de produtos.
    quant = int(input('Quantidade: '))

    # Calcula o valor total a ser pago.
    total = valor * quant
    print(f'Valor do produto sem desconto: R$ {total:.2f}')

    # Verifica se esta entre 10 e 99.
    if 10 <= quant <= 99:
        # Calcula desconto de 5%.
        desconto = total * 0.05

        # Aplica desconto.
        novo_valor = total - desconto
        print(f'Valor com desconto: R$ {novo_valor:.2f} (5% de desconto)')

    # Verifica se esta entre 100 e 999.
    elif 100 <= quant <= 999:
        desconto = total * 0.1
        novo_valor = total - desconto
        print(f'Valor com desconto: R$ {novo_valor:.2f} (10% de desconto)')

    # Verifica se esta acima de 1000.
    elif quant >= 1000:
        desconto = total * 0.15
        novo_valor = total - desconto
        print(f'Valor com desconto: R$ {novo_valor:.2f} (15% de desconto)')
    else:
        print(f'Valor com desconto: R$ {total:.2f} (quantidade mínima para descontos não atingida)')
except ValueError:
    print('Foi inserido um valor não numérico')
