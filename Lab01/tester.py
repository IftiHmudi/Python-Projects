
from Animal import Animal
from AnimalShelter import AnimalShelter

ruffles = Animal("dOg", 12.2, 2, "Ruffles")
jack = Animal("dog", 12.2, 2, "Jack")
ryan = Animal("cAt", 12.2, 2, "Ryan")
habib = Animal("CAt", 12.2, 2, "Habib")
andrew = Animal("horse", 12.2, 2, "Andrew")
zack = Animal("hOrse", 12.2, 2, "Zack")

shelter = AnimalShelter()
shelter.addAnimal(ruffles)
shelter.addAnimal(jack)
shelter.addAnimal(ryan)
shelter.addAnimal(habib)
shelter.addAnimal(andrew)
shelter.addAnimal(zack)
print(shelter.getAnimalsBySpecies('DOG'))
