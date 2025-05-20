import os
import csv

# Pobierz wszystkie pliki .csv w bieżącym folderze
for filename in os.listdir('.'):
    if filename.endswith('.csv'):
        # Otwórz plik i zapisz pustą zawartość (zostawi nagłówki, jeśli są potrzebne)
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            pass  # Plik zostaje wyczyszczony
print("Wyczyszczono wszystkie pliki CSV w bieżącym folderze.")