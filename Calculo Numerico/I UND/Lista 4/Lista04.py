import numpy
import sys
from copy import deepcopy

def cabecalho(questao, enunciado):
    return print(f'|{"-"*100}|\n|{" "*43}QUESTAO {questao}{" "*47}|\n|{"-"*100}|\n{enunciado}\n*{"-"*100}*')


def cabecalho_resolucao():
    return print(f'*{"-"*100}*')

def verificacao(A, txt):
    det = numpy.linalg.det(A)
    if det == 0:
        print(f'{txt}) det[A] = {det}, logo, o sistema linear é indeterminado.\n')
    else:
        print(f'{txt}) det[A] = {det}, logo, o sistema linear é determinado e possui solução única.\n')
    return A

def gauss_sem_pivoteamento(x_1, y_1):
  A = deepcopy(x_1)
  b = deepcopy(y_1)
  print(f'{"*"*40} Eliminação de Gauss: {"*"*40}')
  print('Matriz dos Coeficientes:')
  for c in range(0, len(A)): print(A[c])
  print(f'\nVetor dos Termos Constantes:\n{b}\n')

  #Calculo dos pivôs.
  n = len(b)
  for k in list(range(1, n, 1)):
    # Calculo dos multiplicadores.
    for i in list(range(k+1,n+1,1)):
      m = A[i-1][k-1]/A[k-1][k-1]
      A[i-1][k-1] = 0
      b[i-1] = b[i-1] - m*b[k-1]
      print(f'Escalonamento:')
      for c in range(0, len(A)): print(A[c])
      print(f'\nVetor dos Termos Constantes:\n{b}\n')
      #Atualizar demais valores da linha
      for j in list(range(k+1,n+1,1)):
        A[i-1][j-1] = A[i-1][j-1]-m*A[k-1][j-1]

  print('Matriz Escalonada:')
  for c in range(0, len(A)): print(A[c])
  print()
  return A, b


def fatoracao_LU(x_2):
    LU = deepcopy(x_2)
    print(f'{"*"*44} Fatoração LU: {"*"*44}')
    print('Matriz dos Coeficientes:')
    for c in range(0, len(LU)): print(LU[c])
    print()
    # Calculo dos pivos.
    n = len(LU)
    for k in list(range(1, n, 1)):
        # Calculo dos multiplicadores.
        for i in list(range(k+1,n+1,1)):
            m = LU[i-1][k-1]/LU[k-1][k-1]
            LU[i-1][k-1] = m
            print(f'Escalonamento:')
            for c in range(0, len(LU)): print(LU[c])
            print()
            #Atualizar demais valores da linha
            for j in list(range(k+1,n+1,1)):
                LU[i-1][j-1] = LU[i-1][j-1]-m*LU[k-1][j-1]
    print(f'Escalonamento:')
    for c in range(0, len(LU)):
        print(LU[c])
    print()

    print('Matriz Escalonada:')
    print('Matriz Triangular Superior:')
    superior = deepcopy(LU)
    k = 0
    for c in range(0, len(LU)):
        print(superior[c])
        k +=1
        z = k
        for v in range(0, len(LU)):
            if z < len(LU):
                superior[c+1][v] -= superior[c+1][v]
                z -= 1
            if z == 0:
                break
    print()
    print('Matriz Triangular Inferior:')
    inferior = deepcopy(LU)
    k = 0
    for c in range(0, len(LU)):
        inferior[c][c] = inferior[c][c]/inferior[c][c]
        for v in range(1, len(LU)):
            if c+v < len(LU):
                inferior[c][v+c] -= inferior[c][v+c]
        print(inferior[c])
    print()
    return LU


#Resolve o sistema triangular inferior.
def triangular_inferior(T_l, b_l):
     L = deepcopy(T_l)
     b = deepcopy(b_l)
     n = len(b)
     y = [0] * n

     for i in list(range(1, n + 1, 1)):
          s = 0
          for j in list(range(1, i, 1)):
               s = s + L[i - 1][j - 1] * y[j - 1]
          y[i - 1] = b[i - 1] - s

     eps = sys.float_info.epsilon  # precisao da maquina
     for c in range(0, len(y)):
         if abs(y[c]) < eps:
             y[c] = 0
     print(f'Resultado da Matriz Triangular Inferior:')
     return y

#Resolve o sistema triangular superior.
def triangular_superior(T_u, b_u):
  U = deepcopy(T_u)
  b = deepcopy(b_u)
  n = len(b)
  x = [0]*n
  x[n-1] = b[n-1]/U[n-1][n-1]

  for i in list(range(n-1, 0, -1)):
    s = 0
    for j in list(range(i+1,n+1,1)):
      s = s + U[i-1][j-1]*x[j-1]
    x[i-1] = (b[i-1]-s)/(U[i-1][i-1])

  eps = sys.float_info.epsilon #precisao da maquina
  for c in range(0, len(x)):
    if abs(x[c]) <= eps:
      x[c] = 0

    verf = str(x[c])
    pos_ponto = verf.find(".")
    z = len(verf[verf.find(".")+1:]) #tam strg decimal
    cond = 0
    if (z >= 15):
       parameter = verf[pos_ponto+1]
       for v in range(pos_ponto+2, len(verf)):
           if verf[v] == parameter:
               cond += 1
       if cond > 10:
           x[c] = round(x[c])
           cond = 0
  print(f'Resultado da Matriz Triangular Superior:')
  return x


#ENUNCIADOS:
q01 = """1) Para que serve a técnica de pivoteamento parcial, que deve ser empregada no processo de resolução
de um sistema de equações pelo método direto de eliminação de Gauss?"""

q02 = """Resolva os sistemas lineares abaixo usando os métodos diretos Eliminação de Gauss e Fatoração LU.
Use a técnica de pivoteamento parcial se necessário (se o pivô for zero)

a. 
     3x1 + 2x2 + 4x3 = 1
     x1 + x2 + 2x3 = 2
     4x1 + 3x2 + 2x3 = 3
     
b.     
     3x1 - 4x2 + x3 = 9
     x1 + 2x2 + 2x3 = 3
     4x1 + 0x2 - 3x3 = -2
     
c.     
     3x1 - 2x2 + 5x3 + x4 = 7
    -6x1 + 4x2 - 8x3 + x4 = -9
     9x1 - 6x2 + 19x3 + x4 = 23
     6x1 - 4x2 - 6x3 + 15x4 = 11"""


#QUESTAO-01
cabecalho("01", q01)
print("""Resp. - A técnica de pivoteamento parcial ajuda a evitar a propagação dos erros de arredondamento.""")
cabecalho_resolucao()

#QUESTAO-02
cabecalho("02", q02)

#Dados:
a1 = ([[3, 2, 4],
       [1, 1, 2],
       [4, 3, 2]])

b1 = ([1, 2, 3])

a2 = ([[3, -4, 1],
       [1, 2, 2],
       [4, 0, -3]])

b2 = ([9, 3, -2])

a3 = ([[3, -2, 5, 1],
      [-6, 4, -8, 1],
      [9, -6, 19, 1],
      [6, -4, -6, 15]])

b3 = ([7, -9, 23, 11])

#----------------------------Letra A-----------------------------------
#Verificando Existencia de Solução:
verificacao(a1, "a")
#GAUS:
#Transformando as matrizes em matriz triangular superior:
a_a1, b_b1 = gauss_sem_pivoteamento(a1, b1)
#Resolução:
x = triangular_superior(a_a1, b_b1)
print(x)
print()

#Fatoração LU:
#Obtendo os fatores LU
LU = fatoracao_LU(a1)
#Resolução
y = triangular_inferior(LU, b1)
print(y)
print()
x = triangular_superior(LU, y)
print(x)
cabecalho_resolucao()

#---------------------------------------------------------------------

#----------------------------Letra B-----------------------------------
#Verificando Existencia de Solução:
verificacao(a2, "b")
#GAUS:
#Transformando as matrizes em matriz triangular superior:
a_a2, b_b2 = gauss_sem_pivoteamento(a2, b2)
#Resolução:
x = triangular_superior(a_a2, b_b2)
print(x)
print()

#Fatoração LU:
#Obtendo os fatores LU
LU = fatoracao_LU(a2)
#Resolução
y = triangular_inferior(LU, b2)
print(y)
print()
x = triangular_superior(LU, y)
print(x)
cabecalho_resolucao()
#----------------------------------------------------------------------
#----------------------------Letra C-----------------------------------
#Verificando Existencia de Solução:
verificacao(a3, "c")
cabecalho_resolucao()
#----------------------------------------------------------------------