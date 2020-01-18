import time
from abc import ABC,abstractmethod
def wrap_func(func):
    def wrap():
        print(time.ctime(time.time()))
        func()
        print(time.ctime(time.time()))
    return wrap
@wrap_func
def func():
    print("Function is here")

func()

class Shape(ABC):
    def __str__(self):
        return ''
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def resize(self,fact):
        self.radius=self.resize*fact
    def __str__(self):
        return f'A circle of radius {self.radius}'
class Square(Shape):
    def __init__(self,width):
        self.width=width
    def resize(self,fact):
        self.width=self.width*fact
    def __str__(self):
        return f'A circle of radius {self.width}'
class ColoredShape:
    def __init__(self,shape,color):
        self.shape=shape
        self.color=color
    def __str__(self):
        return f'{self.shape} and color of {self.color}'
c=Circle(2)
print(c)
colored=ColoredShape(c,"red")
print(colored)

class FileLogger:
    def __init__(self,file):
        self.file=file
    def writelines(self,string):
        self.file.writelines(string)
        print(f'wrote {len(string)} to file')
    def __getattr__(self,item):
        print(self.__dict__)
        return getattr(self.__dict__['file'],item)   
fil=open('Vikky.txt','w')
f=FileLogger(fil)
f.writelines(['Hello'])
f.write('Vikky1234')