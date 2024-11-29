#1. Klasa Biblioteka (Podmiot):
#Pole subskrybenci: Lista użytkowników, którzy zapisali się na powiadomienia o nowych książkach.
#Pole dostepne_ksiazki: Lista książek dostępnych w bibliotece.
#Metoda dodaj_subskrybenta: Dodaje użytkownika (obserwatora) do listy subskrybenci.
#Metoda powiadom_subskrybentow: Iteruje przez wszystkich subskrybentów i wysyła im powiadomienie o dostępności nowej książki.
#Metoda dodaj_ksiazke: Dodaje książkę do katalogu i automatycznie powiadamia subskrybentów o jej dostępności.
#2. Klasa Czytelnik (Obserwator):
#Pole imie: Przechowuje imię użytkownika.
#Metoda odbierz_powiadomienie: Wyświetla powiadomienie o dostępności nowej książki.
#3. Test działania systemu:
#Tworzy obiekt Biblioteka oraz dwóch użytkowników: czytelnik1 i czytelnik2.
#Dodaje użytkowników do listy subskrybentów za pomocą metody dodaj_subskrybenta.
#Po dodaniu książki "Władca Pierścieni" do biblioteki, obie osoby automatycznie otrzymują powiadomienie o jej dostępności.


class Biblioteka:
    def __init__(self):
        """Tworzy listę obserwatorów oraz listę książek dostępnych w bibliotece."""
        self.subskrybenci = []  # Lista użytkowników zapisanych na powiadomienia
        self.dostepne_ksiazki = []  # Lista książek w bibliotece

    def dodaj_subskrybenta(self, uzytkownik):
        """Dodaje użytkownika do listy subskrybentów."""
        self.subskrybenci.append(uzytkownik)

    def powiadom_subskrybentow(self, tytul_ksiazki):
        """Wysyła powiadomienie do wszystkich subskrybentów o nowej książce."""
        for subskrybent in self.subskrybenci:
            subskrybent.odbierz_powiadomienie(tytul_ksiazki)

    def dodaj_ksiazke(self, tytul_ksiazki):
        """Dodaje książkę do listy dostępnych pozycji i powiadamia subskrybentów."""
        self.dostepne_ksiazki.append(tytul_ksiazki)
        print(f"Książka '{tytul_ksiazki}' została dodana do biblioteki.")
        self.powiadom_subskrybentow(tytul_ksiazki)


class Czytelnik:
    def __init__(self, imie):
        """Inicjalizuje obiekt użytkownika z przypisanym imieniem."""
        self.imie = imie

    def odbierz_powiadomienie(self, tytul_ksiazki):
        """Wyświetla powiadomienie o dostępności nowej książki."""
        print(f"{self.imie}, książka '{tytul_ksiazki}' jest teraz dostępna w bibliotece.")


# Test systemu powiadomień
biblioteka = Biblioteka()
czytelnik1 = Czytelnik("Anna Kowalska")
czytelnik2 = Czytelnik("Piotr Nowak")

# Dodanie subskrybentów do systemu
biblioteka.dodaj_subskrybenta(czytelnik1)
biblioteka.dodaj_subskrybenta(czytelnik2)

# Dodanie książki i automatyczne powiadomienie subskrybentów
biblioteka.dodaj_ksiazke("Władca Pierścieni")
