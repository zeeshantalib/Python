class Rectangle(object):

    @staticmethod
    def calculate_area(width, height):
        return width * height

# User does not need to know formula to get area of Rectangle
area = Rectangle.calculate_area(5, 7)
print(area)

'''
- a way that you can provide a simple interface for users 
while hiding the complexity

To use a microwave, you don't need to know how electromagnetic '
'waves or electronics work. The user is provided a simple
interface (buttons) that they can easily use. '''