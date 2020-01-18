#Single Responsibility Principle
class BookShelf:
    def __init__(self):
        self.rowname=[]
    def addBookstorow(self,books):
        self.rowname.append(books)
    def __str__(self):
        return f'{self.rowname}'
class Books:
    def __init__(self):
        self.add_toshelf=[]
        self.__row_name=''
    @property
    def row_name(self):
        return self.__row_name
    @row_name.setter
    def row_name(self,value):
        self.__row_name=value
    def add_entry(self,bookname):
        self.add_toshelf.append(bookname)
    def remove_entry(self,pos):
        temp=self.add_toshelf[pos]
        del self.add_toshelf[pos]
        return temp
b1=Books()
b1.row_name="A1"
b1.add_entry("Harry Porter")
b1.add_entry("The Monk who sold is Ferrari")
b2=Books()
b2.row_name="A2"
b2.add_entry("Dog as a Cow")
print(b1.__dict__)
bs=BookShelf()
bs.addBookstorow(b1)
for i in bs.rowname:
    print('\n'.join(i.add_toshelf))

#Liskov Substitution Principle
class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def setWidth(self,val):
        self.width=val
    @property
    def area(self):
        return self.width *self.height
class Square(Shape):
    def __init__(self,size):
        self.width=size
        self.height=size
    def setWidth(self,val):
        self.width=val
        self.height=val
    @property
    def area(self):
        return self.width*self.height
def increasseWidth(obj):
   obj.setWidth(obj.width+1) 
r=Rectangle(2,3)
s=Square(4)
increasseWidth(r)
print(r.area)
increasseWidth(s)
print(s.area)


class _Tigger:
    def __init__(self,name):
        self.name='vikky'
        self.age=20
    def __str__(self):
        return f'{self.name}:-{self.age}'
__instance=None
def Tigger(name):
    global __instance
    if __instance is None:
        __instance=_Tigger(name)
    return __instance
a=Tigger('vikky')
b=Tigger('vaish')
print(id(a))
print(id(b))


     