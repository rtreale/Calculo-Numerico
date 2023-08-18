import sympy
from matplotlib import pyplot

def tabelamento(n, x, y): #FUNCAO PARA TABELAMENTO, RETORNA LISTA COM VALORES: [[X];[Y];[XY];[XX]]
    xy, xx = [], []
    for c in range(0, n):   #LAÇO DE REPETIÇÃO P/ CÁLCULO DE XY E XX
        xy.append(x[c] * y[c])
        xx.append(x[c] * x[c])
    tabelamento = []
    tabelamento.append(x)   #PREENCHIMENTO DA LISTA...
    tabelamento.append(y)   #PREENCHIMENTO DA LISTA...
    tabelamento.append(xy)  #PREENCHIMENTO DA LISTA...
    tabelamento.append(xx)  #PREENCHIMENTO DA LISTA...
    return tabelamento


def MMQ_linear(tabelamento): #FUNÇÃO PARA CÁLCULO DOS COEFICIENTES ANGULAR (a) e LINEAR (b) P/ EQ. DA RETA [y = ax + b]
    n = len(tabelamento[0])
    a = (n*sum(tabelamento[2])-sum(tabelamento[0])*sum(tabelamento[1]))/(n*sum(tabelamento[3])-sum(tabelamento[0])**2)                   #COEF. ANGULAR
    b = (sum(tabelamento[0])*sum(tabelamento[2])-sum(tabelamento[1])*sum(tabelamento[3]))/(sum(tabelamento[0])**2-n*sum(tabelamento[3])) #COEF. LINEAR
    MMQ_linear = []
    MMQ_linear.append(a)   #PREENCHIMENTO DA LISTA...
    MMQ_linear.append(b)   #PREENCHIMENTO DA LISTA...
    return MMQ_linear   #RETORNA LISTA COM VALORES DOS COEFICIENTES [a, b]


#PROGRAMA PRINCIPAL ----------------------------------------------------------------------------------------------------
#ENTRADA DE DADOS: (DADOS JÁ DEFINIDOS NA QUESTÃO)
peso = [79, 69, 70, 81, 61, 63, 79, 71, 73] #UND = [Kg]
altura = [183, 173, 168, 188, 158, 163, 193, 163, 178] #UND = [cm]

#TABELAMENTO E CALCULO DOS COEFICIENTES DA EQ. DA RETA [y = ax + b] ----------------------------------------------------
n = 9   #QNTD. DE DADOS
tabelamento_1 = tabelamento(n, altura, peso) #1ºTABELAMENTO (x=altura; y=peso) :return [x; y; xy; xx]
tabelamento_2 = tabelamento(n, peso, altura) #2ºTABELAMENTO (x=peso; y=altura) :return [x; y; xy; xx]

c1 = MMQ_linear(tabelamento_1) #LISTA C/ COEF. ANG.(a) e LIN.(b) DA EQ. DA RETA(y=ax+b) P/ 1ºTABELAMENTO
c2 = MMQ_linear(tabelamento_2) #LISTA C/ COEF. ANG.(c) e LIN.(d) DA EQ. DA RETA(y=cx+d) P/ 2ºTABELAMENTO

x = sympy.symbols('x')
eq_1 = c1[0]*x+c1[1]
eq_2 = c2[0]*x+c2[1]
#-----------------------------------------------------------------------------------------------------------------------

#EXIBIÇÃO DOS DADOS (PRINTS) -------------------------------------------------------------------------------------------
#a) --------------------------------------------------------------------------------------------------------------------
print(f"a) {'-'*100}")
print(f"\nGráfico de Dispersão (Altura x Peso):\n")
pyplot.scatter(altura, peso)
pyplot.title('Gráfico de Dispersão\n(Altura x Peso)')
pyplot.xlabel('Altura [cm]')
pyplot.ylabel('Peso [Kg]')
pyplot.show()
print(f"\nGráfico de Dispersão (Peso x Altura):\n")
pyplot.scatter(peso, altura)
pyplot.title('Gráfico de Dispersão\n(Peso x Altura)')
pyplot.xlabel('Peso [Kg]')
pyplot.ylabel('Altura [cm]')
pyplot.show()

#b) --------------------------------------------------------------------------------------------------------------------
print(f"\nb) {'-'*100}")
print(f"\n{' '*10}{'-'*51}")
print(f"{' '*10}|{' '*10}1º TABELAMENTO: peso = f(altura){' '*7}|\n{' '*10}|{' '*10}x = altura [cm]; y = peso [Kg]"
      f"{' '*9}|")
print(f"{' '*10}{'-'*51}")
print(f"{' '*10}|     X     |     Y     |     XY     |     XX     |")
print(f"{' '*10}{'-'*51}")
for c in range(0, len(tabelamento_1[0])):
    print(f"{' '*10}|{' '*4}{tabelamento_1[0][c]:3}{' '*4}|", end="")
    print(f"{' '*5}{tabelamento_1[1][c]:2}{' '*4}|", end="")
    print(f"{' '*3}{tabelamento_1[2][c]:5}{' '*4}|", end="")
    print(f"{' '*3}{tabelamento_1[3][c]:5}{' '*4}|")
    print(f"{' '*10}{'-'*51}")
print(f"{' '*10}|{' '*11}|{' '*11}|{' '*12}|{' '*12}|")
print(f"\033[4mSOMATÓRIO\033[m:|{' '*3}\033[4;31m{sum(tabelamento_1[0])}\033[m{' '*4}|{' '*4}\033[4;35m"
      f"{sum(tabelamento_1[1])}\033[m{' '*4}|{' '*2}\033[4;36m{sum(tabelamento_1[2])}\033[m{' '*4}|{' '*2}\033[4;34m"
      f"{sum(tabelamento_1[3])}\033[m{' '*4}|")
print(f"{' '*10}|{' '*11}|{' '*11}|{' '*12}|{' '*12}|")
print(f"{' '*10}{'-'*51}\n")

print(f"Determinando os coeficientes \033[1;33ma\033[m, \033[1;32mb\033[m para determinação da equação da reta [y = "
      f"\033[1;33ma\033[mx + \033[1;32mb\033[m] com \033[1;37mn = {n}\033[m:")
print(f"\n{' '*7}(\033[;37m{n}\033[m*\033[;36m{sum(tabelamento_1[2])}\033[m - \033[;31m{sum(tabelamento_1[0])}\033[m"
      f"*\033[;35m{sum(tabelamento_1[1])}\033[m)", end="")
print(f"{' '*22}(\033[;31m{sum(tabelamento_1[0])}\033[m*\033[;36m{sum(tabelamento_1[2])}\033[m - \033[;35m"
      f"{sum(tabelamento_1[1])}\033[m*\033[;34m{sum(tabelamento_1[3])}\033[m)")
print(f"  \033[1;33ma\033[m = --------------------- = \033[1;33m{c1[0]:.4f}\033[m{' '*10}\033[1;32mb\033[m "
      f"= -------------------------- = \033[1;32m{c1[1]:.4f}\033[m")
print(f"{' '*7}(\033[;37m{n}\033[m*\033[;34m{sum(tabelamento_1[3])}\033[m - (\033[;31m{sum(tabelamento_1[0])}\033[m)²)"
      f"", end="")
print(f"{' '*26}((\033[;31m{sum(tabelamento_1[0])}\033[m)² - \033[;37m{n}\033[m*\033[;34m{sum(tabelamento_1[3])}"
      f"\033[m)")
print(f"\n|{'-'*65}|")
print(f"|   Equação da reta: \033[1;7my = {eq_1}\033[m   |")
print(f"|{'-'*65}|")

#c) --------------------------------------------------------------------------------------------------------------------
print(f"\nc) {'-'*100}")
print(f"\n{' '*59}|{'-'*25}|")
print(f"f(175[cm]) = ax + b = ({c1[0]:.4f}*175 - {abs(c1[1]):.4f})    ---------> | \033[1;7mf(175[cm]) = "
      f"{c1[0]*175+c1[1]:.2f} [Kg]\033[m |")
print(f"{' '*59}|{'-'*25}|")

print()
print(f"{' '*12}(y - b)", end="")
print(f"{' '*3}(80 + {abs(c1[1]):.4f}){' '*23}|{'-'*25}|")
print(f"y(80[Kg]) = ------- = --------------{' '*8}    ---------> | \033[1;7my(80[Kg]) = {(80-c1[1])/c1[0]:.2f}"
      f" [cm]\033[m |")
print(f"{' '*15}a{' '*10}{c1[0]:.4f}{' '*27}|{'-'*25}|")

#d) --------------------------------------------------------------------------------------------------------------------
print(f"\nd) {'-'*100}")
print(f"\n{' '*10}{'-'*51}")
print(f"{' '*10}|{' '*10}2º TABELAMENTO: altura = f(peso){' '*7}|\n{' '*10}|{' '*10}x = altura [cm]; y = peso [Kg]"
      f"{' '*9}|")
print(f"{' '*10}{'-'*51}")
print(f"{' '*10}|     X     |     Y     |     XY     |     XX     |")
print(f"{' '*10}{'-'*51}")
for c in range(0, len(tabelamento_2[0])):
    print(f"{' '*10}|{' '*4}{tabelamento_2[0][c]:3}{' '*4}|", end="")
    print(f"{' '*4}{tabelamento_2[1][c]:2}{' '*4}|", end="")
    print(f"{' '*3}{tabelamento_2[2][c]:5}{' '*4}|", end="")
    print(f"{' '*3}{tabelamento_2[3][c]:5}{' '*4}|")
    print(f"{' '*10}{'-'*51}")
print(f"{' '*10}|{' '*11}|{' '*11}|{' '*12}|{' '*12}|")
print(f"\033[4mSOMATÓRIO\033[m:|{' '*4}\033[4;31m{sum(tabelamento_2[0])}\033[m{' '*4}|{' '*3}"
      f"\033[4;35m{sum(tabelamento_2[1])}\033[m{' '*4}|{' '*2}\033[4;36m{sum(tabelamento_2[2])}\033[m"
      f"{' '*4}|{' '*3}\033[4;34m{sum(tabelamento_2[3])}\033[m{' '*4}|")
print(f"{' '*10}|{' '*11}|{' '*11}|{' '*12}|{' '*12}|")
print(f"{' '*10}{'-'*51}\n")


print(f"Determinando os coeficientes \033[1;33ma\033[m, \033[1;32mb\033[m para determinação da equação da reta "
      f"[y = \033[1;33ma\033[mx + \033[1;32mb\033[m]: com \033[1;37mn = {n}\033[m:")
print(f"\n{' '*7}(\033[;37m{n}\033[m*\033[;36m{sum(tabelamento_2[2])}\033[m - \033[;31m{sum(tabelamento_2[0])}\033[m*"
      f"\033[;35m{sum(tabelamento_2[1])}\033[m)", end="")
print(f"{' '*22}(\033[;31m{sum(tabelamento_2[0])}\033[m*\033[;36m{sum(tabelamento_2[2])}\033[m - "
      f"\033[;35m{sum(tabelamento_2[1])}\033[m*\033[;34m{sum(tabelamento_2[3])}\033[m)")
print(f"  \033[1;33ma\033[m = --------------------- = \033[1;33m{c2[0]:.4f}\033[m{' '*10}\033[1;32mb\033[m "
      f"= -------------------------- = \033[1;32m{c2[1]:.4f}\033[m")
print(f"{' '*7}(\033[;37m{n}\033[m*\033[;34m{sum(tabelamento_2[3])}\033[m - (\033[;31m{sum(tabelamento_2[0])}\033[m)²)"
      f"", end="")
print(f"{' '*26}((\033[;31m{sum(tabelamento_2[0])}\033[m)² - \033[;37m{n}\033[m*"
      f"\033[;34m{sum(tabelamento_2[3])}\033[m)")
print(f"\n|{'-'*65}|")
print(f"|   Equação da reta: \033[1;7my = {eq_2}\033[m    |")
print(f"|{'-'*65}|")

#e) --------------------------------------------------------------------------------------------------------------------
print(f"\ne) {'-'*100}")
print(f"\n{' '*12}(y - b)", end="")
print(f"{' '*3}(175 - {abs(c2[1]):.4f}){' '*23}|{'-'*25}|")
print(f"y(175[cm]) = ------- = --------------{' '*8}    ---------> | \033[1;7my(175[cm]) = "
      f"{(175-c2[1])/c2[0]:.2f} [Kg]\033[m |")
print(f"{' '*16}a{' '*10}{c2[0]:.4f}{' '*27}|{'-'*25}|")
print()
print(f"\n{' '*59}|{'-'*25}|")
print(f"f(80[Kg]) = ax + b = ({c2[0]:.4f}*175 + {c2[1]:.4f})     ---------> | \033[1;7mf(80[Kg]) = "
      f"{c2[0]*80+c2[1]:.2f} [cm]\033[m |")
print(f"{' '*59}|{'-'*25}|")

#f) --------------------------------------------------------------------------------------------------------------------
print(f"\nf) {'-'*100}")
print(f"\nGráfico com Equações das letras (b; d):\n")
p1 = sympy.plot(eq_1, (x, -100, 100), line_color='red', title='Equação B (Azul) e Equação D (Vermelho)', ylabel='',show=False)
p2 = sympy.plot(eq_2, (x, -100, 100), line_color='blue', ylabel='',show=False)
p1.append(p2[0])
p1.show()
#EOF ^.^ ---------------------------------------------------------------------------------------------------------------