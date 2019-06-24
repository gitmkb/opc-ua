from opcua import Client
import time
from opcua.tools import get_node
import csv
from asyncore import write
from getcsv import csvData

url = "opc.tcp://DESKTOP-N5AIHVF:48020"

client = Client(url)

client.connect()
print('Client connected')

# root = client.get_root_node()
# print(root)

# print(root.get_children())

# print(get_server_node())

# print(client.get_server_node())

# print('server nodes start from here:')
# print(client.get_server_node())
# k = client.get_objects_node()
# print(k)

# kk = client.get_children_descriptions()
# print(kk)

# print(client.get_node(6252))

while(True):
    Temp = client.get_node("ns=4;i=6252")
    Temperature = Temp.get_value()
    print(Temperature)  
    TIME = client.get_node("ns=0;i=2258")
    TIME_value = TIME.get_value()
    csvData = [ [ str(Temperature), str(TIME_value) ] ]
    with open('mycsv2.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(csvData)
    print(TIME_value)
    
    time.sleep(1)

csvFile.close()