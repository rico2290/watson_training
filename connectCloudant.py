
import time

#from cloudant import Cloudant, CouchDB
from cloudant.client import Cloudant 
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

username = "951350c0-a21a-46f2-b176-a8b2dcce25ce-bluemix"
api_key = "gayiZh0FagOrvhrxpzCGqBWDYVEnnzqRJkRKpCZJHKKl"
#url = "https://951350c0-a21a-46f2-b176-a8b2dcce25ce-bluemix.cloudantnosqldb.appdomain.cloud"
connectCloudant = Cloudant.iam(username,api_key)

connectCloudant.connect()
try:
   
    print("Entrando no try")
    pemnosCloudant = connectCloudant.create_database("cloudpmenos")
    #res_collect = connectCloudant.all_dbs()
    #print("Documentos: {0}".format(res_collect))
    if pemnosCloudant.exists():
            print("banco criado com sucesso !!!")
    else:
        print("Falha ao criar o banco ")
except CloudantException as exc:
    print("Error " + str(exc))

#database = client["stock-data"]
#client.delete_database(database)



    