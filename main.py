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
    author = {
        "name": "Gaurav Thakur",
        "email": "email@gmail.com"
    }
    # book = {
    #     "title": "A book",
    #     "authors": [
    #         "42f3338d7e494c49acde37cd35ee8c90",
    #         "b3ca0816cf7a418896f494a9016bc16d"
    #     ]
    # }
    connection.connect()
    authors = Collection('authors')
    # books = Collection('books')
    # books.populate({
    #     "fieldRef": "authors",
    #     "to": "authors"
    # })
    # authors.insert(author)
    authors.update({"name": "Anikesh Patel"}, "name")
    # for i in range(100):
    #     col.insert(data)
    # authors.insert(author)
    # books.insert(book)
    # books.readAll()
    # col.readById('07a24a4b3ed246eb85613b9100d3daa5') # 42f3338d7e494c49acde37cd35ee8c90 # b3ca0816cf7a418896f494a9016bc16d
    # Book id - 6809f40002114f4490601b668d36a340
    # query = """
    #         name
    #         """
    # authors.execHyperQl(query)
    # col.execHyperQl(query)
    # col.readAll()
    # col.readOne(query)
    # if connection.connect():
    #     console.interact("Welcome to hyperShell", "Bye!")
    # else:
    #     print("Server is not running")
