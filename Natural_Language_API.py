import json
import PyPDF2
import os, errno
#import time

#from pprint import pprint
from watson_developer_cloud import NaturalLanguageUnderstandingV1 as NLU 
import Modulo_Read_File, Modulo_N_L_U_Information as NLUM, Limita_tamanho_em_binario as Limitador


numero_binario_tranformado = Limitador.transforma_hora_em_binario()

numero_tranformado = Limitador.tranforma(numero_binario_tranformado)
print(numero_tranformado)
#extraindo dados do arquivo json
data_return = Modulo_Read_File._ler_json_file('credentials.json')
#print(json.dumps(data_return, indent=2))

#retorna credencial de autenticação
url, version, apikey, model_id = Modulo_Read_File._return_nlu_credentials_(data_return)


natural_language = NLU(version=version,iam_apikey=apikey,url=url)


# extrair de pdf para txt
pdf_file = 'Decisao_Judicial_Med.pdf'
return_pdf_file = Modulo_Read_File._ler_pdf_file(pdf_file)


# retornar (relacionamento, entidades e por cima mapear o sentimento[Transitado em Julgado])
return_natural_language_understanding = NLUM.extract_natural_language_understanding_information_form_url_or_document(
    NLU=natural_language,document= return_pdf_file, model=model_id, target1='Transitado em julgado', target2='negar provimento')
#print(type(return_natural_language_understanding))



file_name = 'result/body_request{}.json'.format(numero_tranformado)
if not os.path.exists(os.path.dirname(file_name)):
    try:
        os.makedirs(os.path.dirname(file_name))
        print("Pasta e arquivo criado")
    except OSError as exc: 
        if exc.errno != errno.EEXIST:
            raise

# file_name = '/result/body_request.json'
# os.makedirs(os.path.dirname(file_name), exist_ok=True)
with open(file_name,'w',encoding='utf-8') as file:
    ler = json.dumps(return_natural_language_understanding,ensure_ascii=False,indent=1)
    file.write(ler)
