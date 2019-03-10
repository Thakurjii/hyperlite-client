from hyperlite.collection import Collection
from hyperlite import Connection
from hyperlite.event import Event
from code import InteractiveConsole

connection = None
console = InteractiveConsole(globals())


def onResponse(response: str):
    print(response)


def onRequest(request: str):
    if connection is not None:
        connection.sendRequest(request)


if __name__ == '__main__':
    connection = Connection(host='localhost', port=8989)
    Event.on('response', onResponse)
    data = {
        "name": "Anikesh Patel",
        "email": "anikeshpatel@gmail.com",
        "password": "123123",
        "age": 19,
        "addr": {
            "country": "India",
            "geo": {
                "lat": "-105.45443",
                "lon": "182.43445"
            }
        }
    }
    connection.connect()
    col = Collection('users')
    # for i in range(100):
    #     col.insert(data)
    col.insert(data)
    # col.readById('8cf8438062554a8487ce64bef8189ea1')
    query = """
            name,
            addr.geo.lat &eq "-105.45443"
            """
    col.execHyperQl(query)
    # col.readAll()
    # col.readOne(query)
    # if connection.connect():
    #     console.interact("Welcome to hyperShell", "Bye!")
    # else:
    #     print("Server is not running")
