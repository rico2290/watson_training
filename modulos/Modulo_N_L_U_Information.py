from watson_developer_cloud.natural_language_understanding_v1  \
    import Features, RelationsOptions,EntitiesOptions,MetadataOptions, \
        RelationEntity, SentimentOptions
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