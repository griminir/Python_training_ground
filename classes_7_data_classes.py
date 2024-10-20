from collections import namedtuple

# if working with classes that have only data and no methods you might wanna use a namedtuple instead
# namedtuples are immutable once made they can not be modified
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)
