from gensim.summarization import keywords
import json
json_data = open("training1.json")
AIMX_array = []
MISC_array = []
OWNX_array = []
CONT_array = []
data = json.load(json_data)
for value in data:
    root = value['label']
    if(root=="AIMX"):
        text=value['text']
        AIMX_array.append(text)
    if(root=="MISC"):
        text=value['text']
        MISC_array.append(text)
    if(root=="OWNX"):
        text=value['text']
        OWNX_array.append(text)
    if(root=="CONT"):
        text=value['text']
        CONT_array.append(text)	
		
AIMX=  '.'.join(AIMX_array)
MISC=  '.'.join(MISC_array)
OWNX=  '.'.join(OWNX_array)
CONT=  '.'.join(CONT_array)
print "AIMX Keyword:-"
print keywords(AIMX)
print "MISC Keyword:-"
print keywords(MISC)
print "OWNX Keyword:-"
print keywords(OWNX)
print "CONT Keyword:-"
print keywords(CONT)

