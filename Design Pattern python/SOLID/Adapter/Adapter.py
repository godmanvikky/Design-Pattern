from abc import ABC,abstractmethod
class AverageCalculator(ABC):
        def average(self):
            try:
                num_items=0
                total_sum=0
                while self.has_next():
                    total_sum+=self.next_item()
                    num_items+=1
                if num_items==0:
                    raise RuntimeError("Can't compute the sum as the file has zero contents")
            finally:
                    self.dispose()
            return total_sum
        @abstractmethod
        def has_next(self):
            pass
        @abstractmethod
        def next_item(self):
            pass
        @abstractmethod
        def dispose(self):
            pass
class FileAverageCalculator(AverageCalculator):
    def __init__(self,fileName):
        self.fileName=fileName
        self.last_line=float(self.fileName.readline())
    def has_next(self):
        return self.last_line!=''
    def next_item(self):
        result=float(self.last_line)
        self.last_line=self.fileName.readline()
        return result
    def dispose(self):
        self.fileName.close()
class GeneratorAdapter:
    def __init__(self,adaptee):
        self.adaptee=adaptee
    def readline(self):
        try:
            return next(self.adaptee)
        except StopIteration:
            return ''
    def close(self):
        pass
from random import randint
g=(randint(1,100) for i in range(1000))
gen=GeneratorAdapter(g)
fac=FileAverageCalculator(gen)
print(fac.average())

class Duck:
    def quack(self):
        print('Quack')
    def fly(self):
        print("Im flying")
class Turkey:
    def gobble(self):
        print("Gobble gobble")
    def fly(self):
        print("Flying for shor distance")
class TurkeyAdapter:
    def __init__(self,adapte):
        self.adapte=adapte
    def fly(self):
        self.adapte.fly()
    def quack(self):
        self.adapte.gobble()
t=Turkey()
ta=TurkeyAdapter(t)
ta.fly()
ta.quack()

