import pymongo
client = pymongo.MongoClient("mongodb+srv://Anamika:Pass1234@cluster0.33ckn1h.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d={
    "name" : "Anamika",
    "email":"aniverma2006@gmail.com",
    "surname":"sinha"
}

d={
    "name" : "Anamika",
    "email":"aniverma2006@gmail.com",
    "surname":"sinha"
}

d={
    "name" : "Anamika",
    "email":"aniverma2006@gmail.com",
    "surname":"sinha"
}

d={
    "name" : "Anamika",
    "email":"aniverma2006@gmail.com",
    "surname":"sinha"
}

db1=client['mongotest']
coll = db1['test']
coll.insert_one(d)