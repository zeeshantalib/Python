class Head(object):

    def __init__(self, eye_color, hair_color):
        self.eye_color = eye_color
        self.hair_color = hair_color

class Body(object):

    def __init__(self, weight):
        self.weight = weight

class Person(object):

    def __init__(self, eye_color, hair_color, weight):
        self.head = Head(eye_color, hair_color)
        self.body = Body(weight)

    def print_eye_color(self):
        print(self.head.eye_color)

zeeshan = Person('blue', 'blonde', 160)
zeeshan.print_eye_color()

'''
- when you have objects made up of other objects
- used to create complex objects by putting together simple objects

In this example, we can compose a Person object by combining
 a Head and a Body class. '''
