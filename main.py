from hyperlite.collection import Collection
from hyperlite import Connection
from hyperlite.event import Event
from code import InteractiveConsole


def onResponse(response: str):
    print(response)


if __name__ == '__main__':
    connection = Connection(host='localhost', port=9898)
    Event.on('response', onResponse)
    if connection.connect():
        console = InteractiveConsole(globals())
        console.interact("Welcome to hyperShell", "Bye!")
    else:
        print("Server is not running")
    # print(usr_col.get_all().get())
    # for obj in usr_col.get_all().get():
    #     print(obj)
