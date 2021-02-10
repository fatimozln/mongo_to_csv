import pymongo
import csv

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

information = mydb.documents

for record in information.find():
    print('firstname is', record['firstname'], 'and lastname is',
          record['lastname'], 'and age =', record['age'])


with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['firstname', 'lastname', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for record in information.find():
        writer.writerow(
            {'firstname': record['firstname'], 'lastname': record['lastname'], 'age': record['age']})
