import json
from .object import Object
from .cursor import Cursor
from .event import Event
from . import generateReadRequestSchema, generateReadByIdRequestSchema, generateReadOneRequestSchema, generateInsertRequestSchema, generateDeleteRequestSchema, generateUpdateRequestSchema, generateUpdateRequestSchema, generateInsertAllRequestSchema
from . import DATABASE


class Collection(object):
    def __init__(self, name: str):
        self.name = name
        self.objects: Cursor

    def insert(self, obj):
        insertSchema = generateInsertRequestSchema()
        insertSchema["Insert"]["data"] = obj
        insertSchema["Insert"]["meta"]["Database"] = DATABASE
        insertSchema["Insert"]["meta"]["Collection"] = self.name
        Event.emmit('request', json.dumps(insertSchema))

    def execHyperQl(self, query):
        readSchema = generateReadRequestSchema()
        readSchema["Read"]["meta"]["Query"] = query
        readSchema["Read"]["meta"]["Database"] = DATABASE
        readSchema["Read"]["meta"]["Collection"] = self.name
        Event.emmit('request', json.dumps(readSchema))

    def readAll(self):
        readSchema = generateReadRequestSchema()
        readSchema["Read"]["meta"]["Query"] = "*"
        readSchema["Read"]["meta"]["Database"] = DATABASE
        readSchema["Read"]["meta"]["Collection"] = self.name
        Event.emmit('request', json.dumps(readSchema))

    def readOne(self, query="*"):
        readSchema = generateReadOneRequestSchema()
        readSchema["ReadOne"]["meta"]["Query"] = query
        readSchema["ReadOne"]["meta"]["Database"] = DATABASE
        readSchema["ReadOne"]["meta"]["Collection"] = self.name
        Event.emmit('request', json.dumps(readSchema))

    def readById(self, objectId: str):
        readSchema = generateReadByIdRequestSchema()
        readSchema["ReadById"]["meta"]["Database"] = DATABASE
        readSchema["ReadById"]["meta"]["Collection"] = self.name
        readSchema["ReadById"]["meta"]["id"] = objectId
        Event.emmit('request', json.dumps(readSchema))

    def populate(self, obj: dict):
        if 'fieldRef' not in obj:
            raise ValueError("'from' is required")
        if 'to' not in obj:
            raise ValueError("'to' is required")
        obj.update({'type': 'Pipeline', 'Database': DATABASE, 'Collection': self.name})
        Event.emmit('request', json.dumps(obj))

    def update(self, obj: dict, query="*"):
        updateSchema = generateUpdateRequestSchema()
        updateSchema["Update"]["data"] = obj
        updateSchema["Update"]["meta"]["Database"] = DATABASE
        updateSchema["Update"]["meta"]["Collection"] = self.name
        updateSchema["Update"]["meta"]["Query"] = query
        Event.emmit('request', json.dumps(updateSchema))

    def delete(self, obj_id: str):
        deleteSchema = generateDeleteRequestSchema()
        deleteSchema["Delete"]["meta"]["Database"] = DATABASE
        deleteSchema["Delete"]["meta"]["Collection"] = self.name
        deleteSchema["Delete"]["meta"]["Object_Id"] = obj_id
        Event.emmit('request', json.dumps(deleteSchema))

    def insertAll(self, objects: list):
        isValid = False
        if type(objects) is list:
            for hy_object in objects:
                if type(hy_object) is dict:
                    isValid = True
                else:
                    isValid = False
                    break
        
        if isValid:
            insertAllSchema = generateInsertAllRequestSchema()
            insertAllSchema["InsertAll"]["data"] = objects
            insertAllSchema["InsertAll"]["meta"]["Database"] = DATABASE
            insertAllSchema["InsertAll"]["meta"]["Collection"] = self.name
            Event.emmit('request', json.dumps(insertAllSchema))
        else:
            print("Invalid data for Insertion.")