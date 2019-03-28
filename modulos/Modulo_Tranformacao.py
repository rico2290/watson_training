import os

def _trandformacao_do_arquivo(arquivo_ou_caminho_completo_do_arquivo):
    lista = [] 
    with open(arquivo_ou_caminho_completo_do_arquivo,encoding='utf-8') as file:
        for line in file:
            lista.append(line)
        ','.join(lista)
    #remover a quebra de linha
    for x,y in enumerate(lista):
      lista[x] = y.strip()
    return lista

def _transformar_lista_em_string_(lista_desejada):
    lista_para_string = ','.join(str(x) for x in lista_desejada)
    return lista_para_string





 
    


