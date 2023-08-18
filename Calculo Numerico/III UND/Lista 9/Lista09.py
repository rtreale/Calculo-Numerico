import math
import numpy as np

def cabecalho(questao, enunciado):
    return print(f'|{"-"*100}|\n|{" "*43}QUESTAO {questao}{" "*47}|\n|{"-"*100}|\n{enunciado}\n*{"-"*100}*')


def cabecalho_resolucao():
    return print(f'*{"-"*100}*')

#-------------------------Q01----------------------------
def f1(x):
  y = (x**2)-math.exp(x)
  return y


def df1(x):
  z = 2-(math.exp(x))
  return z


def trapezio(inf, sup, f):
  h = sup - inf
  b = (f(inf)+f(sup))/2
  y = b*h
  return y


def et(inf, sup, df):
  maior = []
  for c in range(inf, sup+1):
    maior.append(math.fabs(df(c)))
  max_ = max(maior)
  et = ((sup-inf)**3/12)*max_
  return et
#-----------------------------------------------------------

#----------------------Q02----------------------------------
def f2(x):
  y = (6*x-5)**(1/2)
  return y


def df2(x):
  y = -9*((6*x-5)**(-3/2))
  return y


def trapezioR(inf, sup, n, f):
  h = (sup-inf)/n
  #print("h =", h)
  soma = 0.0
  for c in np.arange(inf+h, sup, h):
    #print(c)
    soma += f(c)
  y = (h/2)*(f(inf)+f(sup)+(2*soma))
  return y


def etr(inf, sup, n):
  aux = et(inf, sup, df2)
  etr = aux*(1/(n**2))
  return etr
#----------------------------------------------------------

#--------------------------Q03-----------------------------
def f3(x):
  #y = pow(x, -2)
  y = math.exp(x)
  return y


def df3(x):
  #y = 120*x**-6
  y = math.exp(x)
  return y


def simpsonR(inf, sup, i, f):
  h = (sup-inf)/i
  x = []
  for c in np.arange(inf, sup+h, h):
    x.append(c)

  maior_par = 0
  for c in range(2, len(x)-1, 2):
    maior_par += f(x[c])

  maior_impar = 0
  for c in range(1, len(x)-1, 2):
    maior_impar += f(x[c])

  isr = (h/3)*(f(inf)+f(sup)+(2*maior_par)+(4*maior_impar))
  return isr


def esr(inf, sup, i, df):
  n = i/2
  maior = []
  for c in range(inf, sup+1):
    maior.append(math.fabs(df(c)))
  max_ = max(maior)
  #print(max_)

  esr = ((sup-inf)**5)*(max_/(2880*(n**4)))
  return esr


def m(inf, sup, i, p, df):
  maior = []
  for c in range(inf, sup+1):
    maior.append(math.fabs(df(c)))
  max_ = max(maior)
  #print(max_)
  n = ((sup-inf)**5*max_/(2800*p))**(1/4)
  m = round(2*n)
  return m
#----------------------------------------------------------

#ENUNCIADOS
q_01 = """Calcule o valor numérico das integrais abaixo pelo método do trapézio e estime o erro do método:"""

q_02 = """a) Calcular f(x) = (6x-5)^(1/2) c/ {x0:1; xn:9}. Empregando o método dos trapézios com 8 repetições.

b) Determine a estimativa para o erro (ETR) nesse caso.

c) Quantas subdivisões devemos ter para que o erro seja menor do que 10^(-4)."""

q_03 = """a) Calcule uma aproximação para I usando 10 subintervalos e a regra de 1/3 de Simpson Repetida.
Estime o erro cometido.

b) Qual o número mínimo de subdivisões de modo que o erro seja inferior a (10^-3)>"""

#QUESTAO 01
cabecalho("01", q_01)
print("IT =", trapezio(5, 10, f1))
print("ET <=", et(5, 10, df1))
cabecalho_resolucao()

#QUESTAO 02
cabecalho("02", q_02)
i = 8           #iteracoes
n = 10**-4      #precisao
print("a) ITR =", trapezioR(1, 9, i, f2))
print("b) ETR <=", etr(1, 9, i))   #ETR = ET*(1/(n**2))
aux = (et(1, 9, df2)*(1/n))**(1/2)
print("c) n =", round(aux))
cabecalho_resolucao()

#QUESTAO 03
cabecalho("03", q_03)
i = 10      #intervalos
print("a) ISR =", simpsonR(0, 1, i, f3))
print("   ESR =", esr(0, 1, i, df3))
print("\nb) m =", m(0, 1, i, 10**-3, df3))
cabecalho_resolucao()