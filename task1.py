class Task1:
    def __init__(self):
        self.a = 0

    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        if isinstance(other, Task1):
            return self.a + other.a
        return self.a + other

    def __str__(self):
        return self.a


print(Task1(5) + Task1(4))
