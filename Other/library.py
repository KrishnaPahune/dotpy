class Library:
    def __init__(self):
        self.bks=[]
        self.n_bks=0
    def addBooks(self,bk):
        self.bks.extend(bk)
    def showBooks(self):
        for book in self.bks:
            print(book)
    def numBooks(self):
        print(len(self.bks))

l = Library()
l.addBooks(['book4','book5','book6'])
l.showBooks()
l.numBooks()
