from abc import abstractmethod,ABC
class TV(ABC):
    @abstractmethod
    def on(self):
        pass
    def off(self):
        pass
class Sony(TV):
    def __init__(self,remote):
        self.remote=remote
    def on(self):
        print("Sony Tv is on")
        self.remote.on()

    def off(self):
        self.remote.off()
        print("Sony Tv is off")
class Lg(TV):
    def __init__(self,remote):
        self.remote=remote
    def on(self):
        print("Lg Tv is on")
        self.remote.on()
    def off(self):
        self.remote.off()
        print("Sony Tv is off")
class Remote(ABC):
    @abstractmethod
    def on(self):
        pass
    def off(self):
        pass
class OldRemote(Remote):
    def on(self):
        print("On with old Remote")
    def off(self):
        print("Off with old Remote")
class newRemote(Remote):
    def on(self):
        print("On with new Remote")
    def off(self):
        print("Off with new Remote")
o=OldRemote()
n=newRemote()
Lgold=Lg(o)
SonyNew=Sony(n)
Lgnew=Lg(n)
SonyOld=Sony(o)
Lgold.on()
Lgnew.on()
SonyNew.on()
SonyNew.on()