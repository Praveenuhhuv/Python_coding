from abc import ABC,abstractmethod

class vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class car(vehicle):
    def go(self):
        print("car go")
    def stop(self):
        print("car stop")

class bike(vehicle):
    def go(self):
        print("bike go")
    def stop(self):
        print("bike stop")