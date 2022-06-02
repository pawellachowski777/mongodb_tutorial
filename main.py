from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

cluster = 'mongodb+srv://pawel:PLbaton1998@cluster0.ci9lhuk.mongodb.net/test?retryWrites=true&w=majority'
client = MongoClient(cluster)
print(client.list_database_names())

db = client.test

print(db.list_collection_names())

# dodawanie danych
todo1 = {"name": "Patric", "text": "list todo", "status": "open", "tags": ["python", "coding"],
         "date": datetime.datetime.utcnow()}

todos = db.todos

# result = todos.insert_one(todo1)

todo2 = [
    {"name": "Patric", "text": "list todo 2", "status": "open", "tags": ["python", "coding"],
     "date": datetime.datetime.utcnow()},
    {"name": "Patric", "text": "list todo 3", "status": "open", "tags": ["c++", "coding"],
     "date": datetime.datetime(2021, 1, 1, 10, 45)}
]
# result = todos.insert_many(todo2)

# wyszukiwanie
result_id = todos.find_one({"_id": ObjectId("6299181845a2e46fef239e7d")})
print('wyszukiwanie po id \n', result_id)

result_name = todos.find({"name": "Patric"})
print('wyszukiwanie po imieniu')
for result in result_name:
    print(result)

date_less = datetime.datetime(2022, 1, 5)
result_condition = todos.find({'date': {'$lt':  date_less}})
print('wyszukiwnie z warunkiem')
# https://www.mongodb.com/docs/manual/reference/operator/query/
for result in result_condition:
    print(result)

# print(todos.count_documents({}))


# aktualizowanie
update_status = todos.update_one({'tags': 'c++'}, {'$set': {"status": "done"}})

update_tags = todos.update_one({'_id': ObjectId('6299152bfcc3f5ee19740ed9')}, {'$addToSet': {'tags': 'web'}})
print('aktualizacja tagu')
