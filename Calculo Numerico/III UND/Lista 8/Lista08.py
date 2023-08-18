import math
import numpy as np

def cabecalho(questao, enunciado):
    return print(f'|{"-"*100}|\n|{" "*43}QUESTAO {questao}{" "*47}|\n|{"-"*100}|\n{enunciado}\n*{"-"*100}*')


def cabecalho_resolucao():
    return print(f'*{"-"*100}*')


#DADOS
q_01 = """Calcular o valor do coeficiente de determinação R² da equação exponencial e logarítmica apresentadas
na aula. Em seguida, justifique qual delas melhor se ajustou aos pontos."""


#Q01
cabecalho("01", q_01)
#exponencial
print("Equação exponencial: g3(x) = 2.37156*e^(0.3125*x)")
#gx1 = 2.37156*math.e**(0.3125*x1)
n1 = 4
x1 = [1, 2, 3, 4, 10]
y1 = [3, 5, 6, 8, 22]
lny1 = [1.0986, 1.6094, 1.7917, 2.0794, 6.5792]
x1y1 = [3, 10, 18, 32, 63]
x1lny1 = [1.0986, 3.2188, 5.3752, 8.3177, 18.0105]
x1_2 = [1, 4, 9, 16, 30]

SQReg1, SQTot1 = [], []
for c in range(0, n1):
    SQReg1.append(((2.37156*math.e**(0.3125*x1[c]))-(y1[4]/4))**2)
    SQTot1.append((lny1[c]-(y1[4]/4))**2)
print("\nSQReg1 =", SQReg1)
print("SQTot1 =", SQTot1)

a, b = 0, 0
for c in range(0, n1):
    a += SQReg1[c]
    b += SQTot1[c]
print("E_SQReg1 =", a)
print("E_SQTot1 =", b)
print("\nR²_exp =", (a/b))

#logaritmica
print("\nEquação logarítmica: g2(x) = 3.3833*Ln(x) + 2.8119")
#gx2 = 3.3833*Ln(x) + 2.8119
n1 = 4

lnx1 = [0, 0.6931, 1.0986, 1.3863, 3.178]
y1lnx1 = [0, 3.4655, 6.5916, 11.0904, 21.1475]
lnx1_2 = [0, 0.4804, 1.2069, 1.9219, 3.6092]

SQReg2, SQTot2 = [], []
for c in range(0, n1):
    SQReg2.append(((3.3833*math.log(x1[c], math.e)+2.8119)-(y1[4]/4))**2)
    SQTot2.append((lny1[c]-(y1[4]/4))**2)
print("\nSQReg2 =", SQReg2)
print("SQTot2 =", SQTot2)

a, b = 0, 0
for c in range(0, n1):
    a += SQReg2[c]
    b += SQTot2[c]
print("E_SQReg2 =", a)
print("E_SQTot2 =", b)
print("\nR²_ln =", (a/b))

print("""\nA equação exponencial se ajustou melhor aos pontos, pois:
                        
                        R²_exp > R²_ln""")
cabecalho_resolucao()

#Q02
cabecalho("02", "")
n = 7
x = [0, 1, 2, 3, 4, 5, 6, 21]
y = [32, 47, 65, 92, 132, 190, 275, 833]
print("n =", n)
print("\nx =", x)
print("y =", y)

lny = []
e = 0
for c in range(0, n):
    e += math.log(y[c], math.e)
    lny.append(math.log(y[c], math.e))
lny.append(e)
print("\nlny =", lny)

xy = []
e = 0
for c in range(0, n):
    e += x[c]*y[c]
    xy.append(x[c]*y[c])
xy.append(e)
print("xy =", xy)

xlny = []
e = 0
for c in range(0, n):
    e += x[c]*math.log(y[c], math.e)
    xlny.append(x[c]*math.log(y[c], math.e))
xlny.append(e)
print("xlny =", xlny)

x2 = []
e = 0
for c in range(0, n):
    e += x[c]**2
    x2.append(x[c]**2)
x2.append(e)
print("x² =", x2)

a = ((n*xlny[n])-(x[n]*lny[n]))/((n*x2[n])-((x[n])**2))
print(f"\nEq. (a) = ({n}*{xlny[n]} - {x[n]}*{lny[n]}) / ({n}*{x2[n]} - {x[n]}²)")
print("a =", a)

b = (((x[n]*xlny[n])-(lny[n]*x2[n]))/((x[n])**2-(n*x2[n])))
print(f"\nEq. (b) = ({x[n]}*{xlny[n]} - {lny[n]}*{x2[n]}) / ({x[n]}² - {n}*{x2[n]})")
print("b =", b)

print("\na)")
print(f"\nResposta: y = {math.e**b}*e^({a}*x)")

print("\nb) y(bactérias) = 2000")
print(f"\nln(2000/{math.e**b}) = {a}*x")
print(f"x = {math.log(2000/math.e**b)}/{a}")

print(f"\nResposta: x(horas) = {math.log(2000/math.e**b)/a}")
cabecalho_resolucao()