#Prywatne pole _instancja:

#Jest to statyczne pole klasy, które przechowuje referencję do jedynej instancji KatalogBiblioteki.
#Na początku ma wartość None, a pierwsze wywołanie klasy inicjalizuje tę zmienną.
#Metoda __new__:

#Kontroluje tworzenie obiektu klasy.
#Jeżeli KatalogBiblioteki nie ma jeszcze instancji, metoda tworzy nowy obiekt, inicjalizuje pole lista_ksiazek (pusta lista na przechowywanie książek) i zapisuje go w _instancja.
#Każde kolejne wywołanie zwraca istniejącą instancję, co zapewnia, że w programie zawsze będzie istniała tylko jedna kopia obiektu.
#Metoda dodaj_ksiazke:

#Służy do dodawania nowego tytułu książki do listy lista_ksiazek.
#Wyświetla komunikat informujący, że książka została dodana do katalogu.
#Metoda pokaz_ksiazki:

#Wyświetla wszystkie książki znajdujące się w katalogu.
#Jeżeli katalog jest pusty, informuje użytkownika, że brak w nim książek.
#Test działania singletona:

#Tworzone są dwie zmienne (katalog_a i katalog_b), które odwołują się do klasy KatalogBiblioteki.
#Po dodaniu książek przez katalog_a, są one widoczne również w katalog_b, co potwierdza, że obie zmienne wskazują na tę samą instancję obiektu.
#Weryfikacja tożsamości instancji odbywa się za pomocą operatora is oraz porównania identyfikatorów obiektów za pomocą id.


class KatalogBiblioteki:
    _instancja = None  # Statyczne pole przechowujące jedyną instancję klasy

    def __new__(cls, *args, **kwargs):
        """Zapewnia, że w programie istnieje tylko jedna instancja klasy."""
        if cls._instancja is None:
            cls._instancja = super().__new__(cls)
            cls._instancja.lista_ksiazek = []  # Inicjalizacja listy książek
        return cls._instancja

    def dodaj_ksiazke(self, tytul_ksiazki):
        """Dodaje nowy tytuł do katalogu."""
        self.lista_ksiazek.append(tytul_ksiazki)
        print(f"Książka '{tytul_ksiazki}' została dodana do katalogu.")

    def pokaz_ksiazki(self):
        """Wyświetla wszystkie książki znajdujące się w katalogu."""
        if self.lista_ksiazek:
            print("Aktualne książki w katalogu:")
            for tytul in self.lista_ksiazek:
                print(f"- {tytul}")
        else:
            print("Katalog jest pusty.")


# Test działania klasy singleton
katalog_a = KatalogBiblioteki()
katalog_a.dodaj_ksiazke("Zbrodnia i kara")
katalog_a.dodaj_ksiazke("W pustyni i w puszczy")

katalog_b = KatalogBiblioteki()
katalog_b.pokaz_ksiazki()

# Sprawdzenie, czy katalog_a i katalog_b to ta sama instancja
print("Czy katalog_a i katalog_b to ta sama instancja?", katalog_a is katalog_b)
if id(katalog_a) == id(katalog_b):
    print("Tak, obie zmienne wskazują na tę samą instancję.")
else:
    print("Nie, zmienne wskazują na różne instancje.")
