from abc import ABC,abstractmethod
class Observer(ABC):
    @abstractmethod
    def update(self,obervable,*args):
        pass
class Observable:
    def __init__(self):
        self.__observers=[]
    def add_observer(self,obs):
        self.__observers.append(obs)
    def remove_observer(self,obs):
        self.__observers.remove(obs)
    def notify_obs(self,*args):
        for obs in self.__observers:
            obs.update(self,*args)
class Employee(Observable):
    def __init__(self,name,salary):
        super().__init__()
        self._name=name
        self._salary=salary
    @property
    def name(self):
        return self._name
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self,inc):
        self._salary=self._salary+inc
        self.notify_obs(self._salary)
class PayRoll(Observer):
    def update(self,observable,sal):
        print(f'Updated salary is {sal}')
class TaxRoll(Observer):
    def update(self,obserable,sal):
        print(f'Updatad Salary in Tax {sal} {obserable.name}')


e=Employee('Vikky',1200000)
t=TaxRoll()
p=PayRoll()
e.add_observer(t)
e.add_observer(p)
e.salary=200
e.salary=2000