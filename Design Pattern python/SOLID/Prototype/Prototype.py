from copy import deepcopy
class Address:
    def __init__(self,address):
        self.address=address
    def __str__(self):
        return self.address
class Person:
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def __str__(self):
        return f'{self.name} is in address {self.address}'
class EmployeeFactory:
    main_office=Person('','2nd Floor Kanak Residency')
    back_office=Person('','3rd Floor Vikky')
    @staticmethod
    def new_Employe(proto,name):
        result=deepcopy(proto)
        result.name=name
        return result

