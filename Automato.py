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
   """ Inicializa a configuração de um autômato celular, solicita ao usuário
   uma regra em formato decimal e o número de iterações, 
   e simula o autômato celular imprimindo a configuração a cada iteração."""
   nomeArqSaida = input("Digite o nome de um arquivo para a saída: ")
   
   arqSai = open(nomeArqSaida, "w", encoding = 'utf-8')
   
   blocoB = chr(11036)
   blocoP = chr(11035)
   
   arqSai.write(f"Escrevendo os itens de lista utilizando caracteres:"
                f" '{blocoB}' para 0 e '{blocoP}' para 1.\n\n")
   
   
   
   cont=0
   config = [] 
   comp = 61
   for i in range (comp):
       cont = cont + 1
       if cont != (int(comp/2)+1):
        config.append(0)
       else:
        config.append(1)
    
   numdec = int(input("Digite um inteiro entre 0 e 255: "))
   nI = int(input("Digite um inteiro para o número de iterações: "))
   regra = decimal_binario_lista(numdec)[0]
   resp_bin = decimal_binario_lista(numdec)[1]
   print(f"A representação binária do inteiro é {resp_bin} e a regra é {regra}")
   print()
   config_seque= config
   for i in range(len(config)):
       print(config[i], end=" ")
       if config[i] == 0:
           arqSai.write(f"{blocoB}")
       else:
           arqSai.write(f"{blocoP}")
   arqSai.write("\n")         
   print()    
   for i in range(nI):
       config_seque = simula_uma_iteracao(regra, config_seque)
       for k in range(len(config_seque)):
           print(config_seque[k], end = " ")
           if config_seque[k] == 0:
               arqSai.write(f"{blocoB}")
           else:
               arqSai.write(f"{blocoP}")        
       print()    
       arqSai.write("\n") 
   
   
   
   
   
   
       
   
   
   
   
def decimal_binario_lista(n):
        """ 
    (int) --> (list, int)
Recebe um inteiro n entre 0 e 255.
Constrói uma lista com 8 posições, contendo os dígitos da representação
binária de n na ordem reversa, completada com 0’s.
AO MESMO TEMPO, determina um inteiro que é a representação binária de n.
A função retorna a lista e o inteiro construídos.
"""
        lista = []
        cont = 0
        k = 0
        
        for i in range (7):
            if n >= 4:
                lista.append(n%2)
                k = k + (n%2)*(10**(cont))
                n = int(n/2)
                cont = cont + 1
                
            elif n < 4 and n >= 2:
                lista.append(n%2)
                lista.append(int(n/2))
                k = k + (n%2)*(10**(cont)) + int(n/2)*(10**(cont + 1))
                n = int(n/2)
                cont = cont + 1
            else:
                lista.append(0)
        return lista, k

def simula_uma_iteracao(regra, config):
        """ 
(list, list) --> list
Recebe duas listas, regra e config, que são listas de inteiros 0’s e 1’s.
A lista regra tem oito posições e ’armazena’ a representação binária de um
inteiro, entre 0 e 255, na ordem reversa e completada com zeros.
A lista config representa uma configuração num determinado instante.
A função constrói e retorna uma lista config_seque, que representa a
configuração no instante seguinte e que é obtida utilizando a lista regra.
"""
        config_seque = []
        i=0
        while i <= len(config):
            if i < (len(config)-1):
                k = config[i-1]*4 + config[i]*2 + config[i+1]*1
                config_seque.append(regra[k])
                i = i + 1
                
            else:
                k = config[i-1]*4 + config[i]*2 + config[0]*1
                config_seque.append(regra[k])
                i = i + len(config)
        return config_seque
main()