#1. Klasa LibraryCatalogIterator:
#Służy do iteracji po liście książek.
#Przechowuje referencję do listy książek oraz aktualny indeks elementu.
#Implementuje metody:
#__iter__: Zwraca referencję na samego siebie.
#__next__: Zwraca kolejny element (tytuł książki). Jeśli nie ma już elementów, podnosi wyjątek StopIteration.
#2. Klasa UserManagementIterator:
#Odpowiada za iterację po liście użytkowników.
#Działa analogicznie do LibraryCatalogIterator, ale przechowuje listę użytkowników.
#3. Klasa LibraryCatalog:
#Zarządza listą książek w bibliotece.
#Metoda dodaj_ksiazke umożliwia dodawanie tytułów.
#Implementuje metodę __iter__, która zwraca iterator (LibraryCatalogIterator) dla listy książek.
#4. Klasa UserManagement:
#Zarządza listą użytkowników biblioteki.
#Metoda dodaj_uzytkownika dodaje użytkownika do systemu.
#Metoda __iter__ zwraca iterator (UserManagementIterator) dla listy użytkowników.



class LibraryCatalogIterator:
    """Iterator do przeglądania listy książek w katalogu biblioteki."""
    def __init__(self, ksiazki):
        """Inicjalizuje iterator z kolekcją książek."""
        self.ksiazki = ksiazki
        self.indeks = 0

    def __iter__(self):
        """Zwraca iterator (self)."""
        return self

    def __next__(self):
        """Zwraca kolejną książkę lub podnosi wyjątek StopIteration, gdy lista się skończy."""
        if self.indeks < len(self.ksiazki):
            tytul = self.ksiazki[self.indeks]
            self.indeks += 1
            return tytul
        else:
            raise StopIteration


class UserManagementIterator:
    """Iterator do przeglądania listy zarejestrowanych użytkowników."""
    def __init__(self, uzytkownicy):
        """Inicjalizuje iterator z listą użytkowników."""
        self.uzytkownicy = uzytkownicy
        self.indeks = 0

    def __iter__(self):
        """Zwraca iterator (self)."""
        return self

    def __next__(self):
        """Zwraca kolejnego użytkownika lub podnosi wyjątek StopIteration."""
        if self.indeks < len(self.uzytkownicy):
            uzytkownik = self.uzytkownicy[self.indeks]
            self.indeks += 1
            return uzytkownik
        else:
            raise StopIteration


class LibraryCatalog:
    """Klasa reprezentująca katalog biblioteki."""
    def __init__(self):
        """Inicjalizuje pustą listę książek."""
        self.ksiazki = []

    def dodaj_ksiazke(self, tytul):
        """Dodaje książkę do katalogu."""
        self.ksiazki.append(tytul)

    def __iter__(self):
        """Zwraca iterator dla listy książek."""
        return LibraryCatalogIterator(self.ksiazki)


class UserManagement:
    """Klasa reprezentująca zarządzanie użytkownikami biblioteki."""
    def __init__(self):
        """Inicjalizuje pustą listę użytkowników."""
        self.uzytkownicy = []

    def dodaj_uzytkownika(self, imie):
        """Dodaje użytkownika do listy zarejestrowanych osób."""
        self.uzytkownicy.append(imie)

    def __iter__(self):
        """Zwraca iterator dla listy użytkowników."""
        return UserManagementIterator(self.uzytkownicy)


# Test systemu z iteratorem
katalog = LibraryCatalog()
katalog.dodaj_ksiazke("Harry Potter")
katalog.dodaj_ksiazke("Władca Pierścieni")
katalog.dodaj_ksiazke("Hobbit")

print("Lista książek w katalogu:")
for ksiazka in katalog:
    print(f"- {ksiazka}")

zarzadzanie_uzytkownikami = UserManagement()
zarzadzanie_uzytkownikami.dodaj_uzytkownika("Anna Kowalska")
zarzadzanie_uzytkownikami.dodaj_uzytkownika("Piotr Nowak")
zarzadzanie_uzytkownikami.dodaj_uzytkownika("Maria Wiśniewska")

print("\nLista użytkowników biblioteki:")
for uzytkownik in zarzadzanie_uzytkownikami:
    print(f"- {uzytkownik}")
