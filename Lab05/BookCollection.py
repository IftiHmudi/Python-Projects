from BookCollectionNode import BookCollectionNode
class BookCollection:
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None

    def insertBook(self, book):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.getData() > book:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = BookCollectionNode(book)

        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def getAllBooksInCollection(self):
        current = self.head
        output = ''
        while current != None:
            output += current.getData().getBookDetails() + "\n"
            current = current.getNext()
        return output

    def getNumberOfBooks(self):
        temp = self.head
        count = 0 
        while temp != None:
            count += 1
            temp = temp.getNext()
        return count

    def getBooksByAuthor(self, author):
        author = author.upper()
        output = ''
        current = self.head
        while current != None:
            if current.getData().getAuthor().upper() == author:
                output += current.getData().getBookDetails() + "\n"
                current = current.getNext()
            else:
                current = current.getNext()
                continue
        return output

    def recursiveSearchTitle(self, title, bookNode):
        if bookNode == None:
            return False
                
        if bookNode.getData().getTitle().upper() == title.upper():
            return True
        else:
            bookNode = bookNode.getNext()
            return self.recursiveSearchTitle(title, bookNode)

    def removeAuthor(self, author):
        current = self.head

        if current == None:
            return

        previous = None
        found = False
        while not found:
            if current == None:
                return
            if current.getData().getAuthor().upper() == author.upper():
                while (current != None and current.getData().getAuthor().upper() == author.upper()):
                    current = current.getNext()
                found = True
            else:
                previous = current
                current = current.getNext()

        if found == True and previous == None:
            self.head = current

        if found == True and previous != None:
            previous.setNext(current)
                    
                        