from . import cursor
from . import object


class Collection:
    def __init__(self, name: str):
        self.name = name
        self.objects: cursor.Cursor

    def get_all(self) -> cursor.Cursor:
        # Logic to fetch add objects of this collection object
        # We get total_page 20 and per page object will 10 it mean total objects is 10*20
        # Dummy data for now
        data = [
            object.Object({
                "name": "Anikesh Patel",
                "email": "developeranikesh@gmail.com",
            }, self),
            object.Object({
                "name": "Gaurav Thakur",
                "email": "gauravthakur@gmail.com",
            }, self),
            object.Object({
                "name": "Sohel Shaikh",
                "email": "sohel@gmail.com",
            }, self)
        ]
        cursor = cursor.Cursor(total_page=20, data=data)

        return cursor
