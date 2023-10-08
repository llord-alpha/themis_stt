import os
hostname = "127.0.0.1" #example
while True:
    response = os.system("ping -1 t  " + hostname)
    print(response)
#and then check the response...