#Klasa Uzytkownik:
#Jest to podstawowa klasa reprezentująca użytkownika systemu. Każdy użytkownik posiada atrybuty:

#imie – przechowuje imię użytkownika.
#typ_uzytkownika – określa, do jakiej grupy należy użytkownik (np. Student, Nauczyciel). Dodatkowo klasa zawiera metodę przedstaw_sie, która wyświetla informacje o użytkowniku w czytelnej formie.
#Klasa FabrykaUzytkownikow:
#Klasa ta pełni rolę fabryki, która ułatwia tworzenie obiektów klasy Uzytkownik.

#Metoda statyczna utworz_uzytkownika(imie, typ_uzytkownika) przyjmuje dane wejściowe (imię i typ) i zwraca nową instancję klasy Uzytkownik. Dzięki temu proces tworzenia obiektów jest uporządkowany i elastyczny.
#Test działania:
#Na końcu kodu znajdują się przykłady zastosowania fabryki:

#Utworzono obiekty dla użytkowników o różnych typach: student, nauczyciel i bibliotekarz.
#Następnie wywołano metodę przedstaw_sie, która wyświetla informacje o każdym użytkowniku.

# Klasa bazowa dla użytkowników systemu bibliotecznego
class Uzytkownik:
    def __init__(self, imie, typ_uzytkownika):
        self.imie = imie
        self.typ_uzytkownika = typ_uzytkownika

    def przedstaw_sie(self):
        """Wyświetla informacje o użytkowniku."""
        print(f"Cześć! Jestem {self.imie}, a mój typ to: {self.typ_uzytkownika}")


# Klasa fabryczna do tworzenia użytkowników
class FabrykaUzytkownikow:
    @staticmethod
    def utworz_uzytkownika(imie, typ_uzytkownika):
        """Tworzy nowy obiekt użytkownika na podstawie typu."""
        return Uzytkownik(imie, typ_uzytkownika)


# Test działania fabryki
student = FabrykaUzytkownikow.utworz_uzytkownika("Anna Kowalska", "Student")
nauczyciel = FabrykaUzytkownikow.utworz_uzytkownika("Marek Nowak", "Nauczyciel")
bibliotekarz = FabrykaUzytkownikow.utworz_uzytkownika("Elżbieta Lis", "Bibliotekarz")

# Wywołanie metod obiektów
student.przedstaw_sie()
nauczyciel.przedstaw_sie()
bibliotekarz.przedstaw_sie()
