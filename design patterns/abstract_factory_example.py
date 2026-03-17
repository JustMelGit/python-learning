from abc import ABC, abstractmethod

# Abstract Factory
class PetFactory(ABC):
    @abstractmethod
    def get_pet(self):
        pass

    @abstractmethod
    def get_food(self):
        pass

# Concrete Products
class Dog:
    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"

class Cat:
    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"

# Concrete Factories
class DogFactory(PetFactory):
    def get_pet(self):
        return Dog()

    def get_food(self):
        return "Dog Food"

class CatFactory(PetFactory):
    def get_pet(self):
        return Cat()

    def get_food(self):
        return "Cat Food"

# Client
class PetStore:
    def __init__(self, factory: PetFactory):
        self.factory = factory

    def get_pet_info(self):
        pet = self.factory.get_pet()
        return {
            "type": str(pet),
            "sound": pet.speak(),
            "food": self.factory.get_food()
        }
