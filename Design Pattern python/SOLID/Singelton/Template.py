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
class ListAverageCalculator(AverageCalculator):
    def __init__(self,l):
        self.list=l
        self.i=0
    def has_next(self):
        return self.list[self.i]!=len(self.list)
    def next_item(self):
        result=self.list[self.i]
        print(result)
        self.i=self.i+1
        return result
    def dispose(self):
        del self.list

fac =FileAverageCalculator(open('data.txt'))
li=ListAverageCalculator([1,2,3,4,5])
print(li.average())
print(fac.average())

t=(i for i in range(0,10))
for i in range(0,10):
    print(next(t[i]))