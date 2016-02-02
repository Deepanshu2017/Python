# Below is not the actual implementation of Points on plane
# They are just for demonstration purpose only

class Point:

    def __new__(cls, **kwargs):
        obj = object().__new__(cls)
        return obj

    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            self.__setattr__(name, value)

    def __add__(self, obj):
        return Point(x = self.x + obj.x, y = self.y + obj.y)

    def __sub__(self, obj):
        return Point(x = self.x - obj.x, y = self.y - obj.y)

    def __mul__(self, obj):
        return Point(x = self.x * obj.x, y = self.y * obj.y)

    def __truediv__(self, obj):
        return Point(x = self.x / obj.x, y = self.y / obj.y)

    def __floordiv__(self, obj):
        return Point(x = self.x // obj.x, y = self.y // obj.y)

    def __pow__(self, num):
        return Point(x = self.x ** num, y = self.y ** num)

    def __mod__(self, num):
        return Point(x = self.x % num, y = self.y % num)

    def __lshift__(self, num):
        return Point(x = self.x << num, y = self.y << num)

    def __rshift__(self, num):
        return Point(x = self.x >> num, y = self.y >> num)

    def __and__(self, num):
        return Point(x = self.x & num, y = self.y & num)

    def __or__(self, num):
        return Point(x = self.x | num, y = self.y | num)

    def __xor__(self, num):
        return Point(x = self.x ^ num, y = self.y ^ num)

    def __invert__(self):
        return Point(x = ~self.x, y = ~self.y)

    def __lt__(self, obj):
        return True if self.x < obj.x else ( True if self.y < obj.y else False)

    def __le__(self, obj):
        return True if self.x <= obj.x else ( True if self.y <= obj.y else False)

    def __gt__(self, obj):
        return True if self.x > obj.x else ( True if self.y > obj.y else False)

    def __ge__(self, obj):
        return True if self.x >= obj.x else ( True if self.y >= obj.y else False)

    def __eq__(self, obj):
        return True if self.x == obj.x and self.y == obj.y else False

    def __ne__(self, obj):
        return True if self.x != obj.x and self.y != obj.y else False

    def __repr__(self):
        return '{0} and {1}'.format(self.x, self.y)

    def __contains__(self, var):
        return True if var == self.x or var == self.y else False

if __name__ == '__main__':
    print(Point(x = 1, y = 2) + Point(x = 2, y = 1))
    print(Point(x = 1, y = 2) - Point(x = 2, y = 1))
    print(Point(x = 1, y = 2) * Point(x = 2, y = 1))
    print(Point(x = 1, y = 2) / Point(x = 2, y = 1))
    print(Point(x = 1, y = 2) // Point(x = 2, y = 1))
    print(Point(x = 1, y = 2) ** 2)
    print(Point(x = 1, y = 2) % 2)
    print(Point(x = 1, y = 2) << 2)
    print(Point(x = 1, y = 2) >> 2)
    print(Point(x = 1, y = 2) & 2)
    print(Point(x = 1, y = 2) | 2)
    print(Point(x = 1, y = 2) ^ 2)
    print(~Point(x = 1, y = 2))
    print(Point(x = 1, y = 2) < Point(x = 2, y = 1))
    print(Point(x = 1, y = 2) <= Point(x = 2, y = 1))
    print(Point(x = 1, y = 2) > Point(x = 2, y = 1))
    print(Point(x = 1, y = 2) >= Point(x = 2, y = 1))
    print(Point(x = 1, y = 2) != Point(x = 2, y = 1))
    print(Point(x = 1, y = 2) == Point(x = 2, y = 1))
    print(3 in Point(x = 1, y = 2))
