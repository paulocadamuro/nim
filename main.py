# Função da Jogada do Computador

def computador_escolhe_jogada(n, m):
    nj = 0
    multiplo = m + 1
# Definiçao da jogada por parte do PC
    while (n - nj) % multiplo != 0:
        nj = nj + 1
    print("O Computador tirou %s peças." % (nj))
    return nj

# Função da Jogada do Computador


def usuario_escolhe_jogada(n, m):
    # Pede uma entrada do usuário
    nj = input("Quantas peças você vai tirar? ")
    nj = int(nj)

    # Se a entrada for menor que o numero de peças, avisa o usuario e segue o codigo
    if nj > m or nj > n:
        while nj > m or nj > n:
            print("Oops! Jogada inválida! Tente de novo.")
            nj = int(input("Quantas peças você vai tirar? "))

    if nj <= n:
        print("Voce tirou %s peças." % (nj))

    # Se não ele entra em loop ate acertar

    return nj


# Função da Partida
def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    vencedor = 0
    nj = 0
    multiplo = m + 1
    # Se nao tiver na formula (m + 1), passa a vez pro jogador
    if n % multiplo == 0:
        print("Você Começa")
        # Enquanto n de peças não for 0, continua o loop chamando as funções

        while n != 0:
            nj = usuario_escolhe_jogada(n, m)
            n = n - nj
            print("Agora restam %s peças no tabuleiro." % n)
            if n == 0:
                print("O computador Ganhou!")
                return "vit"
            nj = computador_escolhe_jogada(n, m)
            n = n - nj
            vencedor = 1
            print("Agora restam %s peças no tabuleiro." % n)
    else:
        print("O Computador Começa!")
        while n != 0:
            nj = computador_escolhe_jogada(n, m)
            n = n - nj
            if n == 0:
                return "vit"
            else:
                print("Agora restam %s peças no tabuleiro." % n)
            nj = usuario_escolhe_jogada(n, m)
            n = n - nj
            vencedor = 1
            print("Agora restam %s peças no tabuleiro." % n)


# Função main

print("Bem-vindo ao jogo do NIM! Escolha")
print("")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")


escolha = int(input())


if not escolha == 1:
    if not escolha == 2:
        escolha = int(input(a))

if escolha == 1:
    partida()
    print("Fim do jogo! O computador ganhou!")
if escolha == 2:
    print("Voce escolheu um campeonato!")
    np = 0
    while np != 3:
        partida()
        np = np + 1
    print("**** Final do campeonato! ****")

    print("")
    print("Placar: Você 0 X 3 Computador")