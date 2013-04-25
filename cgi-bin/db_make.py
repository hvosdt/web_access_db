import shelve
from person import Person, Manager

bob = Person('Bob Smith', 45, 40000, 'developer')
sue = Person('Sue Jones', 40, 50000, 'hardware')
tom = Manager('Tom Stone', 30, 30000)

db = shelve.open('people-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close()

if __name__ == '__main__':
    db = shelve.open('people-shelve')
    for key in db:
        print(db[key].name)
    db.close()

