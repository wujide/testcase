# coding=utf-8
# __author__='Administrator'


import shelve


def store_person(db):
    pid = raw_input("Enter unique ID number:")
    person = {}
    person['name'] = raw_input("Enter name: ")
    person['age'] = raw_input("Enter age: ")
    person['phone'] = raw_input("Enter phone: ")
    db[pid] = person


def lookup_person(db):
    pid = raw_input("Enter ID number: ")
    field = raw_input("(name, age, phone)")
    field = field.strip().lower()
    print field.capitalize() + ':', db[pid][field]


def enter_command():
    cmd = raw_input("Enter command: ")
    cmd = cmd.strip().lower()
    return cmd


def main():
    database = shelve.open('test.dat')
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == 'quit':
                return
    finally:
        database.close()


if __name__ == '__main__':
    main()





