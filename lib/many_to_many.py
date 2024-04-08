class Author:
    all = []
    def __init__(self, name):
        self.name = name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        temp = []
        for contract in Contract.all:
            temp.append(contract.book)
        return temp

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])


class Book:
    all = []
    def __init__(self, title):
        self.title = title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        temp = []
        for contract in Contract.all:
            temp.append(contract.author)
        return temp

class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):       
        if not isinstance(value, Author):
            raise Exception
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):       
        if not isinstance(value, Book):
            raise Exception
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):       
        if not isinstance(value, str):
            raise Exception
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):       
        if not isinstance(value, int):
            raise Exception
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        temp = []
        for contract in Contract.all:
            if contract.date == date:
                temp.append(contract)
        return temp

# Accidentally sorted all dates       
#        temp_dates = []
#        sorted_dates = []
#        for contract in Contract.all:
#            temp_dates.append(contract.date)
#        temp_dates.sort()
#        for date in temp_dates:
#            for contract in Contract.all:
#                if contract.date == date:
#                    sorted_dates.append(contract)
#        return sorted_dates