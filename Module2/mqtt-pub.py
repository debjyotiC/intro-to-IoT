
import paho.mqtt.client as mqtt

sensor_data = '24.3'

client = mqtt.Client()
client.connect("mqtt.eclipseprojects.io", 1883, 60)

client.publish('topic/test', sensor_data)

client.disconnect()