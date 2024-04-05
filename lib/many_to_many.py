class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def get_name(self):
        return self._name
    def set_name(self, value):
        if type(value) is str:
            self._name = value
        else:
            raise ValueError("This is not a string")
    name = property(get_name, set_name)

    def contracts(self):
        declaration = []
        for contract in Contract.all:
            if contract.author is self:
                declaration.append(contract)
        return declaration
    
    def books(self):
        return [book.book for book in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])

class Book:

    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def get_title(self):
        return self._title
    def set_title(self, value):
        if type(value) is str:
            self._title = value
        else:
            raise ValueError("This is not a string")
    title = property(get_title, set_title)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book is self]

    def authors(self):
        return [author.author for author in self.contracts()]

class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    def get_author(self):
        return self._author
    def set_author(self, value):
        if type(value) is Author:
            self._author = value
        else:
            raise ValueError("Incorrect Author")
    author = property(get_author,set_author)

    def get_book(self):
        return self._book
    def set_book(self, value):
        if type(value) is Book:
            self._book = value
        else:
            raise ValueError("Incorrect Book")
    book = property(get_book,set_book)

    def get_date(self):
        return self._date
    def set_date(self, value):
        if type(value) is str:
            self._date = value
        else:
            raise ValueError("Incorrect Date")
    date = property(get_date,set_date)

    def get_royalties(self):
        return self._royalties
    def set_royalties(self, value):
        if type(value) is int:
            self._royalties = value
        else:
            raise ValueError("Incorrect Royalties")
    royalties = property(get_royalties,set_royalties)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date is date]

    