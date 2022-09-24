from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class model(Vehicle):
    def run(self):
        print("Vikram")

    def start(self):
        print("Implementing abstract method")