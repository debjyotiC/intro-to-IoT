import pymongo

# MongoDB stuff
mongo_clinet = pymongo.MongoClient("mongodb://localhost:27017/")
db_connect = mongo_clinet["iot_server"]  # database name
db_collection = db_connect["sensor_data"]  # collection name

db_query = {"api_key": "5HPX7SD7SCNT10MP"}

db_reply = [i for i in db_collection.find(db_query)][-1]

print(db_reply)

#  -4   -3   -2   -1
# ['a', 'b', 'c', 'd']
#   0    1    2    3