from hyperlite.collection import Collection
from hyperlite import *
from hyperlite.event import Event
from code import InteractiveConsole

connection = None
console = InteractiveConsole(globals())
import json


def onResponse(response: str):
    data = json.loads(response)
    data = json.dumps(data, indent=4, sort_keys=True)
    print(data)


def onRequest(request: str):
    if connection is not None:
        connection.sendRequest(request)


if __name__ == '__main__':
    connection = Connection(host='localhost', port=8989)
    Event.on('response', onResponse)
    connection.connect()
    showDatabases()
    showCollections('test.db')
    cities = Collection('cities')
    cities.insert({"name":"indore"})
    # cities.execHyperQl("city")
    # cities.execHyperQl("*, city &eq \"KETCHIKAN\"")
    # cities.execHyperQl("*, city &eq \"KETCHIKAN\", state &eq \"AK\", $limit: 1, $skip: 1")
    # cities.readAll()
    # with open(r"C:\Users\Anikesh\Desktop\zips.json") as dataset:
    #     for object in dataset.readlines():
    #         pass

    # if connection.connect():
    #     console.interact("Welcome to hyperShell", "Bye!")
    # else:
    #     print("Server is not running")
