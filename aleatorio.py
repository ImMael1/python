import random

opcoes_usuario = input(
    "Insira as opcoes a serem sorteadas, separados por vírgula:")

opcoes = opcoes_usuario.split(',')

opcoes = [opcao.strip() for opcao in opcoes]

escolha_aleatoria = random.choice(opcoes)

print("A escolha aleatória é:", escolha_aleatoria)