class Book:
    def __init__ (self, book_id: str, title: str, author: str, is_borrowed: bool = False) -> None:
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def borrow(self) -> bool:
        if self.is_borrowed:
            return False
        self.is_borrowed = True
        return True

    def return_book(self) -> bool:
        if not self.is_borrowed:
            return False
        self.is_borrowed = False
        return True

class Member:
    def __init__ (self, member_id: str, name: str, borrowed_books: list[Book] | None = None) -> None:
        self.member_id = member_id
        self.name = name
        self.borrowed_books = borrowed_books or []

    def borrow_book(self, book: Book) -> bool:
        if book.borrow():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book: Book) -> bool:
        if book in self.borrowed_books and book.return_book():
            self.borrowed_books.remove(book)
            return True
        return False

class Library:
    def __init__ (self) -> None:
        self.books: dict[str, Book] = {}
        self.members: dict[str, Member] = {}

    def add_book(self, book_id: str, title: str, author: str) -> None:
        if book_id not in self.books:
            self.books[book_id] = Book(book_id, title, author, False)

    def register_member(self, member_id: str, name: str) -> None:
        if member_id not in self.members:
            self.members[member_id] = Member(member_id, name, [])

    def borrow_book(self, member_id: str, book_id: str) -> bool:
        if member_id not in self.members:
            raise ValueError(f"Member not found")
        if book_id not in self.books:

            raise ValueError(f"Book not found")
        member = self.members[member_id]
        book = self.books[book_id]
        if member.borrow_book(book):
            return True
        raise ValueError(f"Book is already borrowed")

    def return_book(self, member_id: str, book_id: str) -> bool:
        if member_id not in self.members:
            raise ValueError(f"Member not found")
        if book_id not in self.books:
            raise ValueError(f"Book not found")
        member = self.members[member_id]
        book = self.books[book_id]
        if book not in member.borrowed_books:
            raise ValueError(f"Book not borrowed by this member")
        if member.return_book(book):
            return True

    def get_borrowed_books(self, member_id: str) -> list[str] | None:
        if member_id in self.members:
            member = self.members[member_id]
            return [book.title for book in member.borrowed_books]
        return None

if __name__ == "__main__":
    library = Library()