def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

    print(kwargs["add"])


calculate(2, add=3, multiply=5)


# print(add(3, 5, 6, 2, 1, 7, 4, 3))

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Opel")
print(my_car.make, my_car.model)
