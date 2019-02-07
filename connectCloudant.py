
import time

#from cloudant import Cloudant, CouchDB
from cloudant.client import Cloudant 
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

username = "951350c0-a21a-46f2-b176-a8b2dcce25ce-bluemix"
api_key = "gayiZh0FagOrvhrxpzCGqBWDYVEnnzqRJkRKpCZJHKKl"
url = "https://951350c0-a21a-46f2-b176-a8b2dcce25ce-bluemix.cloudantnosqldb.appdomain.cloud"
connectCloudant = Cloudant(username,url)
db = "pmenosDB"
connectCloudant.connect()
try:
    pemnosCloudant = connectCloudant.create_database(db)
    if pemnosCloudant.exists():
            print("banco criado com sucesso !!!")
except CloudantException as exc:
    print("Falha ao criar o banco {0} ".format(db))

#database = client["stock-data"]
#client.delete_database(database)

'''
try:
    session = client.session()
    
    print("Abrindo sessão...")
    time.sleep(3)
    print("Sessão iniciada com sucesso!!!")

   # print("username: {0}".format(session["userCtx"]["name"]))
    #print("database: {0}".format(client.all_dbs()))
    client.disconnect()
except CloudantException as ex:
    print("Erro --- "  + ":" + ex)


'''


    