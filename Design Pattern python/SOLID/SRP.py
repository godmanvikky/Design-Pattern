class Journal:
    def __init__(self):
        self.enteries=[]
        self.count=0
    def add_entry(self,text):
        self.count=self.count+1
        self.enteries.append(f'{self.count}:-{text}')
    def remove_entry(self,pos):
        del self.enteries[pos]
        return pos
    def __str__(self):
        return '\n'.join(self.enteries)
    

class PresistanceManager:
    @staticmethod
    def save(filename,objJournal):
        file=open(filename,'w')
        file.write(str(objJournal.__dict__))
        file.close()
    @staticmethod
    def load(filename):
        file=open(filename,'r')
        print(file.readlines())
        file.close()

j=Journal()
p=PresistanceManager()
j.add_entry('Hello World')
j.add_entry("Hello Vikky")
j.add_entry("Hello Vaishnav")
j.add_entry("Hello Doggy")
j.remove_entry(0)

PresistanceManager.save('vikky.txt',j)
PresistanceManager.load('vikky.txt')
print(j)
