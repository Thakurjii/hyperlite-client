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
    connection = Connection(host='localhost', port=9898)
    Event.on('response', onResponse)
    data = {
        "name": "Anikesh patel",
        "email": "anikeshpatel4@gmail.com",
        "password": "123123"
    }
    connection.connect()
    col = Collection('users')
    col.insert(data)
    # query = """
    #         name = it,
    #         email = it,
    #         password = it
    #         """
    # col.execHyperQl(query)
    # if connection.connect():
    #     console.interact("Welcome to hyperShell", "Bye!")
    # else:
    #     print("Server is not running")
