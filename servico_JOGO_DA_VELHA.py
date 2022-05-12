def vitoria_por_linha(jogo):    
    """Verifica se houve ou não uma vitória por parte de algum dos jogadores ao fazer uma sequência de 4 símbolos iguais em uma linha;
    list -> bool"""
    for linha in range(len(jogo)):
            contador = 0
            for coluna in range(1,len(jogo[0])):
                if jogo[linha][coluna] != '-' and jogo[linha][coluna] == jogo[linha][coluna-1]:
                    contador += 1
            if contador == 3:
                 return True
            else:
                return False

def vitoria_por_coluna(jogo):
    """Verifica se houve ou não uma vitória por parte de algum dos jogadores ao fazer uma sequência de 4 símbolos iguais em uma coluna;
    list -> bool"""
    for coluna in range(len(jogo[0])):
            contador = 0
            for linha in range(1,len(jogo)):
                if jogo[linha][coluna] != '-' and jogo[linha][coluna] == jogo[linha-1][coluna]:
                    contador += 1
            if contador == 3:
                return True
    return False

def vitoria_por_diagonal(jogo):
    """Verifica se houve ou não uma vitória por parte de algum dos jogadores ao fazer uma sequência de 4 símbolos iguais em uma diagonal;
    list -> bool"""
    # Verifica a diagonal principal
    if  jogo[0][0] != '-' and jogo[0][0] == jogo[1][1] and jogo[1][1] == jogo[2][2] and jogo[2][2] == jogo[3][3]:
        return True

    # Verifica a diagonal secundária
    if jogo[1][2] !='-' and jogo[1][2] == jogo[0][3] and jogo[1][2] == jogo[2][1] and jogo[3][0] == jogo[2][1]:
        return True
    
    return False

def vitoria_por_quadrado(jogo):
    """Verifica se houve ou não uma vitória por parte de algum dos jogadores ao fazer uma sequência de 4 símbolos iguais em um quadrado;
    list -> bool"""
    for i in range(1,len(jogo)):
        for j in range(1,len(jogo[0])):
            if jogo[i-1][j-1] != "-" and jogo[i-1][j-1] == jogo[i-1][j] and jogo[i-1][j] == jogo[i][j-1] and jogo[i][j-1] == jogo[i][j]:
                return True
    return False
            
def final_jogo(jogo):
    """Essa função recebe a matriz do jogo e verifica se ela já foi totalmente preenchida.
    retorna True se sim e False se ainda não acabou.;
    list -> bool"""
    c = 0
    for linha in range(len(jogo)):
        for coluna in range(len(jogo[0])):
            if jogo[linha][coluna] != '-':
                c += 1
    if c == 16:
        return True
    else:
        return False

def realiza_jogada(matriz,posicao):
    """Altera a matriz substituindo um dos "-" pela letra do jogador na posicão escolhida;
    list, list -> list"""
    matriz[posicao[0]][posicao[1]] = posicao[2]
    return matriz

def teste_vitoria_por_linha():
    """Testa a função vitoria_por_linha"""
    matriz_teste1= [["X","X","X","X"],["O","X","O","X"],["X","O","X","O"],["O","O","X","X"]]
    matriz_teste2= [["O","X","O","X"],["X","X","X","X"],["X","O","X","O"],["O","O","X","X"]]
    matriz_teste3= [["O","X","O","X"],["X","O","X","O"],["X","X","X","X"],["O","O","X","X"]]
    matriz_teste4= [["O","X","O","X"],["X","O","X","O"],["O","O","X","X"],["X","X","X","X"]]
    matriz_teste5= [["O","X","O","X"],["X","O","X","O"],["O","O","X","X"],["X","X","X","O"]]
    matriz_teste6= [["-","-","-","-"],["-","-","-","-"],["-","-","-","-"],["-","-","-","-"]]
    return (vitoria_por_linha(matriz_teste1) == True, vitoria_por_linha(matriz_teste2) == True, vitoria_por_linha(matriz_teste3) == True,
            vitoria_por_linha(matriz_teste4) == True, vitoria_por_linha(matriz_teste5) == False, vitoria_por_linha(matriz_teste6)== False)

def teste_vitoria_por_coluna():
    """Testa a função vitoria_por_coluna"""
    matriz_teste1= [["X","X","X","X"],["O","X","O","X"],["X","O","X","O"],["O","O","X","X"]]
    matriz_teste2= [["X","X","X","X"],["X","X","O","X"],["X","O","X","O"],["X","O","X","X"]]
    matriz_teste3= [["O","X","X","X"],["O","X","O","X"],["O","O","X","O"],["O","O","X","X"]]
    matriz_teste4= [["X","X","X","X"],["O","X","O","X"],["X","O","X","X"],["O","O","X","X"]]
    matriz_teste5= [["-","-","-","-"],["-","-","-","-"],["-","-","-","-"],["-","-","-","-"]]
    return (vitoria_por_coluna(matriz_teste1) == False, vitoria_por_coluna(matriz_teste2) == True,
            vitoria_por_coluna(matriz_teste3) == True, vitoria_por_coluna(matriz_teste4) == True, vitoria_por_coluna(matriz_teste5) == False)

def teste_vitoria_por_diagonal():
    """Testa a funcao vitoria_por_diagonal"""
    matriz_teste1= [["X","X","X","X"],["O","X","O","X"],["X","O","X","O"],["O","O","X","X"]]
    matriz_teste2= [["O","X","X","X"],["O","X","X","X"],["X","X","X","O"],["X","O","X","X"]]
    matriz_teste3= [["O","X","X","X"],["O","O","O","X"],["X","O","O","O"],["O","O","X","O"]]
    matriz_teste4= [["O","X","X","O"],["O","X","O","X"],["X","O","X","O"],["O","O","X","X"]]
    matriz_teste5= [["O","X","X","X"],["O","X","O","X"],["X","O","X","O"],["O","O","X","O"]]
    matriz_teste6= [["-","-","-","-"],["-","-","-","-"],["-","-","-","-"],["-","-","-","-"]]
    return (vitoria_por_diagonal(matriz_teste1) == True, vitoria_por_diagonal(matriz_teste2) == True, vitoria_por_diagonal(matriz_teste3) == True,
            vitoria_por_diagonal(matriz_teste4) == True, vitoria_por_diagonal(matriz_teste5) == False, vitoria_por_diagonal(matriz_teste6)== False)

def teste_final_jogo():
    """Testa a funcao final_jogo"""
    matriz_teste1= [["X","X","X","X"],["O","X","O","X"],["X","O","X","O"],["O","O","X","X"]]
    matriz_teste2= [["O","X","-","X"],["O","X","X","X"],["X","X","X","O"],["X","O","X","X"]]
    matriz_teste3= [["O","X","X","X"],["-","O","O","X"],["X","-","O","O"],["O","O","X","O"]]
    matriz_teste4= [["O","X","X","X"],["O","X","O","X"],["X","O","X","O"],["O","O","X","X"]]
    matriz_teste5= [["O","X","X","X"],["O","X","O","X"],["X","O","X","O"],["O","O","X","O"]]
    matriz_teste6= [["-","-","-","-"],["-","-","-","-"],["-","-","-","-"],["-","-","-","-"]]
    return (final_jogo(matriz_teste1) == True, final_jogo(matriz_teste2) == False, final_jogo(matriz_teste3) == False, final_jogo(matriz_teste4) == True,
            final_jogo(matriz_teste5) == True, final_jogo(matriz_teste6) == False)

def teste_vitoria_por_quadrado():
    matriz_teste1= [["X","X","X","X"],["O","X","O","X"],["X","O","X","O"],["O","O","X","X"]]
    matriz_teste2= [["O","X","-","X"],["O","X","X","X"],["X","X","X","O"],["X","O","X","X"]]
    matriz_teste3= [["O","X","X","X"],["-","O","O","X"],["X","-","O","O"],["O","O","X","O"]]
    matriz_teste4= [["O","X","X","X"],["O","X","O","X"],["X","O","X","O"],["O","O","X","X"]]
    matriz_teste5= [["O","X","X","X"],["O","X","X","X"],["X","O","X","O"],["O","O","X","O"]]
    matriz_teste6= [["-","-","-","-"],["-","-","-","-"],["-","-","-","-"],["-","-","-","-"]]
    return (vitoria_por_quadrado(matriz_teste1) == False, vitoria_por_quadrado(matriz_teste2) == True, vitoria_por_quadrado(matriz_teste3) == False,
            vitoria_por_quadrado(matriz_teste4) == False, vitoria_por_quadrado(matriz_teste5) == True, vitoria_por_quadrado(matriz_teste6) == False)
