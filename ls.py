#larsstinkt
import json
import time
import os.path
# testsite

# test2


class JsonParser:
    def __init__(self, destination = None): 
        if destination == None:                     # if no destination is specified, use standart destination
            print("No destination specified. Use standart destination: gitignore/properties.json")
            destination = "gitignore/AAAproperties.json"
        self.destination = destination
        try:
            print("Loading JSON File:")
            with open(self.destination, "r") as f:      # load json contents
                self.data = json.load(f)
            print("JSON File loaded.-----------------------------------------------------------")
        except:
            with open(self.destination, "w") as f:    # create new json file if file is empty   
                print("JSON File -->", destination, "<-- empty. Creating new file.")
                self.data = {}
                json.dump(self.data, f, indent=4)
    def checkexistance(self, key = None):
        if key == None:
            return os.path.isfile(self.destination)
        else:
            try:
                self.data[key]
                return True
            except:
                return False
    def get_json(self, key):
        try:                                    # try to get value from json file
            with open(self.destination, "r") as f:
                self.data = json.load(f)
            return self.data[key]
        except:
            return None
    def write_json(self, key, value):
        self.data[key] = value
        with open(self.destination, 'w') as f:
            json.dump(self.data, f, indent=4)












a = JsonParser("gitignore/AAAproperties.json")
print(a.get_json("API_TOKEN"))
a.write_json("Test", 99999)

while True:
    time.sleep(1)
    inpuut = input("Enter: ")
    testr = input("Enter2: ")
    a.write_json(inpuut, testr)
    print(a.get_json(inpuut))
    tee = input("Enter3: ")
    print(a.checkexistance("friederich"))