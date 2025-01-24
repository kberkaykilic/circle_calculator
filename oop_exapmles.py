import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_circle_area(self):
        return math.pi * self.radius**2

    def calculate_circle_perimeter(self):
        return 2 * math.pi * self.radius

radius = float(input("Give a value for radius of the circle: "))

circle = Circle(radius)

area = circle.calculate_circle_area()
print("Area of the circle: ", area)

perimeter = circle.calculate_circle_perimeter()
print("Perimeter of the circle", perimeter)