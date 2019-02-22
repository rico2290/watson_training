import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1 as NLU
from watson_developer_cloud.natural_language_understanding_v1 import Features, RelationsOptions #CategoriesOptions, ConceptsOptions,EntitiesOptions, KeywordsOptions, MetadataOptions, , RelationEntity



url = 'https://gateway.watsonplatform.net/natural-language-understanding/api'
version = '2017-11-03'
apikey = 'P4pI0dZSd40kc9HKMsXhjAtDw80_cMy9_DNiAL2FPxIy'

nlu = NLU(version=version,iam_apikey=apikey,url=url)

texto = 'Minha namorada acaba de ser contratada pela empresa Cloud Computing'
res = nlu.analyze(
    text=texto,
    features=Features(relations=RelationsOptions())).get_result()

print(json.dumps(res, indent=2))