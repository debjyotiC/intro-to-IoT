import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with " + str(rc))
    client.subscribe("topic/test")


def on_message(client, userdata, msg):
    print(msg.payload.decode())


client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)
client.loop_forever()
