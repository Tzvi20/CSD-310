
from pymongo import MongoClient

mongodb_url = 'mongodb+srv://admin:admin@cluster0.cjljgrs.mongodb.net/'

client = MongoClient(mongodb_url)

db = client["pytech"]

students = db["students"]
fred = {
    "first_name": "Fred"
}# this line code inserts fred
fred_student_id = students.insert_one(fred).inserted_id
print(fred_student_id)

new_students = [
    {"student_id": "1007", "first_name": "Alice"},
    {"student_id": "1008", "first_name": "Bob"},
    {"student_id": "1009", "first_name": "Charlie"}
]
#this line of code update alice to alex
result = db.students.update_one({"student_id": "1007"}, {"$set": {"first_name": "alex"}})
print(result)

docs = students.find({})
for doc in docs:
    print(doc)

#doc = students.find_one({"student_id": "1007"})
#print(doc["student_id"])







