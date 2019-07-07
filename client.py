from opcua import Client
import time
import mysql.connector
import datetime

use_crypto = True


url = "opc.tcp://192.168.0.101:4840"

client = Client(url)
client._username = "OpcUaClient"
client._password = "123456789"
client.set_user("OpcUaClient")
client.set_password("123456789")
client.connect()

print('Client connected')


while(True):
        
            R = client.get_node("ns=2;s=/Channel/Parameter/R")
            R_value = R.get_value()
            print(R_value)
            Date_Time = datetime.datetime.now()
            aaCurr = client.get_node("ns=2;s=/Channel/MachineAxis/aaCurr")
            aaCurr_value = aaCurr.get_value();
            print(aaCurr_value)
            actParts = client.get_node("ns=2;s=/Channel/State/actParts")
            actParts_value = actParts.get_value()
            print(actParts_value)
            DB100 = client.get_node("ns=2;s=/Plc/DB100.DBW")
            DB100_value = DB100.get_value()
            print(DB100_value)
            time.sleep(1)
            mydb = mysql.connector.connect(host="localhost", user="root", password="Srs@2017",database="testschema" )
            mycursor = mydb.cursor()
            sql = "INSERT INTO sinumerik4(Date_Time, R, aaCurr, actParts, DB100) VALUES (%s, %s, %s, %s, %s)"
            mycursor.execute(sql, [str(Date_Time), str(R_value), str(aaCurr_value), str(actParts_value), str(DB100_value)] )
            mydb.commit()


