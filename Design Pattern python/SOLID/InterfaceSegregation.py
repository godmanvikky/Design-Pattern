from abc import abstractmethod,ABC
class Printer(ABC):
    @abstractmethod
    def print(self,doc):
        pass
class PrinterMachine(Printer):
    def __init__(self):
        Printer.__init__(self)
        self.__d='ddd'
    def print(self):
        print('Hello World')
p1=PrinterMachine()
print(p1.d)
