
import json
import glob
import sys
import re
path = 'training_set/*.txt'
files=glob.glob(path)
all_json = []
for file in files:
    f=open(file, 'r')
    for line in f:
        if line.startswith("#"):
            pass
        else:
            if "\t" in line:
                sp = line.split("\t")
                cat = sp[0]
                sentence = sp[1].lower()

                fl = re.compile("[^\w']")
                sentence = fl.sub(' ', sentence)
                sentence = re.sub(' +', ' ', sentence)
                json_data = {
                    'text': sentence,
                    'label': cat
                }
                all_json.append(json_data)
            else:
                sp = line.split(" ")
                cat = sp[0]
                sentence = line[len(cat) + 1:].lower()

                fl = re.compile("[^\w']")
                sentence = fl.sub(' ', sentence)
                sentence = re.sub(' +', ' ', sentence)
                json_data = {
                    'text': sentence,
                    'label': cat
                }
                all_json.append(json_data)

    with open("trained_data.json", "w") as outfile:
        json.dump(all_json, outfile)

    f.close()

