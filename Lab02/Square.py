from Shape2D import Shape2D
class Square(Shape2D):
    def __init__(self, color = None, side = None):
        super().__init__(color)
        self.side = side

    def getSide(self):
        return self.side

    def setSide(self, side):
        self.side = side

    def computeArea(self):
        area = (self.side) ** 2
        
        return area
        
    def computePerimeter(self):
        perimeter = self.side * 4
        return perimeter

    def getShapeProperties(self):
        return 'Shape: {}, Color: {}, Side: {}, Area: {}, Perimeter: {}'. format("SQUARE", self.color, self.side, self.computeArea(), self.computePerimeter())
        