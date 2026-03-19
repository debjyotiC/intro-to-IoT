import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("172.105.59.82", 1883, 60)
sensor_data_temp = 24.3
client.publish('test/topic', sensor_data_temp)
client.disconnect()
