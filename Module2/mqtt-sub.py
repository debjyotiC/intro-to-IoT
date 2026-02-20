import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with " + str(rc))
    client.subscribe("test/topic")


def on_message(client, userdata, msg):
    print(type(float(msg.payload.decode())))


client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 8080, 60)
client.loop_forever()
