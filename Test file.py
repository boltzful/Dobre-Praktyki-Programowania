if __name__ == "__main__":
    # Singleton
    catalog = LibraryCatalog()
    catalog.add_book("001", "Python Programming", "John Doe")
    catalog.add_book("002", "Data Structures", "Jane Smith")
    
    # Adapter
    json_data = '{"003": {"title": "Machine Learning", "author": "Andrew Ng"}}'
    csv_data = "004, Deep Learning, Ian Goodfellow\n005, Artificial Intelligence, Stuart Russell"
    catalog.books.update(JSONAdapter.parse(json_data))
    catalog.books.update(CSVAdapter.parse(csv_data))
    
    # Factory
    user1 = UserFactory.create_user("U001", "Alice", "Student")
    user2 = UserFactory.create_user("U002", "Bob", "Teacher")
    
    # Observer
    notifier = LibraryNotifier()
    observer1 = UserObserver(user1.name)
    observer2 = UserObserver(user2.name)
    notifier.add_observer(observer1)
    notifier.add_observer(observer2)
    
    # Facade
    library = LibraryInterface()
    library.add_book("006", "Introduction to Algorithms", "Thomas H. Cormen")
    library.borrow_book(user1, "001")
    library.return_book(user1, "001")
