from Shape2D import Shape2D
class Circle(Shape2D):
    def __init__(self, color = None, radius = None):
        super().__init__(color)
        self.radius = radius

    def getRadius(self):
        return self.radius

    def setRadius(self, radius):
        self.radius = radius

    def computeArea(self):
        pi = 3.14159
        area = ((self.radius) ** 2)* pi
        return area
    
    def computePerimeter(self):
        pi = 3.14159
        perimeter = 2*(pi)*(self.radius)
        return perimeter

    def getShapeProperties(self):
        area = self.computeArea()
        perimeter = self.computePerimeter()
        return 'Shape: {}, Color: {}, Radius: {}, Area: {}, Perimeter: {}'. format("CIRCLE", self.color, self.radius, area, perimeter)
        