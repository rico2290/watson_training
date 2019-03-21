import re


texto = ' Vistos, relatados e discutidos estes autos de Apelação / Remessa Necessária nº 1009666-43.2015.8.26.0079, da Comarca de Botucatu, em que é apelante/apelado PEDRO ADILSON MULOTTO (JUSTIÇA GRATUITA), é apelado/apelante PREFEITURA MUNICIPAL DE BOTUCATU.'

obj = re.match(r'(.*) [Rr]emessa [Nn]ecessária (.*) ((.\s|[,\t\r])*)', texto, re.M|re.I)
proc = re.sub(r'\D', "", texto)
print ('=> Numero Processo: ',proc)
fatia = re.findall(r'\d{5}', proc)
print ('=> Numero fatiado: {}'.format(fatia))
#print(type(fatia))


if obj:
    print('=> TEXTO COMPLETO: ', obj.group(),'\n')
    print('=> Primeira parte: ', obj.group(1),'\n')
    print('=> Segunda parte: ', obj.group(2))
else:
    print('Não Encontrado!!!')

'''
Algumas sntaxes para compreensão da expressão regular em python 
(.*) -> zero ou mais ocorrencias precedido da expressão
(.*?) -> zero ou uma ocorencia precedido da expressão
'''