import pymongo

client = pymongo.MongoClient("mongodb+srv://Anamika:Pass1234@cluster0.33ckn1h.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database =client['myinfo']
collection =database["Anamika"]





record = collection.find()
for i in record:
    print(i)