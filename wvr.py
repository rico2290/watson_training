from watson_developer_cloud import VisualRecognitionV3 as vr 
import json

#Reconhecimento de Imagem iam_apikey = apikey
wvr = vr( version="2018-01-29",iam_apikey="F_-o_C5ie1HKGU750akv3SsbDwy5dI2yigLVl0TSZVOi",)
img = wvr.classify(url="https://s2.glbimg.com/3auOxS3cG2mc_H5jFXDpxC7ol-w=/e.glbimg.com/og/ed/f/original/2016/09/12/dr-alan-turing-2956483.jpg")
print(img)

print((wvr))