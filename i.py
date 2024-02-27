
class GeneralUse():
    def searchByTitle(self, title: str):
        print("Search for books - Title: " + title)
    
    def searchByAuthor(self, author: str):
        print("Search for books - Title: " + author)

    def searchByTitle(self, genre: str):
        print("Search for books - Title: " + genre)
    
class CanBorrow():
    def rentBook(self, title: str):
        print("Rented book " + title)
    
    def returnBook(self, title: str):
        print("Returned book " + title)

class Admin():
    def addBook(self, title: str, author: str, genre: str):
        print("Added " + title + " by " + author + " to catalog")
    
    def removeBook(self, title: str):
        print("Removed " + title + " from catalog")
    
    def getOverdue(self):
        print("Overdue books list")

    def getBorrowed(self):
        print("Currently loaned books")

class GuestUser(GeneralUse):
    pass

class RegisteredUser(GeneralUse, CanBorrow):
    pass

class LibrarianUser(GeneralUse, CanBorrow, Admin):
    pass

def main():
    g = GuestUser()
    r = RegisteredUser()
    l = LibrarianUser()

    g.searchByTitle("To Kill a Mockingbird")
    r.searchByTitle("Hunger Games")
    l.searchByAuthor("Marissa Meyer")

    #g.rentBook("Lord of the Flies")
    r.rentBook("Of Mice and Men")
    l.returnBook("The Scarlet Letter")

    #g.getOverdue()
    #r.getBorrowed()
    l.addBook("Lord of the Rings", "JRR Tolkien", "Fantasy")

main()
