class Book:
    def __init__(self, title = '', author = '', year = None):
        self.title = title
        self.author = author
        self.year = year
        

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getYear(self):
        return self.year

    def getBookDetails(self):
        return "Title: {}, Author: {}, Year: {}".format(self.getTitle(), self.getAuthor(), self.getYear())

    def __gt__(self, rhs):
        if self.getAuthor() > rhs.getAuthor():
            return True
        if (self.getAuthor() == rhs.getAuthor()) and (self.getYear() > rhs.getYear()):
            return True
        if (self.getAuthor() == rhs.getAuthor()) and (self.getYear() == rhs.getYear()) and (self.getTitle() > rhs.getTitle()):
            return True
        
        return False
        
