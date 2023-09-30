#larsstinkt

# testsite



def larsstinkt():
    print("Lars stinkt")


import json
 
# Opening JSON file



statics = open('gitignore/statics.json')
data = json.load(statics)
YOUR_API_TOKE = data["API_TOKEN"]
 
# Closing file
f.close()