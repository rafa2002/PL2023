import re
from functools import reduce
import json

def parse_op(notas,op):
    lista_filtrada = list(filter(lambda elem: elem != '' and elem!='\n',notas))
    notas_int = []
    for nota in lista_filtrada:
        notas_int.append(int(nota))
    if op == "sum":
        resultado = reduce(lambda x,y:x+y,notas_int)
        return resultado
    elif op== "max":
        resultado = reduce(lambda x,y: x if x>y else y,notas_int)
        return resultado
    elif op == "min":
        resultado = reduce(lambda x, y: x if x < y else y, notas_int)
        return resultado
    elif op == "media":
        resultado = reduce(lambda x,y:x+y,notas_int)/len(notas_int)
        return resultado

def parse(segmento):
    tupla = segmento[0]
    op = "Notas"
    existeOp = False
    if len(tupla) == 2:
        if "," in tupla[0]:
            tuple = tupla[0].split(",")
            min = tuple[0]
            max = tuple[1]
        else:
            min = -1
            max = tupla[0]
        if "::" in tupla[1]:
            existeOp = True
            aux = tupla[1].split("::")
            op = aux[1]

    else:
        if "," in tupla[0]:
            tuple = tupla[0].split(",")
            min = tuple[0]
            max = tuple[1]
        else:
            min = -1
            max = tupla[0]

    return int(min),int(max),existeOp,op


def conversor(ficheiro):
    seg = []
    dados = []
    with open(ficheiro,"r",encoding='utf-8') as f:
        cabecalho = f.readline()
        info = f.readlines()

        seg = re.findall(r'Notas\{(\d+(?:,\d+)?)\}(::\w+)?', cabecalho)
        if len(seg) != 0:
            min,max,existeOperacao,op = parse(seg)
            if existeOperacao:
                for linha in info:
                    linha = linha.split(",")
                    notas = linha[3:]
                    resultado = parse_op(notas,op)
                    nova_entrada = {}
                    nova_entrada["Número"] = linha[0]
                    nova_entrada["Nome"] = linha[1]
                    nova_entrada["Curso"] = linha[2]
                    nova_entrada["Notas_"+op] = resultado
                    entrada = json.dumps(nova_entrada)
                    dados.append(entrada+'\n')
            else:
                for linha in info:

                    linha = linha.split(",")
                    notas = linha[3:]
                    notas_finais = []
                    for elem in notas:
                        num = re.findall(r'(\d+)',elem)
                        if num!=[] and num!='\n' and num!=None:
                            notas_finais.append(int(num[0]))
                    nova_entrada = {}
                    nova_entrada["Número"] = linha[0]
                    nova_entrada["Nome"] = linha[1]
                    nova_entrada["Curso"] = linha[2]
                    nova_entrada[op] = notas_finais
                    entrada = json.dumps(nova_entrada)
                    dados.append(entrada+'\n')
        else:
            for linha in info:
                linha = linha.split(",")
                nova_entrada = {}
                nova_entrada["Número"] = linha[0]
                nova_entrada["Nome"] = linha[1]
                nova_entrada["Curso"] = linha[2]
                entrada = json.dumps(nova_entrada)
                dados.append(entrada+'\n')

    with open("out.json","w",encoding='utf-8') as out:
        out.write("[\n"+",".join(dados)+"]")

    return out


conversor("input.csv")

