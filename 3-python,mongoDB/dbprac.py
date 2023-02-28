from pymongo import MongoClient
client = MongoClient('mongodb+srv://siwon:rlaznf11@cluster0.icysouv.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsiwon

doc1 = {
    'name': 'Alice',
    'age': 22
}

doc2 = {
    'name': 'Mike',
    'age': 19
}

db.users.insert_one(doc1)
db.users.insert_one(doc2)