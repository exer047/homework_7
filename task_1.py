class Car:
    def __init__(self, model, color, year, price):
        self.model = model
        self.color = color
        self.year = year
        self.price = price

    def __eq__(self, other):
        [
            self.model,
            self.color,
            self.year,
            self.price
        ] == [
            other.model,
            other.color,
            other.year,
            other.price
        ]

    def __str__(self):
        string = f"Model: {self.model}\n" \
                 f"Color: {self.color}\n" \
                 f"Year: {self.year}\n" \
                 f"Price: {self.price}"
        return string


class ShowRoom:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self._cars = []

    def add_car(self, car):
        self._cars.append(car)

    def sell_car(self, car):
        if car in self._cars:
            self._cars.remove(car)
            print("You successfully sold the car!")
        else:
            print("No car to sell")

    def show_all(self):
        # print("\n\n".join(map(str, self.cars)))
        string = ""
        for car in self._cars:
            string = string + str(car) + "\n\n"
        print(string)


if __name__ == '__main__':
    car1 = Car("Audi", "Red", "1999", "$12000")
    car2 = Car("Bmw", "Black", "2009", "$18000")
    car3 = Car("Toyota", "Silver", "2015", "$25000")
    # print(car1, car2, car3)
    # print()

    showroom = ShowRoom("Borshagovska, 17", "First showroom")

    showroom.add_car(car1)
    showroom.add_car(car2)
    showroom.add_car(car3)

    showroom.show_all()

    showroom.sell_car(car2)

    showroom.show_all()
