import requests
import json

url = "https://api.thingspeak.com/channels/1360286/feeds.json?api_key=0199ZV7V0LHVX5ED&results=3"

response = json.loads(requests.get(url).content)

print(float(response['feeds'][2]['field1']))


