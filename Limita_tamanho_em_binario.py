import time

def tranforma(numero_binario):
    #print(numero_binario)
    b = ' '
    #Caso o  tamanho do numero binario for menor que 5
    if len(numero_binario) <= 8:
            b = 8-len(numero_binario)
            b ='{:0>8}'.format(numero_binario)
            #print(b, 'menor')
    #Caso o tamanho do numero binario for maior que 5
    if len(numero_binario) > 8:
            b = len(numero_binario) - 8
            b = numero_binario[b:]
            #print(b, 'maior')
    return b


def transforma_hora_em_binario():
    h = time.perf_counter_ns()
    binario = ("{0:b}".format(int(round(h,2))))
    return binario