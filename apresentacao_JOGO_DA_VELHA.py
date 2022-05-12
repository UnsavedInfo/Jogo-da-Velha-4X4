def letra_jogador1():
    """Retorna a letra(X ou O) escolhida pelo jogador 1;
    input -> string"""
    letra_1 = "vazio"
    while letra_1 != "X" and letra_1 != "O" or letra_1 == '':
        letra_1 = input("\nJogador 1, escolha sua letra (X/O):\n")
        if letra_1 != "X" and letra_1 != "O" or letra_1 == '':
            print("\nEntrada Inválida")
    return letra_1


def letra_jogador2(letra_1):
    """Retorna a letra(X ou O) escolhida pelo jogador 2;
    input -> string"""
    letra_2 = "vazio"
    while letra_2 != "X" and letra_2 != "O" or letra_2 == '' or letra_2 == letra_1:
        letra_2 = input("\nJogador 2, escolha sua letra (X/O):\n")
        if letra_2 not in "XO" or letra_2 == '' or letra_2 == letra_1:
            print("\nEntrada Inválida")
    return letra_2


def mostra_tabuleiro(jogo):
    """Essa função converte a matriz de entrada em uma string e exibe ela como o tabuleiro para o usuário"""
    s = '\n'
    for i in range(len(jogo)):
        for j in range(len(jogo[i])):
            s+='   '+jogo[i][j]
        s += '\n'
    print(s)


def nova_partida():
    """Pergunta ao usuário se ele deseja realizar uma nova partida e guarda essa resposta;
    none -> string"""
    resposta = input("Deseja iniciar uma nova partida?(S/N)\n")
    while resposta != "S" and resposta != "N" or resposta == "":
        resposta =input('Comando inválido. Deseja iniciar uma nova partida (S/N)?:')
    return resposta


def posicao_jogada(jogo,letra,jogador):
    """Solicita ao jogador que insira a posição(linha e coluna) em que ele deseja realizar sua jogada e guarda essa informação, junto com a letra escolhida pelo
    jogador, em uma lista;
    list, string, string -> list"""
    valor = True
    while valor == True:
       Posicao_str = input('\nJogador {}, entre com a posição da linha e coluna[x,y]:\n'.format(jogador))
       if (len(Posicao_str)==5 and Posicao_str[1] in "0123" and Posicao_str[3] in "0123" and Posicao_str[0] == '[' and Posicao_str[4] == ']'
           and Posicao_str[2] == ',' and jogo[int(Posicao_str[1])][int(Posicao_str[3])] =='-'):
           valor = False
           Posicao = [int(Posicao_str[1]),int(Posicao_str[3]),letra]
           return Posicao
       else:
           print("\nPosição inválida.")


def informa_vencedor(jogador):
    """Informa qual dos dois jogadores venceu o jogo;
    string -> string"""
    print ("O {} venceu o jogo".format(jogador))


def informa_empate():
    """Informa que houve um empate"""
    print("Empate")


def informa_novo_jogo():
    """Informa ao usuário que um novo jogo está se iniciando;
    none -> none"""
    print(">>> NOVO JOGO\n")
