#Aluno: Ricardo Teixeira Reale

def cabecalho(questao, enunciado):
    return print(f'|{"-"*100}|\n|{" "*43}QUESTAO {questao}{" "*47}|\n|{"-"*100}|\n{enunciado}\n*{"-"*100}*')


def cabecalho_resolucao():
    return print(f'*{"-"*100}*')


def f(x):
    f = x**3 - 9*x + 3
    #f_string = '[x³ - 9x + 3]'
    return f


def metodo_bissecao(a=0.0, b=0.0, e=0.0):
    #Teorema de Bolzano: FASE 01
    if f(a)*f(b) < 0: #Indica f(x) contínua no intervalo [a,b]
        #Método da Bisseção: FASE 02
        x = (a+b)/2 #raiz aproximada
        k = 0 #contador iterações
        while(abs(f(x)) > e): #raiz maior que a precisão indicada
            x = (a+b)/2
            #print(k, a, x, b, f(a), f(x), f(b))
            if f(a)*f(x) < 0:
                a = a
                b = x
            elif f(x)*f(b) < 0:
                a = x
                b = b
            k += 1
        print(f"Para a equação f(x) = [x³–9x+3] com intervalo [0,1] e precissão [e = 0.002] e através do Método da")
        print(f"Bissecção, a raiz aproximada [x'] encontrada após {k} iterações é igual a:\n")
        print(f"x' = {x};\n|f(x')| = {abs(f(x))} < e")
    else:
        print("Não há raiz neste intervalo!")


def metodo_posicao_falsa(a=0.0, b=0.0, e=0.0):
    # Teorema de Bolzano: FASE 01
    if f(a) * f(b) < 0:
        #Método da Posicao Falsa: FASE 02
        x = (a*f(b)-b*f(a))/(f(b)-f(a)) #raiz aproximada
        k = 0
        while (abs(f(x)) > e):
            x = (a*f(b)-b*f(a))/(f(b)-f(a))
            #print(k, a, x, b, f(a), f(x), f(b))
            if f(a) * f(x) < 0:
                a = a
                b = x
            elif f(x) * f(b) < 0:
                a = x
                b = b
            k += 1
        print(f"Para a equação f(x) = [x³–9x+3] com intervalo [0,1] e precissão [e = 0.002] e através do Método da")
        print(f"Posição Falsa, a raiz aproximada [x'] encontrada após {k} iterações é igual a:\n")
        print(f"x' = {x};\n|f(x')| = {abs(f(x))} < e")
    else:
        print("Não há raiz neste intervalo!")


#ENUNCIADOS:
q01 = """Como que uma máquina digital sabe que ela tem que parar de fazer uma determinada
conta num processo iterativo?"""

q02 = """Encontre a raiz da equação f(x) = [x³–9x+3] utilizando o método da bissecção e as condições:
Chute inicial: I = [0,1]
Precisão: ε = 2x10⁻³."""

q03 = """Agora utilize o método da posição falsa para encontrar a raiz da equação apresentada na
questão anterior."""

q04 = """Qual método convergiu mais rápido para encontrar a solução aproximada? Justifique.?"""

#QUESTA0-01:
cabecalho("01", q01)
print("""Existem três criterios de parada num processo iterativo:

I - |x' - R| < E;
II - |f(x')| < E;
III - Limitando iterações;

--> A primeira condição de parada é satisfeita caso o valor
em modulo da raiz aproximada (x') menos o valor da raiz real (R)
for menor que a precisão (E);  
--> A segunda condição é satisfeita caso o valor em modulo da função
no ponto cuja raiz é aproximada (f(x')) seja menor que o valor
da precisão (E);
--> A terceira condição é satisfeita ao impormos um número limite de
iterações ao algoritmo, limitando desta forma a quantidade de iterações;""")
cabecalho_resolucao()

#QUESTAO-02:
cabecalho("02", q02)
metodo_bissecao(0, 1, 0.002)
cabecalho_resolucao()

#QUESTAO-03:
cabecalho("03", q03)
metodo_posicao_falsa(0, 1, 0.002)
cabecalho_resolucao()

#QUESTAO-04:
cabecalho("04", q04)
print("""Ao rodar parte do script e analisando os valores obtidos para o número de iterações de cada metodo
numérico avaliado anteriormente, pude notar que o Método da Posição Falsa convergiu mais rápido
visto que:

Método da Posição Falsa - Num. Iterações [k] = 3
Método da Bissecção - Num. Iterações [k] = 11

Deste modo o Método da Posição Falsa convergiu mais rápido para encontrar a solução da raíz aproximada""")
cabecalho_resolucao()




