class Shape2D:
    def __init__(self = None, color = None):
        self.color = color

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def getShapeProperties(self):
        return 'Shape: {}, Color: {}'.format('N/A', self.color)