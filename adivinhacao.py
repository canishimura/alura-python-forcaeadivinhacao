import random

def jogar():

    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")

    numero_secreto = round(random.randrange(1,101))
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de difículdade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for tentativa in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(tentativa, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")

        print("Você digitou ", chute_str)

        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = numero_secreto == chute
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Seu chute foi maior que o número secreto.")
            elif (menor):
                print("Seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()