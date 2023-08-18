import math
import numpy as np

def cabecalho(questao, enunciado):
    return print(f'|{"-"*100}|\n|{" "*43}QUESTAO {questao}{" "*47}|\n|{"-"*100}|\n{enunciado}\n*{"-"*100}*')


def cabecalho_resolucao():
    return print(f'*{"-"*100}*')

def polinomio(x1, x2, p, y1, y2):
    c = ((y2-y1)/(x2-x1))
    if x1>=0:
        print(f'p1(x) = {y1} + (x - {x1})*({y2} - {y1})/({x2} - {x1})')
    else:
        print(f'p1(x) = {y1} + (x + {abs(x1)})*({y2} - {y1})/({x2} - {x1})')
    p1 = y1+((p-x1)*(c))
    return p1

#DADOS
q_01 = """Parametros: f(x) = -(0.0213903743315508*x²) + (0.7566844919786097*x) - 0.5775401069518717
p = 5
x1 = 3   | x2 = 9
y1 = 1.5 | y2 = 4.5"""

q_02 = """Parametros: f(x) = (12.3543123543124*x²) - (23.4965034965035*x) + 20.8974358974359
p1 = 1.5
x1 = 1.1   | x2 = 2.2
y1 = 10 | y2 = 29

p2 = 2.5
x1 = 2.2 | x2 = 3.5
y1 = 29  | y2 = 90"""

q_03 = """Parametros: f(x) = 12.354312354312357*(x-1.1)*(x-2.2) + 17.27272727272727*(x-1.1) + 10
p1 = 1.5
x1 = 1.1   | x2 = 2.2
y1 = 10 | y2 = 29

p2 = 2.5
x1 = 2.2 | x2 = 3.5
y1 = 29  | y2 = 90"""

#QUESTAO 01
cabecalho("01", q_01)
px_1 = polinomio(3, 9, 5, 1.5, 4.5)
x = 5
fx_1 = -(0.0213903743315508*x*x)+(0.7566844919786097*x)-0.5775401069518717
print(f'\nf({x}) = {fx_1}')
print(f'p({x}) = {px_1}')
print(f'\nE({x}) = {abs(fx_1-px_1)}')
cabecalho_resolucao()

#QUESTAO 02
cabecalho("02", q_02)
px_2 = polinomio(1.1, 2.2, 1.5, 10, 29)
x = 1.5
fx_2 = (12.3543123543124*x*x) - (23.4965034965035*x) + 20.8974358974359
print(f'\nf({x}) = {fx_2}')
print(f'p({x}) = {px_2}')
print(f'\nE({x}) = {abs(fx_2-px_2)}\n')

px_3 = polinomio(2.2, 3.5, 2.5, 29, 90)
x = 2.5
fx_2 = (12.3543123543124*x*x) - (23.4965034965035*x) + 20.8974358974359
print(f'\nf({x}) = {fx_2}')
print(f'p({x}) = {px_3}')
print(f'\nE({x}) = {abs(fx_2-px_3)}')
cabecalho_resolucao()

#QUESTAO 03
cabecalho("03", q_03)
px_4 = polinomio(1.1, 2.2, 1.5, 10, 29)
x = 1.5
fx_3 = (12.354312354312357*(x-1.1)*(x-2.2)) + (17.27272727272727*(x-1.1)) + 10
print(f'\nf({x}) = {fx_3}')
print(f'p({x}) = {px_4}')
print(f'\nE({x}) = {abs(fx_3-px_4)}\n')

px_5 = polinomio(2.2, 3.5, 2.5, 29, 90)
x = 2.5
fx_3 = (12.354312354312357*(x-1.1)*(x-2.2)) + (17.27272727272727*(x-1.1)) + 10
print(f'\nf({x}) = {fx_3}')
print(f'p({x}) = {px_5}')
print(f'\nE({x}) = {abs(fx_3-px_5)}')
cabecalho_resolucao()

