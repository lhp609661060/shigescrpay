# coding=utf-8

import pymongo

DB_HOST = "127.0.0.1"
DB_PORT = 27037

client = None

def get_client():

    global client

    if client:
        return client

    client = pymongo.MongoClient(DB_HOST, DB_PORT)

    return client


def search_spider_info(data):
    return client['spider'].find()

def update_spider_info(data):
    pass


if __name__ ==  '__main__':
    print "pymongo test"

    def test_insert():
        dbtest = client["dbtest"]
        tabletest = dbtest['tabletest']

        inserted_id = tabletest.insert_one({'name': 'lhp', 'age': 89}).inserted_id
        print inserted_id

        print tabletest.find_one()

        print tabletest.find_one({'_id': inserted_id})
