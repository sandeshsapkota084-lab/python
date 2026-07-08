class Flyable:
    def fly(self):
        print("Flying!")

class Swimmable:
    def swim(self):
        print("Swimming!")

class Duck(Flyable, Swimmable):
    def quack(self):
        print("Quack!")

d = Duck()
d.fly()    # From Flyable
d.swim()   # From Swimmable
d.quack()  # Own method

class LogMixin:
    def log(self, message):
        print(f"[LOG] {message}")

class JsonMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class User(LogMixin, JsonMixin):
    def __init__(self, name, email):
        self.name = name
        self.email = email

u = User("Alice", "[email protected]")
u.log("User created")       # [LOG] User created
print(u.to_json())          # {"name": "Alice", "email": "[email protected]"}

#Recreate the A-B-C-D diamond example. Before running it, predict the output. Then run it and compare. Print D.__mro__ to verify.
class A:
    def __init__(self):
        print("A init")
class B(A):
    def __init__(self):
        super().__init__()
        print("B init")
class C(A):
    def __init__(self):
        super().__init__()
        print("C init")
class D(B, C):
    def __init__(self):
        super().__init__()
        print("D init")
d = D()
print(D.__mro__)

#Create a diamond where A has a greet() method, B and C override it differently. Call D().greet() and observe which version runs.
class A:
    def greet(self):
        print("Hello from A!")
class B(A):
    def greet(self):
        print("Hello from B!")
class C(A):
    def greet(self):
        print("Hello from C!")
class D(B, C):
    pass
d = D()
d.greet()

#Modify the diamond example so that B calls A.__init__(self) directly instead of super().__init__(). Observe how A's init runs twice. Then fix it.
class A:
    def __init__(self):
        print("A init")
class B(A):
    def __init__(self):
        A.__init__(self)
        print("B init")
class C(A):
    def __init__(self):
        A.__init__(self)
        print("C init")
class D(B, C):
    def __init__(self):
        super().__init__()
        print("D init")
d = D()