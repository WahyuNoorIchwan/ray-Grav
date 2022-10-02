import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["database"]

table = database["properties"]

# Insert Data
batch = {"project_name": "Hanalulu", "Data": "Gravity"}
x = table.insert_one(batch)

