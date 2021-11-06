from abc import ABC, abstractclassmethod


class FlyBehaviour(ABC):
    """Strategy FlyBehaviour"""
    @abstractclassmethod
    def fly():
        """Method for different fly behaviour"""

class FlyWithWings(FlyBehaviour):
    def fly():
        print("Flying")

class FlyNoWay(FlyBehaviour):
    def fly():
        print("Not lifting off!!!")


class QuackBehaviour(ABC):
    """Strategy QuackBehaviour"""
    @abstractclassmethod
    def quack():
        """Method for different quack behaviour"""

class Quack(QuackBehaviour):
    def quack():
        print("Quacking like a duck!!")

class Squeak(QuackBehaviour):
    def quack():
        print("Squeking like something that squeaks")
    
class MuteQuack(QuackBehaviour):
    def quack():
        print("Silence")

    
class Duck():
    """The Duck class with different properties depending on what duck getting generated"""
    def __init__(self, quack: QuackBehaviour, fly: FlyBehaviour) -> None:
        quack = QuackBehaviour
        fly = FlyBehaviour


if __name__ == "__manin__":
    """Example of how to run the code, should probably be in a function/method in real life"""