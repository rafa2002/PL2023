#Este ficheiro contém uma possível solução para o TPC2 de PL2223

from sys import stdin

total = 0
flag_off = True

def terminal():
    print("Olá imprima ON para somar\nOFF para desligar a soma\n= para somar :D ")
    for lido in stdin:
        lido = lido.upper()
        parse_linha(lido)


def parse_linha(dados):
    global total
    global flag_off
    segmento = str()
    i = 0
    while i<len(dados):
        if dados[i] == '=':
            total = 0
            lista = segmento.split()
            for seg in lista:
                if seg.isdigit():
                    total += int(seg)
                print(seg)
            lista.clear()
            i+=1
            print(f"total somado até ao momento: {total}")
        else:
            if flag_off == False and dados[i].isdigit():
                segmento += str(dados[i])
                for j in range(i+1,len(dados)):
                    if dados[j].isdigit():
                        segmento += str(dados[j])
                    else:
                        segmento += " "
                        i = j-1
                        break
            if dados[i:i+2]=="ON":
                flag_off = False
                i += 2
            if dados[i:i+3]=="OFF":
                flag_off = True
                i+=3
            else:
                i+=1


terminal()
