
#Este ficheiro contém uma possível solução para o TPC1 de PL 22/23 Aluno: A97642


import math
#O Cabeçalho do DataSet é assim:
#   idade,sexo,tensão,colesterol,batimento,temDoença
dados = []
total = 0
pessoas = {"M": 0, "F": 0}
sexo_doentes = {"M": 0, "F": 0} # contém o numero de doentes/infetados de cada sexo
faixas_etarias = dict() # tuplos com (numero de pessoas, numero de pessoas infetadas) para cada faixa etaria
niveis_colesterol = dict() # tuplos com (numero de pessoas, numero de pessoas infetadas) para cada nivel de colesterol
id_min = 0
id_max = 0
col_min = 10000
col_max = -10000


def parseFile():
    global total,id_min,id_max,col_min,col_max
    # Guardamos a informação do ficheiro em memória
    with open("myheart.csv", "r") as f:
        for line in f.readlines()[1:]:
            total += 1
            # [:-1] para ignorar o \n
            dados_pessoa = line[:-1].split(',')
            dados.append(dados_pessoa)
    for pessoa in dados:
        id_min = 30
        if id_max < int(pessoa[0]):
            id_max = int(pessoa[0])
        if col_min > int(pessoa[3]):
            col_min = int(pessoa[3])
        if col_max < int(pessoa[3]):
            col_max = int(pessoa[3])



def distPorGenero():
    for pessoa in dados:
        if pessoa[1] == 'F':
            pessoas['F'] += 1
            if int(pessoa[5]):
                sexo_doentes['F'] += 1
        else:
            pessoas['M'] += 1
            if int(pessoa[5]):
                sexo_doentes['M'] += 1

def distPorId():
    for i in range(id_min,id_max,5):
        faixas_etarias[(i,i+4)] = (0,0)

    for pessoa in dados:
        if int(pessoa[0])>=id_min:
            faixa = lookUpFaixaEtaria(int(pessoa[0]))
            if int(pessoa[5]):
                novo = faixas_etarias[faixa][0] + 1,faixas_etarias[faixa][1] + 1
                faixas_etarias[faixa] = novo
            else:
                novo = faixas_etarias[faixa][0] + 1, faixas_etarias[faixa][1]
                faixas_etarias[faixa] = novo


def lookUpFaixaEtaria(idade):
    for dist in range(0,5):
        if abs(idade-dist)%5==0:
            return idade-dist,idade-dist+4

def distPorColesterol():
    for valor in range(col_min,col_max+1,10):
        if valor in range(lookUpFaixaColesterol(col_max)[0],lookUpFaixaColesterol(col_max)[1]):
            niveis_colesterol[lookUpFaixaColesterol(col_max)] = (0,0)
            break
        else:
            niveis_colesterol[(valor, valor + 9)] = (0,0)

    for pessoa in dados:
        if int(pessoa[3])>=col_min:
            faixa = lookUpFaixaColesterol(int(pessoa[3]))
            if int(pessoa[5]):
                novo = niveis_colesterol[faixa][0]+1,niveis_colesterol[faixa][1]+1
                niveis_colesterol[faixa] = novo
            else:
                novo = niveis_colesterol[faixa][0] + 1, niveis_colesterol[faixa][1]
                niveis_colesterol[faixa] = novo

def lookUpFaixaColesterol(idade):
    for dist in range(0,10):
        if abs(idade-dist)%10==0:
            return idade-dist,idade-dist+9

def tabelaGenero():
    print(f"Sexo :: #Pessoas :: #Doentes")
    print(f"M    ::   {pessoas['M']}    ::   {sexo_doentes['M']}")
    print(f"F    ::   {pessoas['F']}    ::   {sexo_doentes['F']}")

def tabelaIdade():
    print("Faixa étaria :: #Pessoas :: #Doentes")
    for faixa in faixas_etarias.keys():
        print(f"[{faixa[0]}, {faixa[1]}]     ::   {faixas_etarias[faixa][0]}    ::    {faixas_etarias[faixa][1]}")

def tabelaColesterol():
    print("Níveis de Colesterol :: #Pessoas :: #Doentes")
    for nivel in niveis_colesterol.keys():
        print(f"[{nivel[0]}, {nivel[1]}]            ::   {niveis_colesterol[nivel][0]}       ::   {niveis_colesterol[nivel][1]}")

def terminal():
    parseFile()
    valor = 0
    while(valor==0 and valor!=4):
        print("\nQue distribuição pretende ver?")
        print("1 - Valores relativos ao sexo")
        print("2 - Valores relativos à idade")
        print("3 - Valores relativos ao nível de Colesterol")
        print("4 - Para sair")

        valor = int(input())
        while(valor == 1):
                    distPorGenero()
                    tabelaGenero()
                    print("\n")
                    print("0 - Para voltar atrás")
                    valor = int(input())

        while(valor == 2):
                    distPorId()
                    tabelaIdade()
                    print("\n")
                    print("0 - Para voltar atrás")
                    valor = int(input())

        while(valor == 3):
                    distPorColesterol()
                    tabelaColesterol()
                    print("\n")
                    print("0 - Para voltar atrás")
                    valor = int(input())



terminal()