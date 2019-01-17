class human:
    
    def __init__(self, name = "Artem", age = 20):
        self.name = name
        self.age = age
       
    def say_hello(self):
        return "Hello, my name is {name}".format(name = self.name)

class Builder(human):
    def __init__(self, position = "student", name = None):
        super().__init__(name = name)
        self.position = position

    def say_hello(self):
        return "Hello, My name is {name}, and my positin is {position}".format(name = self.name, position = self.position)

class Writer(Human):
    def my_books(*args):
        return "I write {} books".format(len(args))
        pass

Jack = Writer(name = "Jack Kerouac")
print(Jack.my_books("On the road", "Mexico city blues")

Art = Builder(name = "Artem", position = "student")
print(Art.say_hello())
        
