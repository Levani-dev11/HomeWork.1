class Car:
    wheels = 4

    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year


car1 = Car("BMW", "შავი", 2020)
car2 = Car("Toyota", "თეთრი", 2018)

print(car1.brand, car1.wheels)
print(car2.brand, car2.wheels)

car2.wheels = 3

print(car1.wheels)
print(car2.wheels)
print(Car.wheels)

