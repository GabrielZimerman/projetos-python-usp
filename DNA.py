# -*- coding: utf-8 -*-
"""
Nome do aluno: Gabriel Haenni Zimerman
Número USP: 13744112
Curso: Bacharelado em Matemática
Disciplina: MAC0110 Introdução à Computação
Turma 41
Exercício-Programa EP1

    DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
TODAS AS PARTES ORIGINAIS DESTE EXERCÍCIO-PROGRAMA FORAM
DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
OU PLÁGIO.
    DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS DESTE
PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A SUA DISTRIBUIÇÃO.
ESTOU CIENTE QUE OS CASOS DE PLÁGIO E DESONESTIDADE ACADÊMICA SERÃO
TRATADOS SEGUNDO OS CRITÉRIOS DIVULGADOS NA PÁGINA DA DISCIPLINA.
"""
def main():
    """ () --> NoneType
    Executa a leitura de um arquivo contendo pares de sequências de DNA,
    testa se uma sequência é subsequência da outra, e exibe os resultados.
    """  

    
    print("\n--------------------------------------------------------")
    nomeArqEntrada=input("Digite o nome do arquivo com os dados de entrada: ")
    print()
    # abre o arquivo nomeArqEntrada para leitura
    arqEntrada = open(nomeArqEntrada, 'r', encoding='utf-8')
    
    #   readline() - lê a linha corrente de um arquivo e
    #                retorna uma string com o conteúdo dessa linha
    # Obs.: o caractere de nova linha é incluído no final dessa string 
        
    # lê da 1a. linha do arquivo de entrada o número de pares de seqs. de DNA     
    n = int(arqEntrada.readline())
    print(f"\nExitem {n} pares de sequências de DNA para serem testadas")
    print("\n--------------------------------------------------------")
  
    
    for i in range(1, n+1):
        linhaArq = arqEntrada.readline()
        #   dna_s referencia a string obtida de linhaArq sem 
        # os 'brancos' do início e do final 
        dna_s = linhaArq.strip()
        
        linhaArq = arqEntrada.readline()
        #   dna_t referencia a string obtida de linhaArq sem  
        # os 'brancos' do início e do final de linhaArq
        dna_t = linhaArq.strip()
        
        print(f"\nPar {i}")
        print(f"\ndna_s = {dna_s}")
        print(f"\ndna_t = {dna_t}")
        teste = testa_subsequencia_com_comprovante(dna_s, dna_t)[1]
        comprova = testa_subsequencia_com_comprovante(dna_s, dna_t)[0]
        if teste == True:
            print("\n A string dna_s é uma subsequência da string dna_t")
        else:
            print("\n A string dna_s não é uma subsequência da string dna_t")
        print("\n Veja um comprovante de como dna_s ocorre em dna_t")
        visualiza_comprovante(dna_t,comprova)
        print("\n--------------------------------------------------------")
    
    
def testa_subsequencia_com_comprovante(s, t):
    """ (str, str) --> (bool, str)
     
    Recebe duas strings não vazias, s e t, com o comprimento de s 
    menor ou igual ao comprimento de t.
    Testa se s é uma subsequência de t, construindo uma string comprova, que
    representa um comprovante de que s é ou não é uma subsequência de t.
    A função retorna True ou False (de acordo com o resultado do teste) e a
    string construída comprova.
    """ 
    k = 0
    comprova = ""
    
    for i in range(len(t)):
           
            if k < len(s) and s[k] == t[i]:
                comprova = comprova + s[k]
                k = k + 1
            else:
                comprova = comprova + "-"
            i = i + 1
            
            
    teste = False
    if k == len(s):
        teste = True
                
    if teste == False:
       while (k < len (s)):
           comprova = comprova + s[k]
           k = k + 1
          
                   
            
                
            
    return comprova, teste

def visualiza_comprovante(t, c):
    """ (str, str) --> NoneType
   
    Recebe duas strings não vazias, t e c.
    A string c representa um comprovante de que alguma string é ou 
    não é uma subsequência de t.
    A função constrói uma string marca com o sı́mbolo ’|’ nas posições
    onde o comprovante c indicar que um sı́mbolo foi encontrado em t e 
    com o sı́mbolo ’ ’ nas outras posições.
    Obs.: O número de caracteres da string marca é igual ao de t.
    A função imprime as strings t, marca e c alinhadas.
    """
    v = ""
    for i in range(len(t)):
        if c[i] == "-":
            v = v + " "
        else:
            v = v + "|"
    print(f"\ndna_t:        {t}")
    print(f"\n              {v}")
    print(f"\ncomprovante:  {c}")
main()

