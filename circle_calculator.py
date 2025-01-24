import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_circle_area(self):
        return math.pi * self.radius**2

    def calculate_circle_perimeter(self):
        return 2 * math.pi * self.radius

while True:
    print("""Hello, welcome to Circle calculator! Please select one.
1- Calculate Circle Area.
2- Calculate Circle Perimeter.
3- Quit.""")
    try:
        user_input = int(input("Your choice: "))
        if user_input == 1:
            radius = float(input("Give a value for radius of the circle: "))
            circle = Circle(radius)
            area = circle.calculate_circle_area()
            print("Area of the circle: ", area)
        elif user_input == 2:
            radius = float(input("Give a value for radius of the circle: "))
            circle = Circle(radius)
            perimeter = circle.calculate_circle_perimeter()
            print("Perimeter of the circle: ", perimeter)
        elif user_input == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option (1, 2, or 3).")
    except ValueError:
        print("Invalid input! Please enter a number.")
