import json
import PyPDF2


def _ler_json_file(ler_json):
    data = []
    with open(ler_json) as file:
        data = json.load(file)
        return data
        #print(data)

def _ler_pdf_file(ler_pdf):
    pdf_file = ler_pdf
    ler_pdf = PyPDF2.PdfFileReader(pdf_file)
    conteudo = ''
    for x in range(ler_pdf.getNumPages()):
            pagina = ler_pdf.getPage(x)
            #print("Página Numero: {}".format(str(1+ler_pdf.getPageNumber(pagina))))
            conteudo = pagina.extractText()
    return conteudo


#retorna credencial de autenticação
def _return_nlu_credentials_(data_return):
    return data_return['credentials']['url'],\
        data_return['credentials']['version'],\
            data_return['credentials']['apikey'],\
                data_return['credentials']['model_id']

def _return_discovery_credentials_(data_return):
    return data_return['credentials']['url'],\
        data_return['credentials']['version'],\
            data_return['credentials']['apikey'],\
                data_return['credentials']['environment_id'],\
                        data_return['credentials']['configuration_id'],\
                                data_return['credentials']['collecttion_id']