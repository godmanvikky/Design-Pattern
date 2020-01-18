from enum import Enum
from abc import ABC,abstractmethod
class Relation(Enum):
    PARENT=1
    CHILD=2
    SIBLING=3
class Person:
    def __init__(self,name):
        self.name=name
class RelBrowser:
    @abstractmethod
    def find_child(self):
        pass
class RelationShips(RelBrowser):
    def __init__(self):
        self.relation=[]
    def add_parent_and_child(self,parent,child):
        self.relation.append((parent,Relation.PARENT,child))
        self.relation.append((child,Relation.CHILD,parent))
    def find_child(self,name):
       for rel in self.relation:
           if(rel[0].name==name and rel[1].PARENT==Relation.PARENT):
               yield rel[0].name
class Research:
    def __init__(self,browser):
        for p in browser.find_child("Sankar"):
            print(p)           
p=Person("Sankar")
c1=Person("Vikky")
c2=Person("Vaishnav")
rel=RelationShips()
rel.add_parent_and_child(p,c1)
rel.add_parent_and_child(p,c2)
Research(rel)
users=[
    (0,"Bob","password"),
    (1,"Rolf","bob123"),
    (2,"Jose","long4assword"),
    (3,"username",'1234')
]



