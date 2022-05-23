from CustomPizza import CustomPizza
from Pizza import Pizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder
from OrderQueue import OrderQueue, QueueEmptyException


cp1 = CustomPizza("S")
cp2 = CustomPizza('M')
cp3 = CustomPizza('L')
cp4 = CustomPizza("S")
cp5 = CustomPizza('M')
cp6 = CustomPizza('L')

sp1 = SpecialtyPizza("S", "Carne-more")
sp2 = SpecialtyPizza("M", "Vegeterino")
sp3 = SpecialtyPizza("L", "Cheesy")

cp4.addTopping("extra cheese")
cp4.addTopping("sausage")

cp5.addTopping("extra cheese")
cp5.addTopping("sausage")

cp6.addTopping("extra cheese")
cp6.addTopping("sausage")

    
order0 = PizzaOrder(123000) #12:30:00PM
order0.addPizza(cp1)
order0.addPizza(cp3)
order1 = PizzaOrder(143000) #02:30:00PM
order1.addPizza(sp1)
order2 = PizzaOrder(103000) #10:30:00AM
order2.addPizza(cp2)
order3 = PizzaOrder(83000) #08:30:00AM
order3.addPizza(sp2)


    
oq = OrderQueue()
oq.addOrder(order0)
oq.addOrder(order1)
oq.addOrder(order2)
oq.addOrder(order3)
    



def test_CustomPizza1():
    assert cp1.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
Price: $8.00\n"
    assert cp2.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: M\n\
Toppings:\n\
Price: $10.00\n"
    assert cp3.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
Price: $12.00\n"

def test_CustomPizza2():
    assert cp4.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $9.00\n"
    assert cp5.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: M\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $11.50\n"
    assert cp6.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $14.00\n"

def test_SpecialtyPizza3():
    assert sp1.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n"
    assert sp2.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: M\n\
Name: Vegeterino\n\
Price: $14.00\n"
    assert sp3.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: L\n\
Name: Cheesy\n\
Price: $16.00\n"

def test_PizzaOrder4():
    assert order0.getOrderDescription() == \
"******\n\
Order Time: 123000\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
Price: $8.00\n\
\n\
----\n\
CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $20.00\n\
******\n"
    assert order1.getOrderDescription() == \
"******\n\
Order Time: 143000\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $12.00\n\
******\n"
    assert order2.getOrderDescription() == \
"******\n\
Order Time: 103000\n\
CUSTOM PIZZA\n\
Size: M\n\
Toppings:\n\
Price: $10.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $10.00\n\
******\n"
    assert order3.getOrderDescription() == \
'******\n\
Order Time: 83000\n\
SPECIALTY PIZZA\n\
Size: M\n\
Name: Vegeterino\n\
Price: $14.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $14.00\n\
******\n'

def test_OrderQueue1():
    assert oq.processNextOrder() == \
'******\n\
Order Time: 83000\n\
SPECIALTY PIZZA\n\
Size: M\n\
Name: Vegeterino\n\
Price: $14.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $14.00\n\
******\n'
    assert oq.processNextOrder() == \
'******\n\
Order Time: 103000\n\
CUSTOM PIZZA\n\
Size: M\n\
Toppings:\n\
Price: $10.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $10.00\n\
******\n'
    assert oq.processNextOrder() == \
'******\n\
Order Time: 123000\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
Price: $8.00\n\
\n\
----\n\
CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $20.00\n\
******\n'
    assert oq.processNextOrder() == \
'******\n\
Order Time: 143000\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $12.00\n\
******\n'
    



    
    
    



    
