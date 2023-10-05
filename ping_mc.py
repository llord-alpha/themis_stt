import os
hostname = "127.0.0.1" #example
response = os.system("ping " + hostname)
print(response)
#and then check the response...