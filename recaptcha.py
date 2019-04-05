from python-anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask

key_esaj = '6LeME0QUAAAAAPy7yj7hh7kKDLjuIc6P1Vs96wW3&co=aHR0cDovL2VzYWoudGpjZS5qdXMuYnI6ODA.&hl=pt-BR&v=v1552285980763&size=normal&cb=hy9q64yhxw7m'
site_key = '6LeME0QUAAAAAPy7yj7hh7kKDLjuIc6P1Vs96wW3'  
url = 'http://esaj.tjce.jus.br/esaj/portal.do'

apikey = 'fdccafb6bb99c1831cdb6ec8f4a4d697'

client = AnticaptchaClient(api_key)
task = NoCaptchaTaskProxylessTask(url, site_key)
job = client.createTask(task)
job.join()
print(job.get_solution_response())