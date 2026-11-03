class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

    def info(self):
        print(f"{self.name}: ფართობი = {self.area()}")


class Rectangle(Shape):
    def __init__(self, width, height, name="მართკუთხედი"):
        super().__init__(name)
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("სიგანე უნდა იყოს დადებითი")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("სიმაღლე უნდა იყოს დადებითი")
        self.__height = value

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side, "კვადრატი")


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("წრე")

        if radius <= 0:
            raise ValueError("რადიუსი უნდა იყოს დადებითი")

        self.radius = radius

    def area(self):
        return round(3.14 * self.radius ** 2, 2)


def total_area(shapes):
    total = 0

    for shape in shapes:
        total += shape.area()

    return round(total, 2)


def largest(shapes):
    biggest = shapes[0]

    for shape in shapes:
        if shape.area() > biggest.area():
            biggest = shape

    return biggest


# ფიგურების შექმნა
shapes = [
    Rectangle(4, 5),
    Square(3),
    Circle(2),
    Shape("უცნობი ფიგურა")
]

# თითოეული ფიგურის ინფორმაციის დაბეჭდვა
for shape in shapes:
    shape.info()

print("ჯამური ფართობი:", total_area(shapes))
print("უდიდესი:", largest(shapes).name)

# მართკუთხედების დათვლა, კვადრატის ჩათვლით
rectangle_count = 0

for shape in shapes:
    if isinstance(shape, Rectangle):
        rectangle_count += 1

print(
    "მართკუთხედების რაოდენობა (კვადრატის ჩათვლით):",
    rectangle_count
)

# არასწორი მნიშვნელობების შემოწმება
try:
    Circle(-3)
except ValueError as error:
    print("შეცდომა:", error)

try:
    Square(0)
except ValueError as error:
    print("შეცდომა:", error)