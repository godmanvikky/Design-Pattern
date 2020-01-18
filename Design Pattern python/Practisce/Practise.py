#OCP
#Open for extension and closed for modification
from enum import Enum
class Color(Enum):
    GREEN=1
    RED=2
    YELLOW=3
    BLUE=4
    VIOLET=5
class Size(Enum):
    LARGE=1
    SMALL=2
    MEDIUM=3
class Product:
    def __init__(self,color,size):
        self.__name=''
        self.color=color
        self.size=size
    @property
    def name(self):
        self.__name=''
    @name.setter
    def name(self,value):
        self.__name=value
class Specification:
    def is_satisified(self,item):
        pass
class Filter:
    def filter(self,spec,items):
        pass

class ColorSpecification(Specification):
    def __init__(self,color):
        self.color=color
    def is_satisified(self,item):
        return self.color==item.color
class SizeSpecification(Specification):
    def __init__(self,size):
        self.size=size
    def is_satisified(self,item):
        return self.size==item.size
class BaseFilter:
    def filter(self,spec,items):
        for item in items:
            if(spec.is_satisified(item)):
                yield item
class AndSpecfication(Specification):
    def __init__(self,*args):
        self.args=args
    def is_satisified(self,items):
        return all(list(
            map(lambda specs: specs.is_satisified(items),self.args)
        )
        )
p1=Product(Color.GREEN,Size.LARGE)
p1.name="Tree"
p2=Product(Color.YELLOW,Size.SMALL)
p2.name="Crayons"
p3=Product(Color.BLUE,Size.LARGE)
p3.name="Sky"
p4=Product(Color.RED,Size.MEDIUM)
p4.name="Dairy"
l=[p1,p2,p3,p4]
bf=BaseFilter()
for k in bf.filter(AndSpecfication(ColorSpecification(Color.BLUE),SizeSpecification(Size.LARGE)),l):
    print(k.__dict__)
for p in bf.filter(ColorSpecification(Color.GREEN),l):
    print(p.__dict__)
def count_word_occurrences(localfile):
    content = open(localfile, "r").readlines()
    print(content)
from bs4 import BeautifulSoup
from urllib.request import urlopen

def get_text_from_url(url):
    '''Extract html as string from given url'''
    page = urlopen(url).read()
    soup = BeautifulSoup(page)
    text = soup.get_text()
    return text
print(get_text_from_url("https://dev.to/annalara/solid-programming-part-2-open-closed-principle-3ddj"))
count_word_occurrences('../vikky.txt')