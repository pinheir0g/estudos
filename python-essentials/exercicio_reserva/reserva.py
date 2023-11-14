"""
Faça um programa de terminal que exibe ao usuário uma lista dos quartos disponiveis para alugar e o preço de cada quarto, esta informação está disponível em um arquivo de texto separado por virgulas.

'quartos.txt'

# codigo, nome, preço
1,Suite Master,500
2,Quarto Familia,200
3,Quarto Single,100
4,Quarto Simples,50

O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado e a quantidade de dias e no final exive o valor estimado a ser pago.

O programa deve salvar esta escolha em outro arquivo contendo as reservas

`reservas.txt`
# cliente, quarto, dias
Mario,3,12

Se outro usuário tentar reservar o mesmo quarto o programa deve exibir uma mensagem informando que já esta reservado.

"""
import logging
import sys
import os

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("Alerta.py", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s  %(name)s  %(levelname)s'
    'l:%(lineno)d f:%(filename)s:  %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)

ocupados = {}
try:
    for line in open('exercicio_reserva/reservas.txt'):
        nome, num_quarto, dias = line.strip().split(',')
        ocupados[int(num_quarto)] = {
            "nome": nome, 
            "dias": dias
            }
except FileNotFoundError:
    logging.error("Arquivo reservas.txt não existe")
    sys.exit(1)


quartos = {}
try:
    for line in open('exercicio_reserva/quartos.txt'):
        codigo, nome, preco = line.strip().split(',')
        quartos[int(codigo)] = {
            "nome": nome, 
            "preço": float(preco),   # TODO: Decimal 
            "disponivel": False if int(codigo) in ocupados else True
            }
except FileNotFoundError:
    logging.error("Arquivo quartos.txt não existe")
    sys.exit(1)


print("{:-^40}".format("Reserva Hotel Pythonico"))
print()

if len(ocupados) == len(quartos):
    print("Hotel Lotado")
    sys.exit(1)
nome = input("Digite seu nome: ").strip()


if len(ocupados) == len(quartos):
    print("Hotel Lotado")
    sys.exit(1)

print("{:-^40}".format("Lista de Quartos disponiveis"))
print("-" * 40)

for codigo, dados in quartos.items():
    nome_quarto = dados["nome"]
    preco = dados["preço"]
    disponivel = "⛔" if not dados["disponivel"] else "👍"
    print(f"{codigo} - {nome_quarto} - R$ {preco:.2f} - {disponivel}")

print("-" * 40)

try:
    num_quarto = int(input("Digite o número do quarto: ").strip())
    if not quartos[num_quarto]['disponivel']:
        print(f"O quarto {num_quarto} está ocupado")
        sys.exit(1)
except ValueError:
    logging.error("Número inválido, digite apenas digitos.")
    sys.exit(1)
except KeyError:
    print(f"O quarto {num_quarto} não existe.")
    sys.exit(1)
try:
    dias = int(input("Quantidade de dias: ").strip())
except ValueError:
    logging.error("Número inválido, digite apenas digitos.")
    sys.exit(1)



nome_quarto = quartos[num_quarto]["nome"]
preco_quarto = quartos[num_quarto]['preço']
disponivel = quartos[num_quarto]['disponivel']
total = preco_quarto * dias

print(f"{nome} você escolheu o quarto {nome_quarto} e vai custar R$ {total:.2f}")


with open("exercicio_reserva/reservas.txt", 'a') as file_:
    file_.write(f"{nome}, {num_quarto}, {dias}\n")
