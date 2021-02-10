import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

information = mydb.documents

for record in information.find():
    print('firstname is', record['firstname'], 'and lastname is',
          record['lastname'], 'and age =', record['age'])
