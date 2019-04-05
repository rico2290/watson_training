print(json.dumps(discovery.list_environments().get_result(),indent=2))

# time.sleep(3)
# envpemnosAfter = discovery.update_environment(
#     environment_id=environment_id, name=name, 
#     description=description
#     )