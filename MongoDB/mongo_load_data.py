
from pymongo import MongoClient
import random


def upload_data() -> None:

    n = 20
    data_points = [{'time': float(j) / n,
                    'bid': random.gauss(0, 1),
                    'ask': random.gauss(0, 1)} for j in range(0, n)]

    # Mongo is running as a service in windows, it logs to C:\\data\\log\\mongo.log'
    # Log can be accessed with tail -f ....log from git bash in visual studio code
    client = MongoClient('mongodb://localhost:27017/')

    # connect to portfolio database
    db = client['portfolio']

    # get collection 'crypto_portfolio'
    collection = db['crypto_portfolio']

    # remove all documents from collection
    collection.remove()
    collection.insert_many(data_points)

    client.close()


def map_reduce():
    # https://docs.mongodb.com/manual/core/map-reduce/
    pass


def query_data() -> None:

    client = MongoClient('mongodb://localhost:27017/')

    db = client['portfolio']
    collection = db['crypto_portfolio']

    print('Query collection for condition')
    result = collection.find({'time': {'$in': [0, 0.1, 0.2, 0.3]},
                              'bid': {'$gt': 0.0}})
    for p in result:
        print(p)

    client.close()


upload_data()
query_data()
