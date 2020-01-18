#LSP

class Rectangle:
    def __init__(self,width,height):
        self.__width=width
        self.__height=height
    @property
    def area(self):
        return self.__width*self.__height
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,width):
        self.__width=width
    @property 
    def height(self):
        return self.__height
    @height.setter
    def height(self,height):
        self.__height=height
class Square(Rectangle):
    def __init__(self,size):
        Rectangle.__init__(self,size,size)
    @Rectangle.width.setter
    def width(self,value):
        self.__width=self.__height=value
    @Rectangle.height.setter
    def height(self,value):
        self.__height=self.__width=value
rc=Rectangle(2,3)
sq =Square(5)
print(rc.__dict__)
print(sq.__dict__)
def use_rc(s):
    w=s.width
    s.height=10
    print(s.area)
use_rc(rc)
use_rc(sq)
