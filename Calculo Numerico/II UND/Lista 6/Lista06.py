import math
import numpy as np
from sympy import symbols
import sympy as sym

def cabecalho(questao, enunciado):
    return print(f'|{"-"*100}|\n|{" "*43}QUESTAO {questao}{" "*47}|\n|{"-"*100}|\n{enunciado}\n*{"-"*100}*')


def cabecalho_resolucao():
    return print(f'*{"-"*100}*')

def gaussPivoteamento(A, b):
    #Print
    print(f'{"-"*40} Eliminação de Gauss {"-"*40}')
    for k in range(len(A)):
        print(A[k])
    print()
    print(b)
    print()
    for i in range(len(A)):
        pivo = math.fabs(A[i][i])
        linhaPivo = i
        for j in range(i+1, len(A)):
            if math.fabs(A[j][i]) > pivo:
                pivo = math.fabs(A[j][i])
                linhaPivo = j
        if linhaPivo != i:
            linhaAuxiliar = A[i]
            A[i] = A[linhaPivo]
            A[linhaPivo] = linhaAuxiliar

            bAuxiliar = b[i]
            b[i] = b[linhaPivo]
            b[linhaPivo] = bAuxiliar
        for m in range(i+1, len(A)):
            multiplicador = A[m][i]/A[i][i]
            for n in range(i, len(A)):
                A[m][n] -= multiplicador*A[i][n]
            b[m] -= multiplicador*b[i]
        #PRINT
        for k in range(len(A)):
            print(A[k])
        print()
        print(b)


def coeficientes_grau2(A, b):
    print(f'{"-"*45} Coeficientes {"-"*45}')
    a2 = b[2]/A[2][2]
    a1 = (b[1]-(A[1][2]*a2))/A[1][1]
    a0 = (b[0]-(A[0][2]*a2)-(A[0][1]*a1))/A[0][0]
    print(f'a2 = {a2}\na1 = {a1}\na0 = {a0}')
    polinomio = [a0, a1, a2]

    print(f'{"-" * 45} Polinomio {"-" * 45}')
    sinal = list()
    for c in range(0, len(polinomio)):
        if polinomio[c] > 0:
            sinal.append('+')
        else:
            sinal.append('-')

    print(f'P2(x) = ', end='')
    if sinal[0] == '+':
        print(f'{polinomio[0]}', end='')
    else:
        print(f'{polinomio[0]}', end='')
    print(f' {sinal[1]} {abs(polinomio[1])}*x {sinal[2]} {abs(polinomio[2])}*x**2')

    return polinomio

def ponto_no_polinomio2(p2, x=0):
    px = p2[0]+(p2[1]*x)+(p2[2]*x*x)
    print(f'P2(x={x}) = {px}')
    return px


def coeficientes_grau1(a, b):
    c = ((b[1]-b[0])/(a[1]-a[0]))
    a0 = (b[0])-c*(a[0])
    a1 = c

    print(f'P1(x) = {a0}', end='')
    if a1 >=0:
        print(f' + {a1}*x')
    else:
        print(f' - {abs(a1)}*x')
    polinomio1 = [a0, a1]
    return polinomio1

def ponto_no_polinomio1(p1, x=0.0):
    px = p1[0]+(p1[1]*x)
    print(f'P1(x={x}) = {px}\n')
    return px


def polinomio_lagrange(X, FX):
    #X = X.copy()
    #FX = FX.copy()
    x = symbols('x')
    arraylen = len(X)
    L = []

    for i in range(arraylen):
        arrayaux = np.arange(arraylen)
        arrayaux = list(arrayaux)
        arrayaux.remove(i)

        numLi = 1
        denLi = 1

        for j in arrayaux:
            numLi = numLi * (x - X[j])
            denLi = denLi * (X[i] - X[j])

        Li = numLi/denLi
        L.append(sym.expand(Li))
    p = np.sum(FX*np.array(L))
    return p


def interpLagrange(xp,x,y,grau):
  yp = 0
  for k in range(0,grau+1):
      p = 1
      for j in range(0,grau+1):
          if k != j:
              p = p*(xp - x[j])/(x[k] - x[j])
      yp = yp + p * y[k]
  return yp


def interpNewton(x, y, xi=0.0):
    n = len(x)
    fdd = [[None for x in range(n)] for x in range(n)]

    for i in range(n):
        fdd[i][0] = y[i]

    for j in range(1, n):
        for i in range(n - j):
            fdd[i][j] = (fdd[i + 1][j - 1] - fdd[i][j - 1]) / (x[i + j] - x[i])

    # fdd_table = pd.DataFrame(fdd)
    # print(fdd_table)

    xterm = 1
    yint = fdd[0][0]
    for order in range(1, n):
        xterm = xterm * (xi - x[order - 1])
        yint = yint + fdd[0][order] * xterm

    return yint


def polinomio_newton(x, y):
    n = len(x)
    fdd = [[None for x in range(n)] for x in range(n)]

    for i in range(n):
        fdd[i][0] = y[i]

    for j in range(1, n):
        for i in range(n - j):
            fdd[i][j] = (fdd[i + 1][j - 1] - fdd[i][j - 1]) / (x[i + j] - x[i])

    print(f'P2(x) = {fdd[0][0]}', end='')
    if fdd[0][1] > 0:
        print(f' + {fdd[0][1]}*[x-({x[0]})]', end='')
    else:
        print(f' - {abs(fdd[0][1])}*[x-({x[0]})]', end='')
    if fdd[0][2] > 0:
        print(f' + {fdd[0][2]}*[x-({x[0]})]*[x-({x[1]})]')
    else:
        print(f' + {fdd[0][2]}*[x-({x[0]})]*[x-({x[1]})]')


#ENUNCIADOS
q01_a = """a) Encontre o polinômio interpolador de ordem 2 (Parábola) que ajusta os pontos utilizando o método 
de eliminação de Gauss para triangularizar o sistema de equações. Dica: Faça P₂(𝒙𝒾) = f(𝒙𝒾) = 𝒚𝒾 em 
cada ponto 𝒾 e depois triangularizar a matriz sanduíche do sistema para achar os coeficientes 𝑎₀, 𝑎₁ 
e 𝑎₂ do polinômio."""

q01_b = """b) Calcular o valor de P₂(5)."""

q01_c = """c) Encontre o polinômio interpolador de ordem 1 (reta) que ajusta os 1º e 3º pares de pontos da tabela.
Dica: Faça P₁(𝒙𝒾) = f(𝒙𝒾) = 𝒚𝒾 em cada ponto 𝒾 e depois triangularizar a matriz sanduíche do sistema 
para achar os coeficientes 𝑎₀ e 𝑎₁ do polinômio."""

q01_d = """d) Calcule o valor de P₁(5) e verifique se este valor é maior ou menor do que P₂(5) obtido no item b."""

q02_a = """a) Escreva o polinômio interpolador de Lagrange de ordem 2 para esse conjunto de pontos."""

q02_b = """b) Calcule P₂(1.5) e P₂(2.5)."""

q03_a = """a) Escreva o polinômio interpolador de Newton de ordem 2 para esse conjunto de pontos."""

q03_b = """b) Calcule P₂(1.5) e P₂(2.5)."""

#DADOS
#Q01:
a = [[1, 3, 9],
     [1, 9, 81],
     [1, 20, 400]]

b = [1.5, 4.5, 6.0]

x = [3, 20]

y = [1.5, 6.0]

#Q02:
X = [1.1, 2.2, 3.5]
FX = [10, 29, 90]

#Q03:
e = [1.1, 2.2, 3.5]
r = [10, 29, 90]

#QUESTAO-01_a
cabecalho("01", q01_a)
gaussPivoteamento(a, b)
p2 = coeficientes_grau2(a, b)
cabecalho_resolucao()
#QUESTAO-01_b
print(q01_b)
cabecalho_resolucao()
p2_5 = ponto_no_polinomio2(p2, x=5)
cabecalho_resolucao()
#QUESTAO-01_c
print(q01_c)
cabecalho_resolucao()
p1 = coeficientes_grau1(x, y)
cabecalho_resolucao()
#QUESTAO-01_d
print(q01_d)
cabecalho_resolucao()
p1_5 = ponto_no_polinomio1(p1, x=5)
print(f'Temos que: P2(x=5) = {p2_5} e P1(x=5) = {p1_5}\nLogo P2(x=5) > P1(x=5)')
cabecalho_resolucao()

#QUESTAO-02_a
cabecalho("02", q02_a)
p_lagrange = polinomio_lagrange(X, FX)
print(f'P2(x): {p_lagrange}')
cabecalho_resolucao()

#QUESTAO-02_b
print(q02_b)
cabecalho_resolucao()
px_1_5 = interpLagrange(1.5, X, FX, 2)
print(f'P₂(1.5) = {px_1_5}')
px_2_5 = interpLagrange(2.5, X, FX, 2)
print(f'P₂(2.5) = {px_2_5}')
cabecalho_resolucao()

#QUESTAO-03_a
cabecalho("03", q03_a)
polinomio_newton(e, r)
cabecalho_resolucao()
print(q02_b)
cabecalho_resolucao()
p_1_5 = interpNewton(e, r, 1.5)
print(f'P₂(1.5) = {p_1_5}')
p_2_5 = interpNewton(e, r, 2.5)
print(f'P₂(2.5) = {p_2_5}')
cabecalho_resolucao()