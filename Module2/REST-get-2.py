import requests
import json

# url = "https://api.thingspeak.com/channels/1360286/feeds.json?api_key=0199ZV7V0LHVX5ED&results=3"

url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=730&date=15-05-2021'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
result = json.loads(requests.get(url, headers=headers).content)

