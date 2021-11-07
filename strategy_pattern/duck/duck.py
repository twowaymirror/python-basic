from abc import ABC, abstractclassmethod


class FlyBehaviour(ABC):
    """Strategy FlyBehaviour"""
    @abstractclassmethod
    def fly(self):
        """Method for different fly behaviour"""

class FlyWithWings(FlyBehaviour):
    def fly(self):
        return "Flying"

class FlyNoWay(FlyBehaviour):
    def fly(self):
        return "Not lifting off!!!"


class QuackBehaviour(ABC):
    """Strategy QuackBehaviour"""
    @abstractclassmethod
    def quack(self):
        """Method for different quack behaviour"""

class Quack(QuackBehaviour):
    def quack(self):
        return "Quacking like a duck!!"

class Squeak(QuackBehaviour):
    def quack(self):
        return "Squeking like something that squeaks"
    
class MuteQuack(QuackBehaviour):
    def quack(self):
        return "Silence"


class Duck():
    """ The Duck class is the Conctext
        Generating different behaviour depending on strategy.
        The Duck class is unaware of what behaviour that will be used, decoupling the Duck from
        its behaviour.

    """
    def __init__(self, quack: QuackBehaviour, fly: FlyBehaviour) -> None:        
        self.quack = quack
        self.fly = fly

    def swim(self):
        print("Swimming")

    def performFly(self):
        print(self.quack.quack())

    def performQuack(self):
        print(self.fly.fly())


class MallardDuck(Duck):
    """Create Mallard Duck"""
    def __init__(self):
        super().__init__(Quack(), FlyNoWay())


if __name__ == "__main__":
    """ 
    Client
    Example of how to run the code, should probably be in a function/method in real life
    """
    mallard = Duck(Squeak(), FlyNoWay())
    mallard.performQuack()
    mallard.performFly()
    mallard.swim()

    mallard2 = MallardDuck()
    mallard2.performFly()
    mallard2.performQuack()
