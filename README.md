# BIOS

## Instrukcja obsługi programu:

Program należy uruchamiać w trybie wsadowym, tj. z użyciem lini poleceń. Program przyjmuje cztery argumenty: ścieżkę do pliku .fasta, punktację za dopasowanie, niedopasowanie oraz przerwę, niepodanie ich skutkować będzie komunikatem o błędzie, natomiast wszelkie nadmiarowe argumenty zostaną odrzucone. Podany plik fasta powinien zawierać jedynie te dwie sekwencje, które mają zostać porównane. Punkty za niedopasowanie i przerwę powinny być ujemne, zgodnie z logiką działania algorytmu.

## Interpretacja wyników działania programu:

Program podaje następujące dane wynikowe:

```
sequence 1: <pierwsza sekwencja z pliku .fasta>
sequence 2: <druga sekwencja z pliku .fasta>
matrix: <macierz punktowa działania algorytmu Needlemana-Wunscha>
direction: <macierz zawierająca informację o przechodzeniu powyższej macierzy celem uzyskania wyniku>
align 1: <dopasowanie pierwszej sekwencji z pliku .fasta>
align 2: <dopasowanie drugiej sekwencji z pliku .fasta>
score: <wynik punktowy dopasowania>
```
