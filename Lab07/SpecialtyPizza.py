from Pizza import Pizza
class SpecialtyPizza(Pizza):
    def __init__(self, size, name):
        self.setSize(size)
        self.name = name
        
        if size == 'S':
            self.setPrice(12.00)
        elif size == 'M':
            self.setPrice(14.00)
        elif size == 'L':
            self.setPrice(16.00)

    def getPizzaDetails(self):
        return "SPECIALTY PIZZA\nSize: {}\nName: {}\nPrice: ${:.2f}\n".format(self.getSize(),self.name,self.getPrice())