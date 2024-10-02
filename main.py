import os

mensagem = []

nome = input("nome: ")

while True:
    os.system('cls')

    if len(mensagem) > 0:
        for m in mensagem:
            print(m['nome'], "-", m['texto'])

    print("________________________")

    texto = input("mensagens: ")

    if texto == "fim":
        break

    mensagem.append({
        "nome": nome,
        "texto": texto
    })
