class human:
    def __init__(self, name = "Artem", age = 20):
        self.name = name
        self.age = age

    def say_hello(self):
        return "hello, my name is {} and i am {}".format(self.name, self.age)

class builder(human):
    def __init__(self, position = "student", name = None, age = None):
        super().__init__()
        self.position = position
    def say_hello(self):
        return "Hello, my name is {}, i am {} and my position is {}".format(self.name, self.age, self.position)

class writer(human):
    def my_books(*args):
        return "i write {} books".format(len(args))
    pass




#test = human()
test2 = builder()
test3 = writer(name = Jack Kerouac)
#print(test.say_hello())
print(test2.say_hello())
print(test3.my_books("On the road" "Mexico City Blues"))
