from hyperlite.collection import Collection

if __name__ == '__main__':
    usr_col = Collection("user")
    for obj in usr_col.get_all().get():
        print(obj)
