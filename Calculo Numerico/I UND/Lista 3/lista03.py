#Aluno: Ricardo Teixeira Reale
from pylab import *

def cabecalho(questao, enunciado):
    return print(f'|{"-"*100}|\n|{" "*43}QUESTAO {questao}{" "*47}|\n|{"-"*100}|\n{enunciado}\n*{"-"*100}*')


def cabecalho_resolucao():
    return print(f'*{"-"*100}*')


def f(x):
    f = x**3 - x - 1
    return f


def df(x): #derivada f(x) = metodo de newton
  df = 3*(x**2) - 1
  return df


def g(x): #usado no método do ponto fixo
  g = pow((x+1), (1/3))
  return g


def metodo_bissecao(a=0.0, b=0.0, e=0.0):
    print('Método da Bisseção:')
    k = 1 #contador iterações
    x_old = (a+b)/2
    if f(a) * f(b) < 0:  # Indica f(x) contínua no intervalo [a,b]
            # Método da Bisseção: FASE 02
        x = (a + b) / 2  # raiz aproximada
        print(' - Tabelamento:')
        while (abs(f(x)) > e):  # raiz maior que a precisão indicada
            print(f'{" " * 5}[{a}, {b}]')
            x = (a + b) / 2
            x_old = a
            if f(a) * f(x) < 0:
                a = a
                b = x
            elif f(x) * f(b) < 0:
                a = x
                b = b
            k += 1
        print(f'{" " * 5}[{a}, {b}]')
        print('\n - Resultados:')
        print(f"     x' = {x}")
        print(f"     f(x') = {f(x)}")
        print(f"     Erro em x = {abs((x_old-x)/x)}")
        print(f"     Iterações = {k}\n")
    else:
        print("Não há raiz neste intervalo!")


def metodo_posicao_falsa(a=0.0, b=0.0, e=0.0):
    # Teorema de Bolzano: FASE 01
    print('Método da Posição Falsa:')
    if f(a) * f(b) < 0:
        #Método da Posicao Falsa: FASE 02
        x = (a*f(b)-b*f(a))/(f(b)-f(a)) #raiz aproximada
        k = 1
        x_old = 0.0
        print(' - Tabelamento:')
        while (abs(f(x)) >= e):
            print(f'{" "*5}[{a}, {b}]')
            x_old = x
            x = (a*f(b)-b*f(a))/(f(b)-f(a))
            #print(k, a, x, b, f(a), f(x), f(b))
            if f(a) * f(x) < 0:
                a = a
                b = x

            elif f(x) * f(b) < 0:
                a = x
                b = b

            k += 1
        print(f'{" " * 5}[{a}, {b}]')

        print('\n - Resultados:')
        print(f"     x' = {x}")
        print(f"     f(x') = {f(x)}")
        print(f"     Erro em x = {abs((x_old-x)/x)}")
        print(f"     Iterações = {k}\n")
    else:
        print("Não há raiz neste intervalo!\n")


def metodo_ponto_fixo(x0 = 0.0, e = 0.0): #x0 = chute inicial, e = precisao
  print(f'Método do Ponto Fixo:')
  k = 1
  x_old = x0 #para calcular erro relativo
  if ((abs(f(x0))) < e):
    x1 = x0
  else:
    print(' - Tabelamento:')
    x1 = g(x0)  # recebe g(x)
    while ((abs(f(x1))) >= e):
      x_old = x1
      print(f'{" " * 5}[{x1}]')
      if ((abs(f(x1))) < e) or ((abs(x1 - x0)) < e):
        x = x1
        break
      x0 = x1
      k += 1
      x1 = g(x0)
  print(f'{" " * 5}[{x1}]')

  print('\n - Resultados:')
  print(f"     x' = {x1}")
  print(f"     f(x') = {f(x1)}")
  print(f"     Erro em x = {abs((x_old-x1)/x1)}")
  print(f"     Iterações = {k}\n")


def metodo_newton(x0=0.0, e=0.0):
  print('Método de Newton-Raphson:')
  k = 1
  x_old = x0
  if (abs(f(x0))) < e:
    x1 = x0
  else:
    x1 = x0 - (f(x0)/df(x0))
    print(' - Tabelamento:')
    while (abs(f(x1))) > e:
      x_old = x1
      print(f'{" "*5}[{x1}]')
      if ((abs(f(x1))) < e) or ((abs(x1-x0)) < e):
        x1 = x1
        break
      x0 = x1
      k += 1
      x1 = x0 - (f(x0)/df(x0))
  print(f'{" " * 5}[{x1}]')

  print('\n - Resultados:')
  print(f"     x' = {x1}")
  print(f"     f(x') = {f(x1)}")
  print(f"     Erro em x = {abs((x_old-x1)/x1)}")
  print(f"     Iterações = {k}\n")


def metodo_secante(x0=0.0, x1=0.0, e=0.0):
  print('Método da Secante')
  k = 1
  x_old = x0
  if abs(f(x0)) < e:
    x2 = x0
  elif (abs(f(x1)) < e) or (abs(x1-x0) < e):
    x2 = x1
  else:
    x2 = (x0*f(x1) - x1*f(x0)) / (f(x1)-f(x0))

    print(' - Tabelamento:')
    while abs(f(x2)) > e:
      print(f'{" " * 5}[{x1}, {x2}]')
      if (abs(f(x2)) < e) or (abs(x2-x1) < e):
        x2 = x2
        break
      x0 = x1
      x1 = x2
      x_old = x1
      k += 1
      x2 = (x0*f(x1) - x1*f(x0)) / (f(x1)-f(x0))
  print(f'{" " * 5}[{x1}, {x2}]')

  print('\n - Resultados:')
  print(f"     x' = {x2}")
  print(f"     f(x') = {f(x2)}")
  print(f"     Erro em x = {abs((x_old-x2)/x2)}")
  print(f"     Iterações = {k}\n")


#ENUNCIADOS:
q01 = """a) Dos métodos numéricos estudados para encontrar zeros de funções quais necessitam que seja
definido um intervalo onde supostamente estaria o zero da função? 

b) Quais métodos precisam de 1 chute inicial para se encontrar o zero da função? 

c) Qual método exige 2 chutes iniciais?"""

q02 = """Qual dos métodos numéricos estudados para encontrar zeros de funções é necessário utilizar 
a derivada da função no processo iterativo?"""

q03 = """Considerando a função abaixo, identifique qual método convergiu mais rápido para encontrar a solução
aproximada e preencha a tabela com as informações solicitadas.

                             f(x) = x³-x-1; 𝞷 ∈ [1,2]; ℇ = 10⁻⁶"""


#QUESTA0-01:
cabecalho("01", q01)
print("""a) Método da Bisseção e Método da Posição Falsa.

b) Método do Ponto Fixo e Método de Newton-Raphson.

c) Método da Secante.""")
cabecalho_resolucao()

#QUESTAO-02:
cabecalho("02", q02)
print("""Método de Newton-Raphson.""")
cabecalho_resolucao()

#QUESTAO-03:
cabecalho("03", q03)
x = arange(-2.0, 2.0, 0.1)
plt.figure()
plt.grid()
plt.plot(x, f(x))
plt.show()

print("""Ao plotar o gráfico da função f(x) = x³-x-1, verifica-se visualmente que o intervalo [1,2] pode ser 
reduzido à [1,1.5] de modo a reduzir o número de iterações para determinação da raíz da função em análise.

Utilizando o intervalo de [1, 1.5] e precisão ℇ = 10⁻⁶ temos:
""")

metodo_bissecao(1, 1.5, 0.00001)
metodo_posicao_falsa(1, 1.5, 0.00001)
metodo_ponto_fixo(1, 0.00001)
metodo_newton(1.5, 0.00001)
metodo_secante(1, 1.5, 0.00001)
cabecalho_resolucao()

