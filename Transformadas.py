import Modulo_Tranformacao as MT

l = []
l = MT._trandformacao_do_arquivo('c:/Users/102869/Desktop/watson_training/stopwords/stopwords.txt')
print('\n-----------------------------Imprimindo em Lista ---------------------\n',l)

de_lista_para_string = MT._transformar_lista_em_string_(l)
print('\n--------------------Imprimindo em String----------------------------\n',de_lista_para_string)

transformado = 'c:/Users/102869/Desktop/watson_training/stopwords/Lista_para_String.txt'
with open(transformado, 'w', encoding='utf-8') as file:
    file.write(de_lista_para_string)

