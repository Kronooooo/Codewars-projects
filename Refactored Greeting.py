class Person:
    def __init__(self,n):
        self.name = n

    def greet(self,n):
        return "Hello " + n + ", my name is " + self.name