from apresentacao_JOGO_DA_VELHA import letra_jogador1, letra_jogador2, posicao_jogada, nova_partida, informa_vencedor, mostra_tabuleiro, informa_empate, informa_novo_jogo
from servico_JOGO_DA_VELHA import vitoria_por_linha, vitoria_por_coluna, vitoria_por_diagonal, final_jogo, realiza_jogada, vitoria_por_quadrado


def main():
    """Função principal que articula todas as funções criadas anteriormente para execução do programa/jogo
    (I) Começa imprimindo na tela a mensagem "NOVO JOGO"
    (II) Na sequência é exibida o tabuleiro mostrando o estado inicial do jogo 
    (III)É solicitado que jogador 1 e jogador 2 escolham suas letras(X/O)
    (IV) A partir dai, será requisitado que os jogadores realizem suas jogadas. A cada jogada o tabuleiro é imprimido na tela para mostrar o novo estado do jogo
    (V) O valor dado como entrada é atribuido a posicao que está na matriz que essa funcao retorna.
    (VI)Em caso de vitória de algum dos jogadores ou empate, é perguntado ao usuário se ele deseja iniciar uma nova partida ou finalizar."""
    
    informa_novo_jogo()
    jogo = [['-','-','-','-'],['-','-','-','-'],['-','-','-','-'],['-','-','-','-']]
    
    mostra_tabuleiro(jogo)
    letra1 = letra_jogador1()
    letra2 = letra_jogador2(letra1)
    
    while final_jogo(jogo) != True:
        Posicao_j1 = posicao_jogada(jogo,letra1,'1')
        jogo = realiza_jogada(jogo, Posicao_j1)
        mostra_tabuleiro(jogo)

        if vitoria_por_coluna(jogo) == True or vitoria_por_linha(jogo) == True or vitoria_por_diagonal(jogo) == True or vitoria_por_quadrado(jogo) == True:
                 informa_vencedor("Jogador 1")
                 if nova_partida() == "S":
                     return main()
                 else:
                     return 0 
            
        Posicao_j2 = posicao_jogada(jogo,letra2,'2')
        jogo = realiza_jogada(jogo, Posicao_j2)
        (mostra_tabuleiro(jogo))
        
        if vitoria_por_coluna(jogo) == True or vitoria_por_linha(jogo) == True or vitoria_por_diagonal(jogo) == True:
                 informa_vencedor("Jogador 2")
                 if nova_partida() == "S":
                     return main()
                 else:
                        return 0
        final_jogo(jogo)

    informa_empate()
    if nova_partida() == "S":
        return main()
    else:
        return 0 

main()
