import paho.mqtt.client as mqtt

def conectado(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.publish("altairlbn2020@gmail.com/t2")

def nuevoMensaje(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    mensaje=msg.payload.decode('utf-8')
    if mensaje=='ON':
        print('encendido')

    if mensaje=='OFF':
        print('apagado')
client= mqtt.Client()  
client.username_pw_set('altairlbn2020@gmail.com', password='Onepiece746')
client.on_connect = conectado
client.on_message = nuevoMensaje

client.connect("maqiatto.com", 1883, 60)

client.loop_forever()
