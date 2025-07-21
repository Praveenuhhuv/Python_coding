class Shape:
    def area(self):
        return "undefined"

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2


shapes = [Rectangle(2, 3), Circle(5)]

# Iterating through the list and printing areas
for s in shapes:
    print(f"Area: {s.area()}")
