import time # libreria de tiempo
import network  # libreria para conectarse a la red
import random 


wlan=network.WLAN(network.STA_IF) # Crear la interfaz
wlan.active(False)
wlan.active(True) # Cuando se activa saldra un True
wlan.scan() 
wlan.isconnected()
wlan.connect('JORGE_CNT.','lapulga1999')

time.sleep(5)
wlan.config('mac')
wlan.ifconfig()
print(wlan.ifconfig())
print('conectado...',wlan.isconnected())

from machine import Pin
pin=Pin(4,Pin.OUT)
if wlan.isconnected():
    pin.on()
else:
    pin.off()

Pin18=Pin(18,Pin.IN)
Pin5=Pin(5,Pin.IN)

from umqtt.simple import MQTTClient
client=MQTTClient('Jean','maqiatto.com',1883,'altairlbn2020@gmail.com','Onepiece746')

def holamundo(tcp,msg):
    print(msg)
    mensaje=msg.decode('utf-8')
    if mensaje=='RegistroSensores':
        RegistroSensores=open('registrodesensores.txt','r')
        valorRegistro=RegistroSensores.readlines()
        
        Registro='Registro_'
        
        for valor in valorRegistro:
            Registro=Registro+valor
        client.publish('altairlbn2020@gmail.com/t1',Registro)
    
client.set_callback(holamundo)
client.connect()
time.sleep(3)
#client.publish('gabyllanga-15@outlook.com/t1','111')
client.subscribe('altairlbn2020@gmail.com/t2')

registro1Doc=open('registrodesensores.txt','w')
registro1Doc.close()

while True:
    time.sleep(0.5)
    estadoBoton1=Pin18.value()#Sensor1
    estadoBoton2=Pin5.value()#Sensor2
    
    if estadoBoton1:    
        registroDoc=open('registrodesensores.txt','a')
        registroDoc.write('Estado Sensor1:'+str(estadoBoton1)+'-'+'Estado Sensor2:'+str(estadoBoton1)+'\n')
        VectorTiempo=time.gmtime()
        fecha=str(VectorTiempo[2])+'/'+str(VectorTiempo[1])+'/'+str(VectorTiempo[0])
        hora=str(VectorTiempo[3])+':'+str(VectorTiempo[4])+':'+str(VectorTiempo[5])
        registroDoc.write('Fecha de activacion de sensor 1: '+fecha+'-'+hora+'\n')
        registroDoc.close()

    sensores=str(estadoBoton1)+"-"+str(estadoBoton2)
    client.publish('altairlbn2020@gmail.com/t1',sensores)
    client.check_msg()