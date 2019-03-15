import json
import PyPDF2, re
from pprint import pprint
from watson_developer_cloud import NaturalLanguageUnderstandingV1 as NLU 
from watson_developer_cloud.natural_language_understanding_v1  \
    import Features, RelationsOptions,EntitiesOptions,MetadataOptions,RelationEntity, SentimentOptions

data = []
with open('credentials.json', 'r') as file:
    data = json.load(file)
#print(json.dumps(data, indent=2))

url = data['credentials']['url']
version = data['credentials']['version']
apikey = data['credentials']['apikey']
model_id = data['credentials']['model_id']

pdf_file = 'Decisao_Judicial_Med.pdf'
ler_pdf = PyPDF2.PdfFileReader(pdf_file)
for x in range(ler_pdf.getNumPages()):
    pagina = ler_pdf.getPage(x)
    #print("Página Numero: {}".format(str(1+ler_pdf.getPageNumber(pagina))))
    conteudo = pagina.extractText()
    #print((conteudo))
  
#decisao = 'C:\Users\102869\Downloads\STJ_EDC.pdf',

nlu = NLU(version=version,iam_apikey=apikey,url=url)
url_jusBrasil = 'https://tj-sp.jusbrasil.com.br/jurisprudencia/436868694/agravo-de-instrumento-ai-22393797120168260000-sp-2239379-7120168260000/inteiro-teor-436868714?ref=juris-tabs'

res = nlu.analyze(
    url = url_jusBrasil,
    #text=conteudo,
    features=Features(relations=RelationsOptions(model=model_id),
    sentiment=SentimentOptions(targets=['negar provimento']),
    entities=EntitiesOptions(model=model_id))).get_result()
    


print(json.dumps(res, indent=2))


with open('body_request.json','w',encoding='utf-8') as file:
    ler = json.dumps(res,ensure_ascii=False,indent=1)
    #ler = json_encode(ler, JSON_UNESCAPED_UNIOCODE)
    file.write(ler)

