import numpy
import sys
from copy import deepcopy
import math

def cabecalho(questao, enunciado):
    return print(f'|{"-"*100}|\n|{" "*43}QUESTAO {questao}{" "*47}|\n|{"-"*100}|\n{enunciado}\n*{"-"*100}*')


def cabecalho_resolucao():
    return print(f'*{"-"*100}*')


def comparar(x, xk, eps):
    soma = 0
    zip_object = zip(x, xk)
    for list1_i, list2_i in zip_object:
        soma = soma + math.fabs(list1_i - list2_i)

    if (soma < eps):
        return True
    else:
        return False


def gauss_jacobi(A, b, maxiter, eps):
    n = len(b)
    sol = True
    x = b.copy()
    for i in list(range(1, n + 1, 1)):
        if (math.fabs(A[i - 1][i - 1]) > 0.0):
            x[i - 1] = b[i - 1] / A[i - 1][i - 1]
        else:
            sol = False
            break

    if (sol):
        print("Iteração: 1")
        print(f'M = {x}') #M = matriz iteração
        xk = x.copy()
        # maxiter = 10
        # eps     = 0.01
        iter = 0

        while (iter < maxiter):
            iter = iter + 1
            for i in list(range(1, n + 1, 1)):
                s = 0
                for j in list(range(1, n + 1, 1)):
                    if ((i - 1) != (j - 1)):
                        s = s + A[i - 1][j - 1] * x[j - 1]

                xk[i - 1] = (1 / A[i - 1][i - 1]) * (b[i - 1] - s)

            print(f'Iteração: {iter+1}')
            print(f'Mx = {xk}')
            if comparar(x, xk, eps):
                x = xk.copy()
                break
            x = xk.copy()
    print("\nSolução:\n|", end=' ')
    for c in range(0, len(x)):
        x[c] = round(x[c])
        print(f'x{c+1} = {x[c]}', end=' | ')
    print()
    return x


def gauss_seidel(A, b, maxiter, eps):
    n = len(b)
    sol = True
    x = b.copy()
    for i in list(range(1, n + 1, 1)):
        if (math.fabs(A[i - 1][i - 1]) > 0.0):
            x[i - 1] = b[i - 1] / A[i - 1][i - 1]
        else:
            sol = False
            break

    if (sol):
        print("Iteração: 1")
        print("M = ", x)
        xk = x.copy()
        # maxiter = 10
        # eps     = 0.01
        iter = 0

        while (iter < maxiter):
            iter = iter + 1
            for i in list(range(1, n + 1, 1)):
                s = 0
                for j in list(range(1, n + 1, 1)):
                    if ((i - 1) > (j - 1)):
                        s = s + A[i - 1][j - 1] * xk[j - 1]
                    elif ((i - 1) < (j - 1)):
                        s = s + A[i - 1][j - 1] * x[j - 1]

                xk[i - 1] = (1 / A[i - 1][i - 1]) * (b[i - 1] - s)

            print(f"Iteração: {iter+1}")
            print("Mk = ", xk)
            if comparar(x, xk, eps):
                x = xk.copy()
                break
            x = xk.copy()
    print("\nSolução:\n|", end=' ')
    for c in range(0, len(x)):
        x[c] = round(x[c])
        print(f'x{c + 1} = {x[c]}', end=' | ')
    print()
    return x


#ENUNCIADOS:
q01 = """Resolva os sistemas lineares abaixo usando os métodos iterativos de Gauss-Jacobi e Gauss-Seidel. 
Considere a precisão de ε = 5 x 10-2 = 0.05.

a. 
     1x1 + 3x2 + 1x3 = -2
     5x1 + 2x2 + 2x3 =  3
     0x1 + 6x2 + 8x3 = -6
     
b.     
     5x1 + 1x2 + 1x3 = 5
     3x1 + 4x2 + 1x3 = 6
     3x1 + 3x2 - 6x3 = 0"""

#Dados:
a1 = ([[1, 3, 1],
       [5, 2, 2],
       [0, 6, 8]])

b1 = ([-2, 3, -6])

a2 = ([[5, 1, 1],
       [3, 4, 1],
       [3, 3, 6]])

b2 = ([5, 6, 0])

#QUESTAO-01_a
cabecalho("01", q01)
print("""a. Método de Gauss Jacobi (com 10 iterações):

Por não se tratar de uma matriz diagonalmente dominante, a convergência
não será garantida para aplicação deste método.

Atendendo as solicitações imposta nos comentários do problema, serão realizadas
2 iterações com o método de gauss jacobi:
""")
gauss_jacobi(a1, b1, 1, 0.05)
print("""
a. Método de Gauss Seidel (com 10 iterações):

Por não se tratar de uma matriz diagonalmente dominante, a convergência
não será garantida para aplicação deste método.

Atendendo as solicitações imposta nos comentários do problema, serão realizadas
2 iterações com o método de gauss seidel:
""")
gauss_seidel(a1, b1, 1, 0.05)
cabecalho_resolucao()

#QUESTAO-01_b
print("""b. Método de Gauss Jacob (com 10 iterações):
""")
gauss_jacobi(a2, b2, 9, 0.05)
print("""
b. Método de Gauss Seidel (com 10 iterações):
""")
gauss_seidel(a2, b2, 9, 0.05)
cabecalho_resolucao()