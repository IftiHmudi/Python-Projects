from Pizza import Pizza
class CustomPizza(Pizza):
    def __init__(self, size):
        self.setSize(size)
        
        if size == 'S':
            self.setPrice(8.00)
        elif size == 'M':
            self.setPrice(10.00)
        elif size == 'L':
            self.setPrice(12.00)
        
        self.topping = []

    def addTopping(self, topping):
        if self.getSize() == 'S':
            self.setPrice(self.getPrice() + .50)
        elif self.getSize() == 'M':
            self.setPrice(self.getPrice() + .75)
        elif self.getSize() == 'L':
            self.setPrice(self.getPrice() + 1.00)
        self.topping.append(topping)

    def getPizzaDetails(self):
        td = ''
        for i in self.topping:
            td += '\t+ ' + i + '\n'
                
        return "CUSTOM PIZZA\nSize: {}\nToppings:\n{}Price: ${:.2f}\n".format(self.getSize(), td ,self.getPrice())

    
    