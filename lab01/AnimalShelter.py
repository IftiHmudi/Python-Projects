class AnimalShelter:
    def __init__(self):
        self.shelter = {}

    def addAnimal(self, animal):
        if self.shelter.get(animal.species) == None:
            self.shelter[animal.species] = [animal]
        elif not animal in self.shelter.get(animal.species):
            self.shelter[animal.species].append(animal)

    def removeAnimal(self, animal): 
        if animal.species in self.shelter:
            this_list = self.shelter[animal.species]
            for value in this_list:
                if value == animal:
                    self.shelter[animal.species].remove(animal)
                    return True
        return False

    def removeSpecies(self, species):
        species = species.upper()
        if species in self.shelter:
            self.shelter.pop(species)      


    
    def getAnimalsBySpecies(self, species):
        new_string = ''
        count = 0
        if species:
            species = species.upper()
            if species in self.shelter:
                for animal in self.shelter[species]:
                    if count == len(self.shelter[species]) - 1:    
                        new_string += animal.toString()
                    else:
                        new_string += animal.toString() + '\n'
                    count += 1
        return new_string        
                
                

    def doesAnimalExist(self, animal):
        if animal.species in self.shelter:
            this_list = self.shelter[animal.species]
            for value in this_list:
                if value == animal:
                    return True
        return False























            
