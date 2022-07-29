import pymongo
import dns

client = pymongo.MongoClient("mongodb+srv://kakms:Kart123@cluster0.lh6u7hp.mongodb.net/?retryWrites=true&w=majority")
db = client.test

d={
    "name":"karthik",
    "age":32,
    "surname":"kumar"

}

db1=client['mongotest']
coll=db1["test"]
coll.insert_one(d)

