
class PizzaOrder:
    def __init__(self, time):
        self.pizzas = []
        self.time = time

    def getTime(self):
        return self.time

    def setTime(self, time):
        self.time = time

    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def getOrderDescription(self):
        string = ''
        total = 0
        for i in self.pizzas:
            string += i.getPizzaDetails() + '\n' + '----' + '\n'
            total += i.getPrice()
            
        return'******\n' + 'Order Time: {}\n'.format(self.getTime()) + string + 'TOTAL ORDER PRICE: ${:.2f}\n'.format(total) + '******\n'
        
         

        