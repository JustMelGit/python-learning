class Dog:
	"""One of the objects to be returned"""

	def speak(self):
		return "woof"

	def __str__(self):
		return "Dog"

class DogFactory:
	"""Concrete Factory"""

	def get_pet(self):
		"""Returns a Dog object"""
		return Dog()


	def get_food(self):
		"""Returns a Dog food object"""
		return "Dog Food"

class PetStore:
	""" PetStore houses our Abstract Factory"""

	def __init__(self,pet_factory=None):
		""" Pet factory is our abstract factory """
		self._pet_factory = pet_factory

	def show_pet(self):
		""" Utility method to display the details of the objects return"""
		pet = self._pet_factory.get_pet()
		pet_food = self._pet_factory.get_food()

		print("Our pet is '{}!'".format(pet))
		print("Our pet says hello by '{}'".format(pet.speak()))
		print("Its food is '{}'".format(pet_food))


#create a concrete factory
factory = DogFactory()

#creat a pet store housing our abstract factory
shop = PetStore(factory)

#Invoke the utility method to show the details our pet
shop.show_pet()