import re, math, json
n = 1
freq_processos_no_ano = {}
dist_nomes_no_seculo = {}
dist_apelido_no_seculo = {}
nomes = {}
apelidos = {}
lista_ordenada_nomes = []
lista_ordenada_apelidos = []
json_file = {}
tios = 0
irmãos = 0
sobrinhos = 0



def seculo(ano):
    return math.ceil(ano / 100)

def alinea_a(data):
    data = re.split(r'-',data)
    ano = int(data[0])
    if ano not in freq_processos_no_ano.keys():
        freq_processos_no_ano[ano] = 1
    else:
        freq_processos_no_ano[ano] += 1


def alinea_b(data,nome_completo):
    global dist_nomes_no_seculo,dist_apelido_no_seculo,nomes,apelidos,lista_ordenada_nomes,lista_ordenada_apelidos
    data = re.split(r'-', data)
    sec = seculo(int(data[0]))
    nome_completo = re.split(r' ', nome_completo)
    ultimo_index = len(nome_completo)-1
    nome = nome_completo[0]
    sobrenome = nome_completo[ultimo_index]

    #Para dar o 5 nomes e apelidos mais usados

    #Para ordenar pelos seculos os mais usados
    if sec not in dist_nomes_no_seculo.keys():
        dist_nomes_no_seculo[sec] = {}
    if nome not in dist_nomes_no_seculo[sec]:
        dist_nomes_no_seculo[sec] = {}
        (dist_nomes_no_seculo[sec])[nome] = 1
    else:
        dist_nomes_no_seculo[sec][nome] += 1

    if sec not in dist_apelido_no_seculo.keys():
        dist_apelido_no_seculo[sec] = {}
    if sobrenome not in dist_apelido_no_seculo[sec]:
        dist_apelido_no_seculo[sec] = {}
        (dist_apelido_no_seculo[sec])[sobrenome] = 1
    else:
        dist_apelido_no_seculo[sec][sobrenome] += 1

    if nome not in nomes.keys():
        nomes[nome] = 1
    else:
        nomes[nome] += 1

    if sobrenome not in apelidos.keys():
        apelidos[sobrenome] = 1
    else:
        apelidos[sobrenome] += 1

def alinea_c(segmento):
    global tios, irmãos, sobrinhos
    exp_tio = r'(?i:tio)|(?i:tia)'
    exp_irmao = r'(?i:irmao)|(?i:irma)'
    exp_sobrinho = r'(?i:sobrinho)|(?i:sobrinha)'
    if re.search(exp_tio,segmento):
        tios += 1
    if re.search(exp_irmao,segmento):
        irmãos += 1
    if re.search(exp_sobrinho,segmento):
        sobrinhos += 1

def alinea_d(linha,arquivo_json):
    json_file[linha[0]] = {'data': linha[1], 'nome': linha[2], 'pai': linha[3], 'mae': linha[4], 'observacoes': linha[5]}
    json_string = json.dumps(json_file, indent=4)
    arquivo_json.write(json_string)


with open("processos.txt",'r') as f:
    with open("output.json", 'w') as arquivo_json:
        for linha in f.readlines():
            linha = re.split(r'::',linha)
            if len(linha) == 7:
                alinea_a(linha[1])
                alinea_b(linha[1],linha[2])
                if linha[5] != '':
                    alinea_c(linha[5])
                #Escreve as primeiras 20 linhas num ficheiro json
                if n<=20:
                    alinea_d(linha,arquivo_json)
                    n += 1
        irmãos /= 2
    arquivo_json.close()
f.close()

lista_ordenada_nomes = sorted(nomes,key = lambda nome: nomes[nome],reverse = True)
lista_ordenada_apelidos = sorted(apelidos,key = lambda apelido: apelidos[apelido], reverse=True)

def funcao(i):
    if i == 1:
        for ano in sorted(freq_processos_no_ano.keys(),key = None):
            print(f"No ano {ano}: {freq_processos_no_ano[ano]} processos")
    if i == 2:
        for sec in dist_nomes_no_seculo.keys():
            print(f"No seculo {sec}")
            for nome in dist_nomes_no_seculo[sec]:
                    print(f"O nome {nome} aparece {dist_nomes_no_seculo[sec][nome]} vezes")
            for apelido in dist_apelido_no_seculo[sec]:
                print(f"O apelido {apelido} aparece {dist_apelido_no_seculo[sec][apelido]} vezes")

        print("\n\n")
        print("Nomes mais usados:")
        print(lista_ordenada_nomes[0:5])

        print("Apelidos mais usados:")
        print(lista_ordenada_apelidos[0:5])

    if i == 3:
        print(f"Irmaos: {int(irmãos)}")
        print(f"Tios: {tios}")
        print(f"Sobrinhos: {sobrinhos}")


#Para testar basta mudar o parametro da ultima linha:
# 1 - para a alinea a)
# 2 - para a aliena b)
# 3 - para a alinea c)
funcao(3)

