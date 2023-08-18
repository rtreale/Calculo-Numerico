#Aluno: Ricardo Teixeira Reale
import numpy as np
import string
import sys


def cabecalho(questao, enunciado):
    return print(f'|{"-"*100}|\n|{" "*43}QUESTAO {questao}{" "*47}|\n|{"-"*100}|\n{enunciado}\n*{"-"*100}*')

def cabecalho_resolucao():
    return print(f'*{"-"*100}*')

#DECIMAL PARA BINARIO - QUESTAO-01
def dec2bin(*valor):
    cont1 = 0
    while cont1 < len(valor):
        decimal = np.format_float_scientific(valor[cont1], precision=sys.float_info.dig, unique=False)  # COLOCANDO VALOR EM NOTACAO CIENTIFICA - STRING
        #REORDENDANDO STRING EM LISTA P/ MANIPULACAO DO PONTO FLUTUANTE
        indices = list()
        indices.append(decimal[0])  # O PRIMEIRO VALOR É SEMPRE UM NUM INTEIRO DEVIDO CONVERSAO VIA np.format_scientific
        pos_e = decimal.find("e") #POSICAO e (base)
        mantissa = (pos_e) - 2      #TAMANHO MANTISSA
        # PREENCHENDO LISTA COM A MANTISSA
        for x in range(0, mantissa):
            indices.append(decimal[x + 2])
        # ADICIONANDO O PONTO FLUTUANTE
        if (decimal[pos_e + 1]) == "+":  # EXPOENTE POSITIVO
            exp = int(decimal[pos_e + 2:])
            pos_ponto = 1 + exp
            indices.insert(pos_ponto, ".")
        else:  # EXPOENTE NEGATIVO
            exp = int(decimal[pos_e + 2:])
            for c in range(0, exp):
                indices.insert(c, '0')
            pos_ponto = 1
            indices.insert(pos_ponto, ".")

        #PARTE INTEIRA - (INT) --------------------------------------------------------------------------*/
        #CONVERTENDO LISTA EM STRING UNICA - PARTE INTEIRA
        parte_inteira = ""
        for x in range(0, pos_ponto):
            parte_inteira += indices[x]
        #CONVERTENDO STRING EM INT - PARTE INTEIRA
        parte_inteira = int(parte_inteira)
        #CONVERTENDO INT EM BINARIO - PARTE INTEIRA
        bin_int = bin(parte_inteira)  # RESULTADO CONVERSAO INTEIRO
        #------------------------------------------------------------------------------------------------*/

        #PARTE FLUTUANTE - (FLOAT) ----------------------------------------------------------------------*/
        #CONVERTENDO LISTA EM STRING UNICA - PARTE FLUTUANTE
        parte_float = ""
        for x in range(pos_ponto+1, len(indices)):
            parte_float += indices[x]
        #CONVERTENDO STRING EM FLOAT - PARTE FLUTUANTE
        parte_float = float(parte_float) / (10**len(parte_float))
        #CALCULANDO A FRACAO EM BINARIO
        indices_float = list()
        if indices_float == 0:
            indices_float.append('0')
        else:
            a = parte_float
            for x in range(0, sys.float_info.dig):
                a *= 2
                indices_float.append(str(a)[0])
                if a > 1:
                    a -= 1
                if a == 0.0:
                    break
        #CONVERTENDO LISTA EM STRING UNICA - LISTA bin_float
        bin_float = ""
        for x in range(0, len(indices_float)):
            bin_float += indices_float[x]
        #-------------------------------------------------------------------------------------------*/

        #SAIDA:
        if (len(bin_float) == 1) and (bin_float[0] == '0'):
            print(f'{string.ascii_lowercase[cont1]}. {bin_int[2:]}')
        else:
            print(f'{string.ascii_lowercase[cont1]}. {bin_int[2:]}.{bin_float}')

        cont1 += 1

#BINÁRIO PARA DECIMAL - QUESTAO-02
def bin2dec(*valor):
    #VERIFICA VALORES PRESENTES NA TUPLA (*VALOR)
    cont1 = 0
    while cont1 < len(valor):
        #VERIFICA O TIPO DE DADO: - INT
        if type(valor[cont1]) == int:
            #BIN TO INT
            bin = str(valor[cont1])
            bin2dec_int = bin[::-1] #REORDENANDO A PARTE INTEIRA DA LISTA
            dec_int = 0  #VALOR DECIMAL A SER EXIBIDO APÓS CONVERSÃO
            power = 0   #EXPOENTE
            for num in bin2dec_int:
                if num == '1':
                    dec_int += 2**power
                power += 1
            decimal = int(dec_int)
            print(f'{string.ascii_lowercase[cont1]}. ({decimal})')
        #VERIFICA O TIPO DE DADO: - FLOAT
        elif type(valor[cont1] == float):
            #BIN TO INT
            bin_int = str(valor[cont1]).split('.')[0]
            bin2dec_float = str(valor[cont1]).split('.')[1]
            bin2dec_int = bin_int[::-1]
            dec_int = 0
            power = 0
            for num in bin2dec_int:
                if num == '1':
                    dec_int += 2**power
                power += 1
            #BIN TO FLOAT
            dec_float = 0
            power2 = -1
            for num in bin2dec_float:
                if num == '1':
                    dec_float += 2**power2
                power2 -= 1
            # SAIDA
            decimal = int(dec_int) + float(dec_float)
            print(f'{string.ascii_lowercase[cont1]}. ({decimal})')
        else:
            print(':error')
        cont1 += 1

#NORMALIZACAO DE FLOAT - QUESTAO-03
def normalizacao_float(*valor, base):
    #VERIFICA VALORES PRESENTES NA TUPLA (*VALOR)
    cont1 = 0
    while cont1 < len(valor):
        #A FUNCAO np.format_float_scientific PERMITE TRATAR OS VALORES COMO FLUTUANTE PADRAO IEE 754
        #A FUNCAO sys DEFINE OS PARAMETROS NECESSARIOS DE PRECISAO ENTRE OUTROS P/ TIPO FLOAT
        num = np.format_float_scientific(valor[cont1], precision=sys.float_info.dig, exp_digits=sys.float_info.max_exp)
        sinal_expoente = num.find('e') + 1  # LOCALIZAR POSICAO DO EXPOENTE NA STRING - num

        """
        #DEBUGGER
        print('DEBUGGER')
        for x in range(0, len(num)):
            print(num[x], end="")

        #INDICES MANIPULACAO DA STRING - num (CASO NECESSARIO)
        ponto_flutuante = num.find('.')
        expoente = num.find('e')
        sinal_expoente = num.find('e') + 1
        #mantissa = len(num[ponto_flutuante+1:expoente-1])
        #print(ponto_flutuante, expoente, sinal_expoente, mantissa)
        """

        if num[sinal_expoente] == '+':
            # print('positive') #APAGAR
            print(f'{string.ascii_lowercase[cont1]}. 0.{num[0]}', end="")
            for x in range(2, sinal_expoente - 1):
                print(num[x], end="")
            print(f'*{base}^({num[sinal_expoente]}{int(num[sinal_expoente + 1:]) + 1})')
        else:
            # print('negative') #APAGAR
            print(f'{string.ascii_lowercase[cont1]}. 0.{num[0]}', end="")
            for x in range(2, sinal_expoente - 1):
                print(num[x], end="")
            print(f'*{base}^({num[sinal_expoente]}{int(num[sinal_expoente + 1:]) - 1})')
        cont1 += 1

#NORMALIZACAO DE FLOAT 4 DIGITOS - QUESTAO-05
def normalizacao_float_4dig(*valor, base):
    # VERIFICA VALORES PRESENTES NA TUPLA (*VALOR)
    cont1 = 0
    while cont1 < len(valor):
        # A FUNCAO np.format_float_scientific PERMITE TRATAR OS VALORES COMO FLUTUANTE PADRAO IEE 754
        # A FUNCAO sys DEFINE OS PARAMETROS NECESSARIOS DE PRECISAO ENTRE OUTROS P/ TIPO FLOAT
        num = np.format_float_scientific(valor[cont1], precision=3, exp_digits=sys.float_info.max_exp)
        sinal_expoente = num.find('e') + 1  # LOCALIZAR POSICAO DO EXPOENTE NA STRING - num

        """
        #DEBUGGER
        print('DEBUGGER')
        for x in range(0, len(num)):
            print(num[x], end="")

        #INDICES MANIPULACAO DA STRING - num (CASO NECESSARIO)
        ponto_flutuante = num.find('.')
        expoente = num.find('e')
        sinal_expoente = num.find('e') + 1
        mantissa = len(num[ponto_flutuante+1:expoente-1])
        #print(ponto_flutuante, expoente, sinal_expoente, mantissa)
        """

        if num[sinal_expoente] == '+':
            # print('positive') #APAGAR
            print(f'{string.ascii_lowercase[cont1]}. 0.{num[0]}', end="")
            for x in range(2, sinal_expoente - 1):
                print(num[x], end="")
            print(f'*{base}^({num[sinal_expoente]}{int(num[sinal_expoente + 1:]) + 1})')
        else:
            # print('negative') #APAGAR
            print(f'{string.ascii_lowercase[cont1]}. 0.{num[0]}', end="")
            for x in range(2, sinal_expoente - 1):
                print(num[x], end="")
            print(f'*{base}^({num[sinal_expoente]}{int(num[sinal_expoente + 1:]) - 1})')

        cont1 += 1

#EXPOENTE MAX E MIN (-2<E<2) - QUESTAO-06
def exp_max_e_min(*valor, base):
    cont1 = 0
    while cont1 < len(valor):
        # A FUNCAO np.format_float_scientific PERMITE TRATAR OS VALORES COMO FLUTUANTE PADRAO IEE 754
        # A FUNCAO sys DEFINE OS PARAMETROS NECESSARIOS DE PRECISAO ENTRE OUTROS P/ TIPO FLOAT
        num = np.format_float_scientific(valor[cont1], precision=sys.float_info.dig, exp_digits=sys.float_info.max_exp)
        sinal_expoente = num.find('e') + 1  # LOCALIZAR POSICAO DO EXPOENTE NA STRING - num

        """
        #DEBUGGER
        print('DEBUGGER')
        for x in range(0, len(num)):
            print(num[x], end="")

        #INDICES MANIPULACAO DA STRING - num (CASO NECESSARIO)
        ponto_flutuante = num.find('.')
        expoente = num.find('e')
        #mantissa = len(num[ponto_flutuante+1:expoente-1])
        #print(ponto_flutuante, expoente, sinal_expoente, mantissa)
        """

        expoente = 0
        if num[sinal_expoente] == '+':
            expoente = int(num[sinal_expoente+1:]) + 1
        elif num[sinal_expoente] == '-':
            expoente = -int(num[sinal_expoente+1:]) - 1

        if expoente > 2:
            if num[sinal_expoente] == '+':
                # print('positive') #APAGAR
                print(f'{string.ascii_lowercase[cont1]}. 0.{num[0]}', end="")
                for x in range(2, sinal_expoente - 1):
                    print(num[x], end="")
                print(f'*{base}^({num[sinal_expoente]}{int(num[sinal_expoente+1:]) + 1}) - OVERFLOW')
            else:
                # print('negative') #APAGAR
                print(f'{string.ascii_lowercase[cont1]}. 0.{num[0]}', end="")
                for x in range(2, sinal_expoente - 1):
                    print(num[x], end="")
                print(f'*{base}^({num[sinal_expoente]}{int(num[sinal_expoente + 1:]) - 1}) - OVERFLOW')

        elif expoente < 2:
            if num[sinal_expoente] == '+':
                # print('positive') #APAGAR
                print(f'{string.ascii_lowercase[cont1]}. 0.{num[0]}', end="")
                for x in range(2, sinal_expoente - 1):
                    print(num[x], end="")
                print(f'*{base}^({num[sinal_expoente]}{int(num[sinal_expoente+1:]) + 1}) - UNDERFLOW')
            else:
                # print('negative') #APAGAR
                print(f'{string.ascii_lowercase[cont1]}. 0.{num[0]}', end="")
                for x in range(2, sinal_expoente - 1):
                    print(num[x], end="")
                print(f'*{base}^({num[sinal_expoente]}{int(num[sinal_expoente + 1:]) - 1}) - UNDERFLOW')

        else:
            if num[sinal_expoente] == '+':
                # print('positive') #APAGAR
                print(f'{string.ascii_lowercase[cont1]}. 0.{num[0]}', end="")
                for x in range(2, sinal_expoente - 1):
                    print(num[x], end="")
                print(f'*{base}^({num[sinal_expoente]}{int(num[sinal_expoente+1:]) + 1})')
            else:
                # print('negative') #APAGAR
                print(f'{string.ascii_lowercase[cont1]}. 0.{num[0]}', end="")
                for x in range(2, sinal_expoente - 1):
                    print(num[x], end="")
                print(f'*{base}^({num[sinal_expoente]}{int(num[sinal_expoente + 1:]) - 1})')
        cont1 += 1


#ERRO ABSOLUTO - QUESTAO-07-PT1
def erro_absoluto(*valores):
    cont1 = 0
    cont2 = 0
    while cont1 < len(valores):
        # ERRO ABSOLUTO
        ea = abs(valores[cont1] - valores[cont1 + 1])  # O METODO abs() RETORNA UMA STRING
        ea_f = np.format_float_scientific(ea, precision=4, unique=False)  # BIBLIOTECA NUMPY P MANIPULAR STRING E COLOCAR EM NOTACAO DE PONTO FLUTUANTE, RETORNANDO OUTRA STRING

        # SAIDA
        print(f'{string.ascii_lowercase[cont2]}. {ea_f[0:ea_f.find("e")]}*10^{ea_f[ea_f.find("e") + 1:]}')

        # CONTADORES
        cont1 += 2
        cont2 += 1


#ERRO RELATIVO - QUESTAO-07-PT2
def erro_relativo(*valores):
    cont1 = 0  # CONTADOR P/ WHILE
    cont2 = 0  # CONTADOR P/ STRING.ASCII
    while cont1 < len(valores):
        # ERRO ABSOLUTO
        ea = abs(valores[cont1] - valores[cont1 + 1])  # O METODO abs() RETORNA UMA STRING
        ea_f = np.format_float_scientific(ea, precision=4, unique=False)  # BIBLIOTECA NUMPY P MANIPULAR STRING E COLOCAR EM NOTACAO DE PONTO FLUTUANTE, RETORNANDO OUTRA STRING

        # ERRO RELATIVO
        a = float(ea_f)  # TRANSFORMANDO A STRING EM VALOR DE PONTO FLUTUANTE
        b = float(valores[cont1 + 1])  # TRANSFORMANDO A STRING EM VALOR DE PONTO FLUTUANTE
        c = np.format_float_scientific((a / b), precision=4, unique=False)  # BIBLIOTECA NUMPY P CALCULA NOVO FLOAT E RETORNA STRING COM PRECISAO DEFINIDA

        # SAIDA
        print(f'{string.ascii_lowercase[cont2]}. {c[0:c.find("e")]}*10^{c[c.find("e") + 1:]}')

        # CONTADORES
        cont1 += 2
        cont2 += 1


#ENUNCIADOS:
q01 = """1. Converta os seguintes números decimais para binário
a. 39
b. 1500
c. 65,023"""

q02 = """Converta os seguintes números binários para decimal:
a. (0.1101)2
b. (101111101)2
c. (11011.01)2"""

q03 = """Escreva os números abaixo na notação ponto flutuante (normalização).
a. 0.000000123
b. 25
c. 52342034342
d. 12000
e. 132²"""

q04 = """Quais as principais fontes de erros devido a operações em máquinas digitais? Dê exemplos."""

q05 = """Como esse números acima seriam representados numa máquina digital se tivesse
apenas 4 dígitos na mantissa? Dê a resposta ainda utilizando a notação ponto flutuante e
empregando o arredondamento (se preciso).
a. 0.000000123
b. 25
c. 52342034342
d. 12000
e. 132²"""

q06 = """Qual(is) do(s) números acima não seria(m) possível(is) de ser(em)
representado(s) numa maquina digital cujo os valores máximos e mínimos dos
expoentes da representação do ponto flutuante fosse 2 e -2?
a. 0.000000123
b. 25
c. 52342034342
d. 12000
e. 132²"""

q07 = """Calcule o erro relativo e o erro absoluto envolvidos nos seguintes
cálculos numéricos abaixo onde o valor preciso da solução é dado por x e o
valor aproximado é dado por x' (aproximado).
a. x = 0.0020 e x' = 0.0021
b. x = 530000 e x' = 529400
c. x = 2x10^12 e x' = 1.872x10^12"""

q08 = """Dê dois exemplos de problema da sua área de estudo que pode ser
solucionado por métodos numéricos."""

#QUESTA0-01:
cabecalho("01", q01)
dec2bin(39, 1500, 65.023)
cabecalho_resolucao()

#QUESTA0-02:
cabecalho("02", q02)
bin2dec(0.1101, 101111101, 11011.01)
cabecalho_resolucao()

#QUESTAO-03:
cabecalho("03", q03)
normalizacao_float(0.000000123, 25, 52342034342, 1200, 132*132, base=10)
cabecalho_resolucao()

#QUESTAO-04:
cabecalho("04", q04)
print(f"""Princais tipos de erros:

1. Incerteza dos Dados: são devidos aos erros nos dados de entrada.
Quando o modelo matemático é oriundo de um problema físico, existe incerteza
nas medidas feitas pelos instrumentos de medição, que possuem acurácia finita

2. Erros de Arredondamento: são aqueles relacionados com as limitações
existentes na forma de representar números em máquina.

ex: A saida da soma (0.1 + 0.2) em python é dada por: ({0.1+0.2})
e não (0.3) como esperado.
O erro de arredondamento ocorre pela maneira como o número de ponto flutuante
é armazenado e manipulado na própria CPU, sendo o sistema binário o responsavel
pelas operações de maquina, por isso existem imprecisões na representação do sistema decimal.

3. Erros de Truncamento: surgem quando aproximamos um conceito matemático formado por
uma sequência infinita de passos por de um procedimento finito. Por exemplo, a definição
de integral é dada por um processo de limite de somas. Numericamente, aproximamos por uma
soma finita. O erro de truncamento deve ser estudado analiticamente para cada método empregado
e normalmente envolve matemática mais avançada que a estudada em um curso de graduação.
""", end="")
cabecalho_resolucao()

#QUESTAO-05:
cabecalho("05", q05)
normalizacao_float_4dig(0.000000123, 25, 52342034342, 1200, 132 * 132, base=10)
cabecalho_resolucao()

#QUESTAO-06:
cabecalho("06", q06)
exp_max_e_min(0.000000123, 25, 52342034342, 1200, 132*132, base=10)
cabecalho_resolucao()

#QUESTAO-07:
cabecalho("07", q07)
print('Exibindo erros calculados com uma precissão de 4 digitos:\n')
print('Erro Absoluto:')
erro_absoluto(0.0020, 0.0021, 529400, 530000, 2*10**12, 1.872*10**12)
print('\nErro Relativo:')
erro_relativo(0.0020, 0.0021, 530000, 529400, 2*10**12, 1.872*10**12)
cabecalho_resolucao()

#QUESTAO-08:
cabecalho("08", q08)
print("""Método dos elementos finitos (FEM):

É um método numérico utilizado para solucionar problemas de física, matemática
e engenharia. Dentre suas principais aplicações estão a analise estrutural: determinação
de deslocamentos, deformações e tensões; analises de materiais: resistência, rigidez e
fadiga. Além disso, analises térmicas, acústicas, dinâmicas, eletromagnéticas e de mecânica
dos fluidos. O método é adequado para tratar de problemas com geometrias e carregamentos complexos.

Método dos volumes finitos (FVM):

O método dos volumes finitos (FVM – Finite Volume Method) é um método desenvolvido na década de 70 
muito utilizado em problemas de mecânica dos fluidos. É bastante eficaz na solução de problemas de
fluxos multifásicos, reativos e turbulentos. o método dos volumes finitos, assim como no método 
dos elementos finitos, há a discretização do domínio em pequenos volumes, denominados volumes de controle,
os volumes são conectados por nós formando uma malha. As variáveis do problema são calculadas nos nós e
armazenadas no interior do elemento. O método dos volumes finitos é baseado na ideia da observação de Euler
e nos princípios de conservação de massa, de quantidade de movimento e de energia.""")
cabecalho_resolucao()
