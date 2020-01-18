from abc import ABC,abstractmethod
class Observer(ABC):
    def update(self,*args):
        pass
class Observable:
    def __init__(self):
        self.list_observer=[]
    def add_observer(self,obs):
        self.list_observer.append(obs)
    def removeuser(self,obs):
        self.list_observer.remove(obs)
    def notify_obs(self,salary,*args):
        for observer in self.list_observer:
                observer.update(salary,*args)
class Employee(Observable):
    def __init__(self,name,salary):
        super().__init__()
        self.name=name
        self.__salary=salary
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,value):
        self.__salary=value
        self.notify_obs(self.__salary,self.name)
    def __str__(self):
        return self.name +':-'+ str(self.salary)
class PayRoll(Observer):
    def update(self,salary,name):
        print(f'{name}:-{salary} PayRoll Updataded')
class TaxRoll(Observer):
    def update(self,salary,name):
        print(f'{name} has salary as {salary}')
e=Employee('Vikky',2000)
print(e)
p=PayRoll()
t=TaxRoll()
e.add_observer(p)
e.add_observer(t)
e.salary=200000
class HardDrink(ABC):
    @abstractmethod
    def consume(self):
        pass

class Coffe(HardDrink):
    def __init__(self,name):
        self.name=name
    def consume(self):
        print("Consuming Coffe")  

class Tea(HardDrink):
    def __init__(self,name):
        self.name=name
    def consume(self):
        print("Consuming Tea")  

class HardDrinkFactory:
    def 
    