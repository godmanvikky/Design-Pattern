from math import *
from abc import ABC,abstractmethod
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class FactoryPoint:
    @staticmethod
    def new_point(x,y):
        return Point(x,y)
    @staticmethod
    def new_cartisian(a,b):
        return Point(sin(a),sin(b))
p=Point(1,2)
p1=FactoryPoint.new_point(2,3)
print(p1.__dict__)
p2=FactoryPoint.new_cartisian(2,3)
print(p2.__dict__)
class HotDrink(ABC):
    @abstractmethod
    def consume(self):
        pass
class Coffe(HotDrink):
    @property
    def consume(self):
        print("Consumed Coffed")
class Tea(HotDrink):
    def consume(self):
        print("Tea is Consumed")
class HotDrinkFactory(ABC):
    @abstractmethod
    def prepare(self,amount):
        pass
class CoffeFactory(HotDrinkFactory):
    def __init__(self,amount):
        self.amount=amount
    def prepare(self):
        print(f'Preparing Coffe using Coffe Class:-{self.amount}')
        return Coffe()
class TeaFactory(HotDrinkFactory):
    def __init__(self,amount):
        self.amount=amount
    def prepare(self):
        print(f'Preparing Tea using Tea Class:-{self.amount}')
def typeofFacory(t,amount):
    if t=="Coffe":
        return CoffeFactory(amount).prepare()
    else:
        return TeaFactory(amount).prepare()
if __name__ == "__main__":
    t=input("Enter the type of ")
    c=typeofFacory("Coffe",250)
    tea=typeofFacory("Tea",300)
    c.consume

class TV(ABC):
    def 

