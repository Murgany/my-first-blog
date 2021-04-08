class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if self.open_seats():
            self.passengers.append(name)
            return True
        else:
            return False

    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(3)

people = ['john', 'moses', 'simon', 'joseph']
for person in people:
    if flight.add_passenger(person):
        print(f'added {person} successfully')
    else:
        print(f'no seats available for {person}')


# decorators
def announce(f):
    def wrapper():
         print('about to run a func')
         f()
         print('done running func')
    return wrapper

@announce
def hello():
    print('hello world')


hello()

# lambda

people2 = [
    {"name": "harry", "city": "cairo"},
    {"name": "john", "city": "kampala"},
    {"name": "moses", "city": "arua"}
]


def f(person):
    return person["city"]


print(people2)

people2.sort(key=lambda person: person["name"])
print(people2)

