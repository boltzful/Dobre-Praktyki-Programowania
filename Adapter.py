#"System biblioteczny często wymaga importowania danych o książkach z różnych źródeł, 
# takich jak pliki CSV czy JSON, które mogą mieć różne formaty. 
# Aby ujednolicić proces przetwarzania danych i zapewnić ich zgodność z wewnętrznym systemem katalogowym, 
# zastosowano wzorzec projektowy Adapter. 
# Klasa CSVAdapter została stworzona specjalnie do odczytu danych z plików CSV i ich konwersji na standardowy format – listę tytułów książek. 
# Dzięki temu możliwe jest efektywne zarządzanie danymi z różnych źródeł, niezależnie od ich pierwotnego formatu.
#Adapter pozwala systemowi na elastyczność w integracji nowych źródeł danych bez konieczności modyfikowania istniejącego kodu. 
# W implementacji zadbano również o obsługę potencjalnych błędów, takich jak brak pliku czy problemy z kodowaniem, 
# co czyni rozwiązanie bardziej niezawodnym i przyjaznym w praktycznym zastosowaniu."

import csv

# Klasa adaptera umożliwia przekształcenie danych z pliku CSV na listę książek.
class CSVAdapter:
    def __init__(self, sciezka_pliku_csv):
        self.sciezka_pliku_csv = sciezka_pliku_csv

    def pobierz_ksiazki(self):
        """Metoda wczytująca dane z pliku CSV i zwracająca listę tytułów książek."""
        lista_ksiazek = []
        try:
            with open(self.sciezka_pliku_csv, newline='', encoding='utf-8') as plik_csv:
                csv_reader = csv.reader(plik_csv)
                for wiersz in csv_reader:
                    if wiersz:  # Pomijanie pustych wierszy
                        lista_ksiazek.append(wiersz[0])  
        except FileNotFoundError:
            print(f"Nie znaleziono pliku: {self.sciezka_pliku_csv}")
        except Exception as e:
            print(f"Wystąpił błąd podczas wczytywania pliku: {e}")
        return lista_ksiazek


# Tworzenie przykładowego pliku CSV do testów
with open("C:/Users/Public/Desktop/przykladowe_ksiazki.csv", "w", encoding="utf-8") as plik_testowy:
    plik_testowy.write("Harry Potter\nWładca Pierścieni")

# Test działania adaptera
adapter = CSVAdapter("C:/Users/Public/Desktop/przykladowe_ksiazki.csv")
ksiazki_z_csv = adapter.pobierz_ksiazki()
print("Wczytane tytuły książek:", ksiazki_z_csv)
