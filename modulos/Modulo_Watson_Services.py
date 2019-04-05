from watson_developer_cloud.natural_language_understanding_v1 \
    import Features, RelationsOptions,EntitiesOptions,MetadataOptions, \
        RelationEntity, SentimentOptions
from watson_developer_cloud import WatsonApiException
from watson_developer_cloud import DiscoveryV1 as Discovery
from watson_developer_cloud import WatsonApiException

    
def extract_natural_language_understanding_information_form_url_or_document(NLU ,document=None, url=None, html=None,model=None, target1=None, target2=None):
    try:
        result = NLU.analyze(text=document,url=url, \
            features=Features( relations=RelationsOptions(model=model),\
                sentiment=SentimentOptions(targets=[target1, target2]),\
                    entities=EntitiesOptions(model=model))).get_result()
        return result
    except WatsonApiException as exc:
        print("Method Analyse fail with status code "+ str(exc.code) + ": " + exc.message)


def update_discovery_environment_(Discovery,environment_id,new_name,description=None):
    try:
        result = Discovery.update_environment(environment_id,new_name,description).get_result()
        return result
    except WatsonApiException as exc:
        print("Method Analyse fail with status code "+ str(exc.code) + ": " + exc.message)


def update_discovery_collection_(Discovery,environment_id,collection_id,configuration_id,name,description=None):
    try:
        result = Discovery.update_collection(environment_id,collection_id,configuration_id,name,description).get_result()
        return result
    except WatsonApiException as exc:
        print("Method fail with status code "+ str(exc.code) + ": " + exc.message)
    