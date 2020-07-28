import serial
import pandas as pd

x = []
y = []
ser = serial.Serial('/dev/ttyUSB0', 9600)
for i in range(11):
    arduinoData = ser.readline().decode('utf-8"')
    x.append(arduinoData[0:5]) 
    y.append(arduinoData[6:11])
    # print(type(arduinoData))
    # print(arduinoData)
    print("\nUmidade {}\t Temperatura {}\n".format(x[i],y[i]))

df = pd.DataFrame(columns=['Umidade','Temperatura'])
df['Umidade'] = x
df['Temperatura'] = y

print(df.head(10))