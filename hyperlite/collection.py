from .object import Object
from .cursor import Cursor


class Collection(object):
    def __init__(self, name: str):
        self.name = name
        self.objects: Cursor

    def get_all(self) -> Cursor:
        # Logic to fetch add objects of this collection object
        # We get total_page 20 and per page object will 10 it mean total objects is 10*20
        # Dummy data for now
        data = [
            Object({
                "name": "Anikesh Patel",
                "email": "developeranikesh@gmail.com",
            }, self),
            Object({
                "name": "Gaurav Thakur",
                "email": "gauravthakur@gmail.com",
            }, self),
            Object({
                "name": "Sohel Shaikh",
                "email": "sohel@gmail.com",
            }, self)
        ]
        cur = Cursor(total_page=20, data=data)

        return cur
