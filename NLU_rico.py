import json
import PyPDF2, re
from pprint import pprint
from watson_developer_cloud import NaturalLanguageUnderstandingV1 as NLU 
from watson_developer_cloud.natural_language_understanding_v1  \
    import Features, RelationsOptions,EntitiesOptions,MetadataOptions,RelationEntity, SentimentOptions

#Explorar arquivo json
def _ler_json_file(ler_json):
    data = []
    with open(ler_json, 'r') as file:
        data = json.load(file)
        return data
        print(data)


data_return = _ler_json_file('credentials-rico.json')

#Extrair dados do arquivo json
def _return_nlu_credentials_(data_return):
    print(json.dumps(data_return, indent=2))
    return data_return['credentials']['url'],\
        data_return['credentials']['version'],\
            data_return['credentials']['apikey'],\
                data_return['credentials']['model_id']



url, version, apikey, model_id = _return_nlu_credentials_(data_return)

print("Imprimindo a extração URL :{}".format(url))

'''
#Concatenar jsonString
a = json.loads(url)
b = json.loads(version)
c = json.loads(apikey)
d = json.loads(model_id)

ab = dict(a.items() + b.items())
cd = dict(c.items() + d.items())
jsonMerged = dict.items()
print(json.dumps(a, indent=2))
'''
natural_language = NLU(version=version,iam_apikey=apikey,url=url)

'''

def _ler_pdf_file(ler_pdf):
    pdf_file = ler_pdf
    ler_pdf = PyPDF2.PdfFileReader(pdf_file)
    conteudo = ''
    for x in range(ler_pdf.getNumPages()):
            pagina = ler_pdf.getPage(x)
            #print("Página Numero: {}".format(str(1+ler_pdf.getPageNumber(pagina))))
            conteudo = pagina.extractText()
    return conteudo

# Chamando a função para extrair de pdf para txt
pdf_file = _ler_pdf_file('Decisao_Judicial_Med.pdf')
  


def _return_natural_language_information_from_document_or_url_(NLU ,document=None, url=None, model=None):
    result = NLU.analyze(
        text=document,
        features=Features(
            relations=RelationsOptions(model=model_id),\
            sentiment=SentimentOptions(targets=['Transitado em julgado', 'negar provimento']),
            entities=EntitiesOptions(model=model_id))
        ).get_result()
    return result

#Chamando a função para retornar (relacionamento, entidades e por cima mapear o sentimento[Transitado em Julgado])
natural_language_return = _return_natural_language_information_from_document_or_url_(natural_language,pdf_file,model_id)

#print(json.dumps(res, indent=2))

with open('body_request.json','w',encoding='utf-8') as file:
    ler = json.dumps(natural_language_return,ensure_ascii=False,indent=1)
    #ler = json_encode(ler, JSON_UNESCAPED_UNIOCODE)
    file.write(ler)

'''
response = natural_language.delete_model(
    model_id='model_id').get_result()

print(json.dumps(response, indent=2))