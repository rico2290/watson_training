from watson_developer_cloud import DiscoveryV1 as Discovery
from watson_developer_cloud import WatsonApiException
from watson_developer_cloud import WatsonService
from http import HTTPStatus
import modulos.Modulo_Read_File as Modulo_Read_File
import modulos.Modulo_Watson_Services as Modulo_Watson_Services
#from watson_developer_cloud import AuthorizationV1
import os.path
import json


data_return = Modulo_Read_File._ler_json_file('credentials_discovery.json')

url, version, apikey,environment_id,configuration_id, collection_id = Modulo_Read_File._return_discovery_credentials_(data_return)
# print(configuration_id)
discovery = Discovery(version=version,iam_apikey=apikey,url=url)
new_name = 'PMENOS_COLLECTION-2019'
description = 'Teste de Update'
#create_environment = Modulo_Watson_Services.create_discovery_environment_(discovery,envinorment_name=name,description=description)

#print(create_environment)
#abcsd = discovery.get_document_status(environment_id,collection_id,)

#print(json.dumps(discovery.list_environments().get_result(),indent=2))

#result_environment = Modulo_Watson_Services.update_discovery_collection_(discovery,environment_id,new_name,description)

#print(json.dumps(result_environment,indent=2) )

new_description_name = "Coleção PagueMenos"
new_Collection_name = "Pague_Menos_Collection-2019"
updated = Modulo_Watson_Services.update_discovery_collection_(discovery,environment_id,collection_id,configuration_id,new_Collection_name,description=new_description_name)
print(json.dumps(updated,indent=2) )
#  --------- Create a new Colletion -------------------------
# new_description_name = "Coleção de PagueMenos"
# new_Collect_name = "Pague_Menos_Collection-2019"
# discovery.create_collection(
#     environment_id=environment_id,
#     name=new_Collect_name,
#     configuration_id=configuration_id, 
#     description=new_description_name,
#     language='pt-br'
#     )

#print(json.dumps(discovery.list_collections().get_result(),indent=2) )

'''
#config = discovery.list_collections(envpemnos["environments"][0]).get_result()
#print(json.dumps(config, indent=2))
print("Data Before Updated => "+ json.dumps(envpemnos, indent=2))
#print(json.dumps(discovery.user_agent_header)) -- show version of api sdk and windows version
#print(discovery.url)




print("\n\n---------------------Printing After Updated -----------------")
time.sleep(3)
envpemnosAfter = discovery.update_environment(
    environment_id=envID, name="envpmenos", 
    description="environment updated"
    )

# ------------------- Print Environment after updated ------------------------------
#print("Data After Updated "+ json.dumps(envpemnosAfter, indent=2))





# --------------- Delete existing Collection -------------------------
env_del_id = "c42a101a-6034-4d6d-b90a-5f3a2e608b5e"
collect_del_id ="45f20508-c2d7-4e1c-8806-a96bce22761d"
discovery.delete_collection(env_del_id,collect_del_id)

# ---------- Update existing Collection -----------------------
new_collecttion = "Novo nome para coleção"
descricao = "Coleção atualizada hoje"
discovery.update_collection(envID,collectID,new_collecttion, configID )


 # --------------------- Upload Docs from existing Collection (e.g: Pague_Menos_Collection) ---------------
env_id = "c42a101a-6034-4d6d-b90a-5f3a2e608b5e"
collect_id ="be1d4783-0de3-4cd7-a329-9381cdf1716c"
pdf_file = "pythonAPI.pdf"
with open(pdf_file, "rb") as arq:
     add_Docs = discovery.add_document(env_id,
     collect_id,
     file=arq, 
     filename="Python_Api",
     )

# -------------------- List Collections -------------------------
envpemnos = discovery.list_environments().get_result()
print("Data Before Updated => "+ json.dumps(envpemnos, indent=2))


'''









