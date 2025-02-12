class Library:
    def __init__(self,bks,n_bks):
        self.bks=bks
        self.n_bks=n_bks
    def addBooks(self,bk):
        self.bks.extend(bk)
        self.n_bks += len(bk)
    def showBooks(self):
        print(self.bks)
    def numBooks(self):
        print(self.n_bks)

bks=['book1','book2','book3']
n_bks=len(bks)

l = Library(bks,n_bks)

l.showBooks()
l.numBooks()
l.addBooks(['book4','book5','book6'])
l.showBooks()
l.numBooks()
