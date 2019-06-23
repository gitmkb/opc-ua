from opcua import Client
import time

url = "opc.tcp://192.168.0.100:4040"

client = Client(url)

client.connect()
print('Client connected')

while(True):
    Temp = client.get_node("ns=2;i=2")
    Temperature = Temp.get_value()
    print(Temperature)
    
    Press = client.get_node("ns=2;i=3")
    Pressure = Press.get_value()
    print(Pressure)
    
    TIME = client.get_node("ns=2;i=4")
    TIME_value = TIME.get_value()
    print(TIME_value)
    
    time.sleep(1)
    