class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(v1 + v2)
print(v1 - v2)
print(v1 * 2)
print(v2 / 2)

class Add:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return Add(self.value - other.value)
    def __repr__(self):
        return f"Add({self.value})"
a1 = Add(5)
a2 = Add(10)
a3 = Add(15)
print(a1 + a2 + a3)