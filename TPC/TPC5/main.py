import re
MOEDAS = {'1c':0,'2c':0,'5c':0,'10c':0,'20c':0,'50c':0,'1e':0,'2e':0}
valido = True

def saldo():
    global MOEDAS
    c = MOEDAS['1c'] + 2 * MOEDAS['2c'] + 5 * MOEDAS['5c'] + 10 * MOEDAS['10c'] + 20 * MOEDAS['20c'] + 50 * MOEDAS['50c']
    e = MOEDAS['1e'] + 2 * MOEDAS['2e']
    if c>=100:
        c,e = c%100,e+c//100
    return str(e)+'e'+str(c)+'c'

def suficiente(saldo_min,saldo_cliente):
    grupos_saldo_min = re.match(r'(\d+)e(\d+)c',saldo_min)
    grupos_saldo_cliente = re.match(r'(\d+)e(\d+)c', saldo_cliente)
    centimos_saldo_min = int(grupos_saldo_min.group(1))*100 + int(grupos_saldo_min.group(2))
    centimos_saldo_cliente = int(grupos_saldo_cliente.group(1)) * 100 + int(grupos_saldo_min.group(2))

    valido = centimos_saldo_cliente - centimos_saldo_min >= 0

    return valido

def extrai_saldo(valor):
    global MOEDAS
    custo = re.match(r'(\d+)e(\d+)c',valor)
    custo_centimos = int(custo.group(1))*100 + int(custo.group(2))
    while MOEDAS['2e']>0 and custo_centimos>=200:
        custo_centimos -= 200
        MOEDAS['2e']-=1

    while MOEDAS['1e']>0 and custo_centimos>=100:
        custo_centimos -= 100
        MOEDAS['1e'] -= 1

    while MOEDAS['50c']>0 and custo_centimos>=50:
        custo_centimos -= 50
        MOEDAS['50c'] -= 1

    while MOEDAS['20c']>0 and custo_centimos>=20:
        custo_centimos -= 20
        MOEDAS['20c'] -= 1

    while MOEDAS['10c']>0 and custo_centimos>=10:
        custo_centimos -= 10
        MOEDAS['10c'] -= 1

    while MOEDAS['5c']>0 and custo_centimos>=5:
        custo_centimos -= 5
        MOEDAS['5c'] -= 1

    while MOEDAS['2c']>0 and custo_centimos>=2:
        custo_centimos -= 2
        MOEDAS['2c'] -= 1

    while MOEDAS['1c']>0 and custo_centimos>=1:
        custo_centimos -= 1
        MOEDAS['1c'] -= 1

def terminal():
    global valido
    global MOEDAS
    entrada = input()
    while entrada == "LEVANTAR":
        moedas = input("maq: Introduza moedas.\n")
        moedas = moedas.strip()
        moedas = moedas.split()

        str_saida = "maq: "
        m_invalid = 1
        for moeda in moedas:
            if moeda in MOEDAS.keys() :
                MOEDAS[moeda] += 1
            else:
                if(m_invalid):
                    str_saida += f" moeda invalida -"
                    m_invalid=0
                str_saida += f" {moeda}"
        str_saida += "; saldo =" + saldo() + "\n"
        print(str_saida)
        while valido:
            contacto = input("maq: Queira introduzir um contacto ou pousar a maquina\n")
            if re.match(r'601|641\d{6}',contacto):
                valido = False
            elif re.match(r'00\d+',contacto):
                if suficiente("1e50c",saldo()):
                    extrai_saldo("1e50c")
                    print("maq: Chamada realizada com sucesso\n")
                else:
                    print("maq: Saldo inválido\n")
            elif re.match(r'2\d{8}',contacto):
                if suficiente("0e20c",saldo()):
                    extrai_saldo("0e20c")
                    print("maq: Chamada realizada com sucesso\n")
                else:
                    print("maq: Saldo inválido\n")
            elif re.match(r'800\d{6}',contacto):
                print("maq: Chamada realizada com sucesso\n")
            elif re.match(r'808\d{6}',contacto):
                if suficiente("0e10c",saldo()):
                    extrai_saldo("0e10c")
                    print("maq: Chamada realizada com sucesso\n")
                else:
                    print("maq: Saldo inválido\n")
            elif re.match(r'POUSAR',contacto):
                valido = False
                entrada = "POUSAR"
            else:
                print("maq: Operação inválida queira voltar a outra operação\n")
    print(f"maq: Decidiu dar a operação por concluída. OBRIGADO.\nEste é o valor do seu saldo final  - {saldo()}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    terminal()
