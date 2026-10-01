import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("broker.consentiumiot.com", 1883, 60)

sensor_data_temp = 25

client.publish('temp/sensor_0', sensor_data_temp)
client.disconnect()
