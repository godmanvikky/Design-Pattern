class Library:
    counter=0
    def __init__(self):
        self.list=[]
        self.book_dict={}
    def add_book(self,bookname,price):
        self.book_dict={
            'BookId':Library.counter,
            'Bookname':bookname,
            'BookPrice':price
        }
        self.list.append(self.book_dict)
        Library.counter=Library.counter+1
    def remove_book(self,pos):
        del self.list[pos]
    def list_books(self):
        return self.list
class BookSave:
    def __init__(self,filename):
        self.filename=filename
    def loadFile(self,file):
        self.filename=open(file,'w')
    def readFile(self):
        for  f1 in self.filename.readlines():
            print(f'{f1}\n')
    def writeFile(self,file,value):
        self.loadFile(file)
        self.filename.write(str(value))
        self.filename.close()
# l1=Library()
# l1.price=500
# l1.add_book("Donkey",300)
# l1.add_book("Monkey",700)
# print(l1.list_books())
# fi=open('vikky.txt','r')
# f1=BookSave(fi)
# f1.readFile()
# f1.writeFile('vikky.txt',"vikky how are you")
# f1.readFile()
from enum import Enum
from abc import ABC,abstractmethod
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class PointFactory:
    @staticmethod
    def new_cartisian(x,y):
        return Point(x*2,y*2)
    @staticmethod
    def new_thrice(x,y):
        return Point(x*3,x*3)
p=PointFactory.new_cartisian(2,3)
print(p.__dict__)     
class Bird(ABC):
    @abstractmethod
    def fly(self):
        print("Fly")
class Duck(Bird):
    def quack(self):
        print("Speak Quack")
    def fly(self):
        print("Fly Long Distance")
class Hen(Bird):
    def Koko(self):
        print("Ko Ko")
    def fly(self):
        print("Fly short Distance")
class HenAdapter:
    def __init__(self,adapte:Hen):
        self.adapte=adapte
    def quack(self):
        self.adapte.Koko()
    def fly(self):
        print("Flying for short")
hen=Hen()
h=HenAdapter(hen)
h.quack()
import functools
def func(a,b):
    return a+b

import threading

print('Current Executing Thread',threading.current_thread().getName())