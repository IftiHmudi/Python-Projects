class Animal:
    def __init__(self, species = None, weight = None, age = None, name = None):
        if species:
            self.species = species.upper()
        else:
            self.species = species
        self.weight = weight
        self.age = age
        if name:
            self.name = name.upper()
        else:
            self.name = name
        
    def setSpecies(self, species):
        self.species = species.upper()

    def setWeight(self, weight):
        self.weight = weight

    def setAge(self, age):
        self.age = age

    def setName(self, name):
        self.name = name.upper()

    def toString(self):
        spec = ''
        nam = ''
        ag = ''
        weigh = ''
        if self.species:
            spec = self.species
        if self.name:
            nam = self.name
        if self.age:
            ag = self.age
        if self.weight:
            weigh = self.weight
        return 'Species: {}, Name: {}, Age: {}, Weight: {}'.format(spec, nam, ag, weigh)
