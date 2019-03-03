import json
from .object import Object
from .cursor import Cursor
from .event import Event
from . import generateInsertRequestSchema,generateReadRequestSchema
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
        readSchema["Insert"]["meta"]["Database"] = DATABASE
        readSchema["Insert"]["meta"]["Collection"] = self.name
        Event.emmit('request', json.dumps(readSchema))

    def readAll(self):
        readSchema = generateReadRequestSchema()
        readSchema["Read"]["meta"]["Query"] = None
        readSchema["Insert"]["meta"]["Database"] = DATABASE
        readSchema["Insert"]["meta"]["Collection"] = self.name
        Event.emmit('request', json.dumps(readSchema))
