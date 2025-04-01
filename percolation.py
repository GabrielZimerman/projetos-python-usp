# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM import ...
#------------------------------------------------------------------

'''

    Nome: Gabriel Haenni Zimerman
    NUSP: 13744112

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não 
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da 
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

    Abaixo descreva qualquer ajuda que você recebeu para fazer este
    EP.  Inclua qualquer ajuda recebida por pessoas (inclusive
    monitores e colegas). Com exceção de material de MAC0110 e MAC0122, 
    caso você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''

#-------------------------------------------------------------------------- 
# constantes
BLOCKED = 0  # sítio bloqueado
OPEN    = 1  # sítio aberto
FULL    = 2  # sítio cheio

class Percolation:
    '''
    Representa uma grade n x m com todos os sítios inicialmente bloqueados.
    o parâmetro shape é a forma (n, m) da matriz que representa a grade.
    '''

    def __init__(self, shape):
        if type(shape) == int:
            shape = (shape, shape)
        self.shape = shape
        self.grid = []
        
        for i in range(shape[0]):
            self.grid.append([BLOCKED]*shape[1])
            
    def __str__(self):#FINALIZAR 
       
        
        linha1= '+'
        linha2='|'
        
        moldura =''
        linhas = []
        
        for m in range(self.shape[1]):
            linha1 += '---+'
            
            
        for n in range(self.shape[0]):
            for m in range(self.shape[1]):
                if self.grid[n][m] == BLOCKED:
                    linha2 += '   |'
                elif self.grid[n][m] == OPEN:
                    linha2 += ' o |'
                else:
                    linha2 += ' x |'
                         
            linhas.append(linha2)
            linha2='|'
                     
        for linha2 in linhas:
            moldura += linha1 +'\n' + linha2 + '\n'
        moldura += linha1
        
        
        return f'{moldura}\ngrade de dimensão: {self.shape[0]}x{self.shape[1]}\nno. sítios abertos: {self.no_open()}\npercolou: {self.percolates()}\n'
        
        
    def is_open(self,lin,col):
        
        if lin > self.shape[0] - 1 or col > self.shape[1] - 1:
            print(f'posição[{lin}][{col}] está fora da grade')
            return None 
        
        if self.grid[lin][col] == OPEN or self.grid[lin][col] == FULL:
            return True
        else:
            return False 
        
        
    def is_full(self,lin,col):
        
        if lin > self.shape[0] - 1 or col > self.shape[1] - 1:
            print(f'posição[{lin}][{col}] está fora da grade')
            return None 
        
        if self.grid[lin][col] == FULL:
            return True
        else:
            return False 
        
        
    def percolates(self):
        ult_linha = self.grid[-1]
        for num in ult_linha:
            if num == FULL:
                return True
        return False
        
    def no_open(self):
        
        cont = 0
        for n in range(self.shape[0]):
            for m in range(self.shape[1]):
                if self.grid[n][m] == OPEN or self.grid[n][m] == FULL:
                    cont += 1
        return cont
    
    
    def open(self, lin, col):
       vizinhos_open = []
       
       if lin > self.shape[0] - 1 or col > self.shape[1] - 1:
           print(f'posição[{lin}][{col}] está fora da grade')
           return None 
       
       if lin != 0: 
           self.grid[lin][col] = OPEN
       else:
           self.grid[lin][col] = FULL
       
       
       if lin-1 >= 0:
           if self.grid[lin-1][col] == OPEN or self.grid[lin-1][col] == FULL:
               vizinhos_open.append((lin-1,col))
               
       if lin+1 <= self.shape[0]-1:
           if self.grid[lin+1][col] == OPEN or self.grid[lin+1][col] == FULL:
               vizinhos_open.append((lin+1,col))
       
       if col-1 >= 0:
           if self.grid[lin][col-1] == OPEN or self.grid[lin][col-1] == FULL:
               vizinhos_open.append((lin,col-1))
               
       
       if col+1 <= self.shape[1]-1:
           if self.grid[lin][col+1] == OPEN or self.grid[lin][col+1] == FULL:
               vizinhos_open.append((lin,col+1))
       
       
       aux_vizinhos_open = []
       while  vizinhos_open != []:
           elemento = vizinhos_open.pop()
           if elemento not in aux_vizinhos_open:
               aux_vizinhos_open.append(elemento)
           if elemento[0]-1 >= 0:
               if (elemento[0]-1,elemento[1]) not in aux_vizinhos_open and (self.grid[elemento[0]-1][elemento[1]] == OPEN or self.grid[elemento[0]-1][elemento[1]] == FULL):
                   vizinhos_open.append((elemento[0]-1,elemento[1]))
                   
           if elemento[0]+1 <= self.shape[0]-1:
               if (elemento[0]+1,elemento[1]) not in aux_vizinhos_open and (self.grid[elemento[0]+1][elemento[1]] == OPEN or self.grid[elemento[0]+1][elemento[1]] == FULL):
                   vizinhos_open.append((elemento[0]+1,elemento[1]))
           
           if elemento[1]-1 >= 0:
               if (elemento[0],elemento[1]-1) not in aux_vizinhos_open and (self.grid[elemento[0]][elemento[1]-1] == OPEN or self.grid[elemento[0]][elemento[1]-1] == FULL):
                   vizinhos_open.append((elemento[0],elemento[1]-1))
                   
           
           if elemento[1]+1 <= self.shape[1]-1:
               if (elemento[0],elemento[1]+1) not in (vizinhos_open and aux_vizinhos_open) and (self.grid[elemento[0]][elemento[1]+1] == OPEN or self.grid[elemento[0]][elemento[1]+1] == FULL):
                   vizinhos_open.append((elemento[0],elemento[1]+1))
        
       condicao = False 
       for pos_0 in aux_vizinhos_open:
           if pos_0[0] == 0:
               condicao = True
       if condicao:
           for pos in aux_vizinhos_open:
               self.grid[pos[0]][pos[1]] = FULL
               
    def get_grid(self):
        clone = self.grid[:]
        return clone                    
    
       
               


