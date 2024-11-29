#1. LibraryCatalog:
#Zarządza książkami w bibliotece (dodawanie, wyszukiwanie, wypożyczanie, zwracanie).
#Każda książka jest reprezentowana jako klucz w słowniku ksiazki, z wartością True (dostępna) lub False (wypożyczona).
#2. UserManagement:
#Zarządza użytkownikami biblioteki (dodawanie użytkowników, śledzenie wypożyczonych książek).
#Każdy użytkownik ma listę wypożyczonych książek przechowywaną w słowniku uzytkownicy.
#3. LibraryInterface:
#Uproszczony interfejs łączący LibraryCatalog i UserManagement.
#Dostarcza metody umożliwiające:
#Dodawanie książek i użytkowników.
#Wypożyczanie i zwracanie książek.
#Wyszukiwanie książek w katalogu.
#Wyświetlanie książek wypożyczonych przez użytkowników.

class LibraryCatalog:
    """Klasa zarządzająca katalogiem książek w bibliotece."""
    def __init__(self):
        self.ksiazki = {}

    def dodaj_ksiazke(self, tytul):
        """Dodaje książkę do katalogu."""
        if tytul not in self.ksiazki:
            self.ksiazki[tytul] = True  # True oznacza, że książka jest dostępna
            print(f"Książka '{tytul}' została dodana do katalogu.")
        else:
            print(f"Książka '{tytul}' już znajduje się w katalogu.")

    def wypozycz_ksiazke(self, tytul):
        """Zarządza wypożyczeniem książki."""
        if self.ksiazki.get(tytul):
            self.ksiazki[tytul] = False  # False oznacza, że książka jest wypożyczona
            print(f"Książka '{tytul}' została wypożyczona.")
            return True
        elif tytul in self.ksiazki:
            print(f"Książka '{tytul}' jest już wypożyczona.")
        else:
            print(f"Książka '{tytul}' nie istnieje w katalogu.")
        return False

    def zwroc_ksiazke(self, tytul):
        """Zarządza zwrotem książki."""
        if tytul in self.ksiazki and not self.ksiazki[tytul]:
            self.ksiazki[tytul] = True  # True oznacza, że książka jest ponownie dostępna
            print(f"Książka '{tytul}' została zwrócona.")
        else:
            print(f"Nie można zwrócić książki '{tytul}'. Może nie była wypożyczona lub nie istnieje.")

    def wyszukaj_ksiazke(self, tytul):
        """Sprawdza dostępność książki."""
        if tytul in self.ksiazki:
            status = "dostępna" if self.ksiazki[tytul] else "wypożyczona"
            print(f"Książka '{tytul}' jest {status}.")
        else:
            print(f"Książka '{tytul}' nie istnieje w katalogu.")


class UserManagement:
    """Klasa zarządzająca użytkownikami biblioteki."""
    def __init__(self):
        self.uzytkownicy = {}

    def dodaj_uzytkownika(self, imie):
        """Dodaje użytkownika do systemu."""
        if imie not in self.uzytkownicy:
            self.uzytkownicy[imie] = []
            print(f"Użytkownik '{imie}' został dodany.")
        else:
            print(f"Użytkownik '{imie}' już istnieje.")

    def wypozyczona_ksiazka(self, imie, tytul):
        """Dodaje książkę do listy wypożyczonych książek użytkownika."""
        if imie in self.uzytkownicy:
            self.uzytkownicy[imie].append(tytul)
        else:
            print(f"Nie znaleziono użytkownika '{imie}'.")

    def zwrocona_ksiazka(self, imie, tytul):
        """Usuwa książkę z listy wypożyczonych książek użytkownika."""
        if imie in self.uzytkownicy and tytul in self.uzytkownicy[imie]:
            self.uzytkownicy[imie].remove(tytul)
        else:
            print(f"Użytkownik '{imie}' nie ma wypożyczonej książki '{tytul}'.")

    def pokaz_wypozyczenia(self, imie):
        """Wyświetla listę wypożyczonych książek użytkownika."""
        if imie in self.uzytkownicy:
            wypozyczenia = self.uzytkownicy[imie]
            print(f"Użytkownik '{imie}' ma wypożyczone książki: {', '.join(wypozyczenia) if wypozyczenia else 'brak'}.")
        else:
            print(f"Użytkownik '{imie}' nie istnieje.")


class LibraryInterface:
    """Fasada upraszczająca interakcję z systemem biblioteki."""
    def __init__(self):
        self.katalog = LibraryCatalog()
        self.uzytkownicy = UserManagement()

    def dodaj_ksiazke(self, tytul):
        """Dodaje książkę do katalogu."""
        self.katalog.dodaj_ksiazke(tytul)

    def dodaj_uzytkownika(self, imie):
        """Dodaje użytkownika do systemu."""
        self.uzytkownicy.dodaj_uzytkownika(imie)

    def wypozycz_ksiazke(self, imie, tytul):
        """Pozwala użytkownikowi wypożyczyć książkę."""
        if self.katalog.wypozycz_ksiazke(tytul):
            self.uzytkownicy.wypozyczona_ksiazka(imie, tytul)

    def zwroc_ksiazke(self, imie, tytul):
        """Pozwala użytkownikowi zwrócić książkę."""
        self.katalog.zwroc_ksiazke(tytul)
        self.uzytkownicy.zwrocona_ksiazka(imie, tytul)

    def wyszukaj_ksiazke(self, tytul):
        """Wyszukuje książkę w katalogu."""
        self.katalog.wyszukaj_ksiazke(tytul)

    def pokaz_wypozyczenia(self, imie):
        """Pokazuje wypożyczone książki użytkownika."""
        self.uzytkownicy.pokaz_wypozyczenia(imie)


# Test fasady
interfejs = LibraryInterface()

interfejs.dodaj_ksiazke("Harry Potter")
interfejs.dodaj_ksiazke("Władca Pierścieni")
interfejs.dodaj_uzytkownika("Jan Kowalski")
interfejs.dodaj_uzytkownika("Anna Nowak")

interfejs.wypozycz_ksiazke("Jan Kowalski", "Harry Potter")
interfejs.pokaz_wypozyczenia("Jan Kowalski")
interfejs.wyszukaj_ksiazke("Harry Potter")

interfejs.zwroc_ksiazke("Jan Kowalski", "Harry Potter")
interfejs.pokaz_wypozyczenia("Jan Kowalski")
interfejs.wyszukaj_ksiazke("Harry Potter")
