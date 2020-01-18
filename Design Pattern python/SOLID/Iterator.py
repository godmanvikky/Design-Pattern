class UptoTen:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        val=self.num
        self.num+=1
        return val
values=UptoTen()
print(values.__next__())
print(values.__next__())
print(values.__next__())
print(values.__next__())
    