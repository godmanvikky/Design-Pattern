#Sigelton Pattern
from tigger import Car

c1=Car('Maruti','Red')
c2=Car('BMW','Black')
c1.price=20000000
print(c1.__dict__)