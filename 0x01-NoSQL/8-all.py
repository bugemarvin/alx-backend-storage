#!/usr/bin/env python3
'''
function to list all docs in mongo
'''
import pymongo


def list_all(mongo_collection):
    '''
    print all lists
    '''
    details = mongo_collection.find()
    if details:
        return [values for values in details]
    else:
        return []
