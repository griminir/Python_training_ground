# class: blueprint for creating new objects
# object: instance of a class

# class: human
# object: john, mary, timmy

class Point:
    # class attributes
    default_color = 'red'

    # contstructor
    def __init__(self, x, y):
        # instance attributes
        self.x = x
        self.y = y

    # this just makes it so it returns this text instead of object x in memory x
    def __str__(self):
        return f"({self.x, self.y})"

    # use to compare if objects are the same since doing it without this method just returns false
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # use to check if one object is greater then another
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f'Point ({self.x}, {self.y})')


# factory method
point = Point(1, 2)
other = Point.zero()
print(point == other)
print(point > other)

point.draw()

another = Point(3, 4)
another.draw()

Point.default_color = 'green'
print(Point.default_color)  # class
print(point.default_color)  # object 1
print(another.default_color)  # object 2

print(type(point))
print(isinstance(point, Point))
