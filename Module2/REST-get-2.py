import requests
import json

# url = "https://api.thingspeak.com/channels/1360286/feeds.json?api_key=0199ZV7V0LHVX5ED&results=3"

url = 'http://192.168.0.107:5000/feeds.json?api_key=5HPX7SD7SCNT10MP'

response = json.loads(requests.get(url).content)

print(response)


