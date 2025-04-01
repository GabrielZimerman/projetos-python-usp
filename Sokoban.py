# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 19:27:21 2024

@author: gabri
"""

#------------------------------------------------------------------------------
# DEFINIÇÃO DE ALGUMAS 'CONSTANTES' DO PROGRAMA
#------------------------------------------------------------------------------

# CARACTERES USADOS NO MAPA DO JOGO
PAREDE           = '#'
PISO_VAZIO       = ' '
MARCA_VAZIA      = '.'    
CAIXA_NO_PISO    = '$'
CAIXA_NA_MARCA   = '*'
JOGADOR_NO_PISO  = '@'
JOGADOR_NA_MARCA = '+'

# CARACTERES USADOS PARA ESCOLHER E INDICAR UM MOVIMENTO DO JOGADOR
CIMA     = 'w'
BAIXO    = 's'
ESQUERDA = 'a'
DIREITA  = 'd'
FINALIZA = 'f'

#  CARACTERES USADOS PARA INDICAR UM MOVIMENTO DO JOGADOR QUANDO UMA CAIXA
# É EMPURRADA. Essas 'constantes' não precisam aparecer explicitamente 
# no seu programa.
CIMA_CX     = 'W'
BAIXO_CX    = 'S'
ESQUERDA_CX = 'A'
DIREITA_CX  = 'D'

#------------------------------------------------------------------------------
#  DEFINIÇÃO DE UM DICIONÁRIO 
# que mapeia cada uma das quatro direções possíveis para um par
# (incremento no índice de linha, incremento no índice de coluna)
# e deve ser utilizado para determinar a nova posição do jogador 
#------------------------------------------------------------------------------

DirMovJog = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
 
 

def main():
    
    mapa = le_arquivo_cria_mapa_jogo()
    imprime_mapa_jogo(mapa)
    imprime_mapa_jogo_emoldurado(mapa)
    print('----------------------------------------------------------------\n')
    
    historico_movimentos = ""
 
    jogo_continua = True 
    while jogo_continua:
        
        
        pos_jogador = posicao_jogador(mapa)
        valor_pos_jogador = mapa[pos_jogador[0]][pos_jogador[1]]
        print(f'Jogador ({valor_pos_jogador}) está na posição {pos_jogador}\n')
        escolha = input(" Digite os movimentos que deseja para o jogador, "
                        "escolhendo entre\n| w | s | a | d | f | "
                        "(cima, baixo, esq, dir, finaliza): ")
        
        
        n = len(escolha)        
        i = 0
        while i < n and jogo_continua:
            
            caracMov = escolha[i]
            
            nova_pos_jogador = (DirMovJog[caracMov][0]+pos_jogador[0],
                                    DirMovJog[caracMov][1]+pos_jogador[1])
                
            valor_nova_pos_jogador = mapa[nova_pos_jogador[0]][nova_pos_jogador[1]]
                
            if caracMov != FINALIZA:
                retorno = tenta_movimentar_jogador(mapa, caracMov)
                mov_valido = retorno[0]
                caixa_empurrada = retorno[1]
                
                if mov_valido == False and valor_nova_pos_jogador == PAREDE:
                    print("\nMovimento inválido:"
                          f" o jogador {pos_jogador} vai bater na parede!")
                    
                    jogo_continua = False
                    
                elif (
                        mov_valido == False and
                        (valor_nova_pos_jogador == CAIXA_NO_PISO or
                         valor_nova_pos_jogador == CAIXA_NA_MARCA)
                        ):
                    print("\nMovimento inválido:"
                          f" a caixa {nova_pos_jogador} está presa!")
                    jogo_continua = False
                
                elif (
                        mov_valido == True and
                        caixa_empurrada == False
                        ):
                    historico_movimentos = historico_movimentos + caracMov
                
                else:
                    historico_movimentos = historico_movimentos + caracMov.upper()
            else: 
                print("\n O jogo ainda não acabou."
                      "Poderia tentar um pouco mais.")
                jogo_continua = False
                
                
            
            i = i + 1
        imprime_mapa_jogo_emoldurado(mapa)
        print('------------------------------------------------------------\n')
        
        
        if todas_caixas_posicionadas(mapa) == True:
            jogo_continua = False
            print("Parabéns! Todas caixas foram posicionadas")
        
    print("\n o histórico dos movimentos realizado é o seguinte:"
            f"\n {historico_movimentos}")
            
    
    
            
            
            
        
    
        

def le_arquivo_cria_mapa_jogo():
    ''' ( ) --> matriz 

    Lê o nome de um arquivo contendo um mapa de um jogo de Sokoban.
    Abre esse arquivo, lê uma representação de um mapa de jogo de
    Sokoban, cria uma matriz com esse mapa e retorna a matriz criada.
    
    Exemplo:
    Para o arquivo de entrada "sokoban00.txt" com o mapa abaixo:
    #####
    #@$. #
    #####

    a seguinte lista de listas é retornada:
    [['#', '#', '#', '#', '#'], ['#', '@', '$', '.', ' ', '#'], 
                                     ['#', '#', '#', '#', '#']]
    '''

    nomeArq = input("Digite o nome do arquivo com um mapa do jogo sokoban: ")

    with open(nomeArq, 'r', encoding='utf-8') as arqEntra:
        mapa = []
        for linha in arqEntra:
            mapa.append(list(linha.rstrip()))
            
    return mapa   
      
#-----------------------------------------------------------------------
    
def imprime_mapa_jogo(mapa):
    ''' (matriz) --> NoneType

    Recebe uma matriz representando um mapa de um jogo de Sokoban
    e imprime esse mapa.

    Exemplo: Se mapa referencia a seguinte lista de listas:
    [['#', '#', '#', '#', '#'], ['#', '@', '$', '.', ' ', '#'], 
                                     ['#', '#', '#', '#', '#']]
    a função deve imprimir:
    
      Mapa de um jogo:

      #####
      #@$. #
      #####

    '''
    
    print("\n Mapa de um jogo: \n")    
    for linha in mapa:
        print(f"{''.join(linha)}")
    print()
           
#-----------------------------------------------------------------------

def imprime_mapa_jogo_emoldurado(mapa):
    ''' (matriz) --> NoneType

    Recebe uma matriz representando um mapa de um jogo de Sokoban
    e imprime esse mapa totalmente "emoldurado" e com as linhas e
    colunas numeradas para facilitar a visualização do usuário.

    '''
 
    # maxcol representa o maior dos comprimentos das linhas da matriz mapa. 
    maxcol = 0
    for linha in mapa:
        if len(linha) > maxcol:
            maxcol = len(linha)
            
    print("\n")            
    s = ' '*7
    for i in range(maxcol):
        s += f"{i:^5} "
    print(f"{s}")
    
    molda_linha = (' '*6) + ('+-----' * maxcol) + '+'
    print(f"{molda_linha}")
    
    nlin = len(mapa)
    for i in range(nlin):
        ncol = len(mapa[i])
        s = f"{i:5} "
        for j in range(ncol):
            s+= f"|{mapa[i][j]:^5}"
        for k in range(ncol, maxcol):
            s+= f"|{' '*5}"
        s+='|'
        print(f"{s}")
        print(f"{molda_linha}")
    print()    
    
#----------------------------------------------------------------------
def posicao_jogador(mapa):
    ''' (matriz) --> (int, int) ou (NoneType, NoneType)

    Recebe uma matriz representando um mapa de um jogo de Sokoban.
    Retorna os índices de linha e de coluna da posição do jogador
    na matriz mapa.
    Caso o jogador não seja encontrado, deve retornar (None, None).

    Exemplo: No mapa abaixo, o jogador está na posição (2, 3).
    
    #######
    #     #

    # $+$ #
    #.*#*.#
    # $.$ #
    #     #
    #######

    ''' 
    cont = 0
    jogador = False
    for linha in mapa:
        for i in range(len(linha)):
            if linha[i] == '@' or linha[i] == '+':
                index_linha = cont
                index_coluna = i
                jogador = True
        cont = cont + 1
    if jogador == False:
        return None, None
    else:
        return index_linha, index_coluna
#------------------------------------------------------------------------------

def tenta_movimentar_jogador(mapa, caracMov):
    ''' (matriz, str) --> (bool, bool)

    Recebe uma matriz representando um mapa de um jogo de Sokoban e 
    um caractere caracMov que representa uma das direções possíveis 
    (CIMA, BAIXO, ESQUERDA ou DIREITA) para um movimento do jogador.
    Se possível, a função realiza o movimento dado por caracMov e 
    atualiza a matriz mapa. 
    A função retorna dois valores booleanos:
    - O primeiro indica se o movimento é válido (True) ou não (False).
    - O segundo indica se uma caixa foi empurrada (True) ou não (False)
    pelo movimento do jogador.
    OBS: 1) O segundo valor deve ser sempre False se o primeiro for False.
    2) Quando o movimento não é válido (ou porque o jogador vai bater na
    parede ou porque a caixa que seria empurrada pelo jogador está presa),
    a função escreve uma mensagem na tela relatando uma das duas situações.
    '''
    
    #variaveis de localizacao e respectivos valores na matriz mapa    
    pos_jogador = posicao_jogador(mapa)  
    valor_pos_jogador = mapa[pos_jogador[0]][pos_jogador[1]]
        
    nova_pos_jogador = (DirMovJog[caracMov][0]+pos_jogador[0],
                            DirMovJog[caracMov][1]+pos_jogador[1])
        
    valor_nova_pos_jogador =  mapa[nova_pos_jogador[0]][nova_pos_jogador[1]]
        
        
    #variaveis auxiliares para verificar a validade do movimento    
    index_aux_matriz = (DirMovJog[caracMov][0] + nova_pos_jogador[0],
                            DirMovJog[caracMov][1] + nova_pos_jogador[1])
    aux_valor_matriz = mapa[index_aux_matriz[0]][index_aux_matriz[1]]
        
    mov_valido = True
    caixa_empurrada = False
    #sequencia if e elif definem quando o mov sera invalido
    if valor_nova_pos_jogador == PAREDE:
        
        mov_valido = False
        
    elif ( 
            (valor_nova_pos_jogador == CAIXA_NA_MARCA or 
            valor_nova_pos_jogador == CAIXA_NO_PISO) and
            (aux_valor_matriz == CAIXA_NA_MARCA or 
            aux_valor_matriz == CAIXA_NO_PISO or 
            aux_valor_matriz == PAREDE)
            ):
        
        mov_valido = False
    #sequecias de elif para quando o mov é valido, mas a caixa nao é empurrada
    elif ( 
            valor_pos_jogador == JOGADOR_NO_PISO and 
            valor_nova_pos_jogador == PISO_VAZIO
            ):
        
        mapa[pos_jogador[0]][pos_jogador[1]] = PISO_VAZIO
        mapa[nova_pos_jogador[0]][nova_pos_jogador[1]] = JOGADOR_NO_PISO
    
    elif ( 
            valor_pos_jogador == JOGADOR_NO_PISO and 
            valor_nova_pos_jogador == MARCA_VAZIA
            ):
        
        mapa[pos_jogador[0]][pos_jogador[1]] = PISO_VAZIO
        mapa[nova_pos_jogador[0]][nova_pos_jogador[1]] = JOGADOR_NA_MARCA
        
    elif ( 
             valor_pos_jogador == JOGADOR_NA_MARCA and 
             valor_nova_pos_jogador == PISO_VAZIO
             ):
        
        mapa[pos_jogador[0]][pos_jogador[1]] = MARCA_VAZIA
        mapa[nova_pos_jogador[0]][nova_pos_jogador[1]] = JOGADOR_NO_PISO
        
    elif ( 
             valor_pos_jogador == JOGADOR_NA_MARCA and 
             valor_nova_pos_jogador == MARCA_VAZIA
             ):
        
        mapa[pos_jogador[0]][pos_jogador[1]] = MARCA_VAZIA
        mapa[nova_pos_jogador[0]][nova_pos_jogador[1]] = JOGADOR_NA_MARCA
        
    #sequencias de elif para quando a caixa é empurrada
    elif (
           valor_pos_jogador == JOGADOR_NO_PISO and 
           valor_nova_pos_jogador == CAIXA_NO_PISO and
           aux_valor_matriz == PISO_VAZIO
            ):
        
        mapa[pos_jogador[0]][pos_jogador[1]] = PISO_VAZIO
        mapa[nova_pos_jogador[0]][nova_pos_jogador[1]] = JOGADOR_NO_PISO
        mapa[index_aux_matriz[0]][index_aux_matriz[1]] = CAIXA_NO_PISO
        caixa_empurrada = True
        
    elif (
           valor_pos_jogador == JOGADOR_NO_PISO and 
           valor_nova_pos_jogador == CAIXA_NO_PISO and
           aux_valor_matriz == MARCA_VAZIA
            ):
        
        mapa[pos_jogador[0]][pos_jogador[1]] = PISO_VAZIO
        mapa[nova_pos_jogador[0]][nova_pos_jogador[1]] = JOGADOR_NO_PISO
        mapa[index_aux_matriz[0]][index_aux_matriz[1]] = CAIXA_NA_MARCA
        caixa_empurrada = True
        
    elif (
           valor_pos_jogador == JOGADOR_NO_PISO and 
           valor_nova_pos_jogador == CAIXA_NA_MARCA and
           aux_valor_matriz == PISO_VAZIO
            ):
        
        mapa[pos_jogador[0]][pos_jogador[1]] = PISO_VAZIO
        mapa[nova_pos_jogador[0]][nova_pos_jogador[1]] = JOGADOR_NA_MARCA
        mapa[index_aux_matriz[0]][index_aux_matriz[1]] = CAIXA_NO_PISO
        caixa_empurrada = True
        
    elif (
            valor_pos_jogador == JOGADOR_NO_PISO and 
            valor_nova_pos_jogador == CAIXA_NA_MARCA and
            aux_valor_matriz == MARCA_VAZIA
             ):
         
         mapa[pos_jogador[0]][pos_jogador[1]] = PISO_VAZIO
         mapa[nova_pos_jogador[0]][nova_pos_jogador[1]] = JOGADOR_NA_MARCA
         mapa[index_aux_matriz[0]][index_aux_matriz[1]] = CAIXA_NA_MARCA
         caixa_empurrada = True
        
    elif (
             valor_pos_jogador == JOGADOR_NA_MARCA and 
             valor_nova_pos_jogador == CAIXA_NO_PISO and
             aux_valor_matriz == PISO_VAZIO
              ):
          
          mapa[pos_jogador[0]][pos_jogador[1]] = MARCA_VAZIA
          mapa[nova_pos_jogador[0]][nova_pos_jogador[1]] = JOGADOR_NO_PISO
          mapa[index_aux_matriz[0]][index_aux_matriz[1]] = CAIXA_NO_PISO
          caixa_empurrada = True
          
    elif (
             valor_pos_jogador == JOGADOR_NA_MARCA and 
             valor_nova_pos_jogador == CAIXA_NA_MARCA and
             aux_valor_matriz == PISO_VAZIO
              ):
          
          mapa[pos_jogador[0]][pos_jogador[1]] = MARCA_VAZIA
          mapa[nova_pos_jogador[0]][nova_pos_jogador[1]] = JOGADOR_NA_MARCA
          mapa[index_aux_matriz[0]][index_aux_matriz[1]] = CAIXA_NO_PISO
          caixa_empurrada = True
          
    elif (
              valor_pos_jogador == JOGADOR_NA_MARCA and 
              valor_nova_pos_jogador == CAIXA_NA_MARCA and
              aux_valor_matriz == MARCA_VAZIA
               ):
           
           mapa[pos_jogador[0]][pos_jogador[1]] = MARCA_VAZIA
           mapa[nova_pos_jogador[0]][nova_pos_jogador[1]] = JOGADOR_NA_MARCA
           mapa[index_aux_matriz[0]][index_aux_matriz[1]] = CAIXA_NA_MARCA
           caixa_empurrada = True
           
    elif (
              valor_pos_jogador == JOGADOR_NA_MARCA and 
              valor_nova_pos_jogador == CAIXA_NO_PISO and
              aux_valor_matriz == MARCA_VAZIA
               ):
           
           mapa[pos_jogador[0]][pos_jogador[1]] = MARCA_VAZIA
           mapa[nova_pos_jogador[0]][nova_pos_jogador[1]] = JOGADOR_NO_PISO
           mapa[index_aux_matriz[0]][index_aux_matriz[1]] = CAIXA_NA_MARCA
           caixa_empurrada = True
        
            
   
    
    return mov_valido, caixa_empurrada
#------------------------------------------------------------------------------
 
def todas_caixas_posicionadas(mapa):
    ''' (matriz) --> bool

    Recebe uma matriz representando um mapa de um jogo de Sokoban e
    verifica se todas as caixas estão posicionadas nas marcas. 
    Se estiverem, a função retorna True; em caso contrário, retorna False.
    '''
    jogo_concluido = True
    for linha in mapa:
        for i in range(len(linha)):
            if linha[i] == '.':
                jogo_concluido = False
            
    return jogo_concluido 
        
        
#------------------------------------------------------------------------------      
main()