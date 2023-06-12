# Programa de logistica, calcula o valor a ser pago pelo item enviado

def dimensoes_objeto():
    """
    Função para calcular a dimensão do objeto a ser enviado;
    :return valor para calcular o preço do envio.
    """
    valor = 0   # Inicia a variavel com o valor do objeto
    while True:
        print('=' * 44)
        try:    # Try para tratar erro ao receber valor não numérico
            # Recebe as informações do objeto
            altura = float(input('Altura do Objeto (em cm): '))
            comp = float(input('Comprimento do Objeto (em cm): '))
            largura = float(input('Largura do Objeto (em cm): '))

            # Calcula o volume do objeto
            volume = altura * comp * largura

            # Valida se o volume esta nas dimensões permitidas
            if volume < 1000:
                valor = 10
            elif 1000 <= volume < 10000:
                valor = 20
            elif 10000 <= volume < 30000:
                valor = 30
            elif 30000 <= volume < 100000:
                valor = 50
            else:
                print(f'O volume do objeto {volume} (em cm³)')
                print('Não é permitido dimensões acima ou igual a 100.000 cm³')
                print('Entre com as dimensões novamente')
                continue
            print(f'O volume do objeto {volume} (em cm³)')
            break
        except ValueError:
            print('Apenas valores numéricos são aceitos!')
            print('Entre com as dimensões novamente.')
    return valor


def peso_objeto():
    """
    Função para calcular o peso e o multiplicador do objeto a ser enviado;
    :return mutiplicador para calcular o preço do envio.
    """
    multi = 1  # Inicia a variavel com o valor do multiplicador
    while True:
        print('='*44)
        try:    # Try para tratar erro ao receber valor não numérico
            # Recebe o peso do obejto
            peso = float(input('Digite o peso do objeto (em kg): '))

            # Valida se o peso está no valor permitido
            if peso < 0.1:
                multi = 1
            elif 0.1 <= peso < 1:
                multi = 1.5
            elif 1 <= peso < 10:
                multi = 2
            elif 10 <= peso < 30:
                multi = 3
            else:
                print('Não aceitamos objetos acima ou igual a 30 kg')
                print('Entre com o peso novamente.')
                continue
            break
        except ValueError:
            print('Apenas valores numéricos são aceitos!')
            print('Entre com o peso novamente.')
    return multi


def rota_objeto():
    """
    Função para receber a rota e calcular o multiplicador do objeto a ser enviado;
    :return mutiplicador para calcular o preço do envio.
    """
    multi = 1  # Inicia a váriavel com o valor do multiplicador
    while True:
        print('='*44)
        print('Selecione a rota')
        print("""
BR - De Brasilia para Rio de Janeiro
BS - De Brasilia para São Paulo
RB - De Rio de Janeiro para Brasilia
RS - De Rio de Janeiro para São Paulo
SR - De São Paulo para Rio de Janeiro
SB - De São Paulo para Brasilia
""")
        # Recebe os dados da rota
        rota = str(input('>> ')).upper()

        # Valida se a rota recebida está nas rotas permitidas
        if rota in 'BR' or rota in 'RB':
            multi = 1.5
        elif rota in 'BS' or rota in 'SB':
            multi = 1.2
        elif rota in 'RS' or rota in 'SR':
            multi = 1
        else:
            print('Você digitou uma rota que não existe')
            continue
        break
    return multi


#  Programa principal
print('Bem vindo a Gustavo Viana Pinheiro Logistica')

d = dimensoes_objeto()  # Variável que recebe a função para calcular as dimensões
p = peso_objeto()   # Variável que recebe a função para calcular o peso
r = rota_objeto()   # Variável que recebe a função para calcular a rota

total = d * p * r   # Cálculo do valor total a ser pago

print('='*61)
print(f'Total a pagar: R$ {total:.2f} (dimensões: {d} * peso: {p} * rota: {r})')
print('='*61)
