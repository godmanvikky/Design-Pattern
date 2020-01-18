class _Car:
    def __init__(self,name,color):
        self.name=name
        self.color=color
        self.__price=''
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,value):
        self.__price=value
    def __str__(self):
        print(f'{self.name},{self.color},{self.price}')
    @property
    def no(self):
        return "No instance can be created"
_instance=None
def Car(name,color):
    global _instance
    if _instance is None:
        _instance=_Car(name,color)
    else:
        print(_instance.no)
    return _instance