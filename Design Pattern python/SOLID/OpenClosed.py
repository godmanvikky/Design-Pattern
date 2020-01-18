from enum import Enum
class Color(Enum):
    RED=1
    GREEN=2
    BLUE=3
class Size(Enum):
    SMALL=1
    MEDIUM=2
    LARGE=3
class Product:
    def __init__(self,name,color,size):
        self.name=name
        self.color=color
        self.size=size
class ProductFilter:
    def filter_by_color(self,product,color):
        for p in product:
            if p.color==color:
                yield p
    def filter_by_size(self,product,size):
        for p in product:
            if p.size==size:
                yield p
# p3=Product("Karthik",Color.BLUE,Size.SMALL)
# p1=Product('Vikky',Color.RED,Size.MEDIUM)
# p2=Product("Vaish",Color.GREEN,Size.LARGE)

# p=[p3,p1,p2]
# f=ProductFilter() 
# print(next(f.filter_by_color(p,Color.BLUE)).__dict__)

#BetterFilter
#Specification
class ColorT(Enum):
    GREEN=1
    BLUE=2
    RED=3
class SizeT(Enum):
    SMALL=1
    MEDIUM=2
    LARGE=3

class ProductCart:
    def __init__(self,name,color,size):
        self.name=name
        self.color=color
        self.size=size
class Specification:
    def is_satisfied(self,item):
        pass
    def __and__(self,other):
        return AndSpecification(self,other)
class Filter:
    def filter(self,spec,items):
        pass
class ColorSpecification(Specification):
    def __init__(self,color):
        self.color=color
    def is_satisfied(self,item):
        return self.color==item.color
class SizeSpecification(Specification):
    def __init__(self,size):
        self.size=size
    def is_satisfied(self,item):
        return self.size==item.size
class AndSpecification(Specification):
    def __init__(self,*args):
        self.args=args
    def is_satisfied(self,items):
        return all(
            list(map(
                lambda spec: spec.is_satisfied(items),self.args
            )
        ))
class OrSpecification(Specification):
    def __init__(self,*args):
        self.args=args
    def is_satisfied(self,item):
        return any(
            list(
                map(
                    lambda specs: specs.is_satisfied(item),self.args
                )
            )
        )
class AdvanceFilter(Filter):
    def filter(self,spec,items):
        for item in items:
            if spec.is_satisfied(item):
                yield item
c1=ProductCart("Trees",ColorT.GREEN,SizeT.LARGE)
c2=ProductCart("Plant",ColorT.GREEN,SizeT.SMALL)
c3=ProductCart("Signal",ColorT.RED,SizeT.LARGE)
c4=ProductCart("Sky",ColorT.BLUE,SizeT.SMALL)
c=[c1,c2,c3]
ad=AdvanceFilter()
# for p in ad.filter(ColorSpecification(ColorT.GREEN),c):
#     print(f'{p.name}:-{p.color}')
for p in ad.filter(AndSpecification(ColorSpecification(ColorT.GREEN),SizeSpecification(SizeT.LARGE)),c):
    print(f'{p.name}:-{p.color}')
for p in ad.filter(OrSpecification(ColorSpecification(ColorT.GREEN),SizeSpecification(SizeT.LARGE)),c):
     print(f'{p.name}:-{p.color}')
large_green= ColorSpecification(ColorT.GREEN) & SizeSpecification(SizeT.LARGE)
for p in ad.filter(large_green,c):
    print(f'{p.name}:-{p.color}')