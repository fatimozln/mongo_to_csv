import random
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

information = mydb.documents

first_names = ['ali', 'amin', 'sara', 'fati', 'amir']
last_names = ['akbari', 'rezayi', 'mosavi', 'ahmadi', 'amini']
ages = ['20', '30', '40', '50', '60']


def random_user():
    users = []
    counter = 1
    while counter < 11:
        # print("user", counter, " = name =", random.choice(first_names), "and lastname =",
        # random.choice(last_names), "and ", random.choice(ages), "years old")
        dict_name = {
            'firstname': random.choice(first_names),
            'lastname': random.choice(last_names),
            'age': random.choice(ages)
        }
        users.append(dict_name)
        counter += 1

    return users


def insert_to_database():
    users = random_user()
    information.insert_many(users)


insert_to_database()
