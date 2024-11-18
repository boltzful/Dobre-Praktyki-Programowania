class LibraryCatalog:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.books = {}
        return cls._instance

    def add_book(self, book_id, title, author):
        self.books[book_id] = {"title": title, "author": author, "available": True}

    def get_book(self, book_id):
        return self.books.get(book_id)

    def mark_as_borrowed(self, book_id):
        if book_id in self.books and self.books[book_id]["available"]:
            self.books[book_id]["available"] = False
            return True
        return False

    def mark_as_returned(self, book_id):
        if book_id in self.books:
            self.books[book_id]["available"] = True

import json

class JSONAdapter:
    @staticmethod
    def parse(json_data):
        return json.loads(json_data)

class CSVAdapter:
    @staticmethod
    def parse(csv_data):
        books = {}
        for line in csv_data.strip().split("\n"):
            book_id, title, author = line.split(",")
            books[book_id] = {"title": title.strip(), "author": author.strip()}
        return books

class User:
    def __init__(self, user_id, name, role):
        self.user_id = user_id
        self.name = name
        self.role = role

    def __str__(self):
        return f"{self.name} ({self.role})"

class UserFactory:
    @staticmethod
    def create_user(user_id, name, role):
        if role.lower() in ["student", "teacher", "librarian"]:
            return User(user_id, name, role)
        raise ValueError("Invalid role")

class LibraryObserver:
    def update(self, event):
        pass

class UserObserver(LibraryObserver):
    def __init__(self, name):
        self.name = name

    def update(self, event):
        print(f"Notification for {self.name}: {event}")

class LibraryNotifier:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify(self, event):
        for observer in self._observers:
            observer.update(event)

class LibraryInterface:
    def __init__(self):
        self.catalog = LibraryCatalog()
        self.notifier = LibraryNotifier()

    def add_book(self, book_id, title, author):
        self.catalog.add_book(book_id, title, author)

    def borrow_book(self, user, book_id):
        if self.catalog.mark_as_borrowed(book_id):
            self.notifier.notify(f"{user.name} borrowed '{self.catalog.get_book(book_id)['title']}'")
            return True
        print(f"Book '{book_id}' is not available.")
        return False

    def return_book(self, user, book_id):
        self.catalog.mark_as_returned(book_id)
        self.notifier.notify(f"{user.name} returned '{self.catalog.get_book(book_id)['title']}'")
