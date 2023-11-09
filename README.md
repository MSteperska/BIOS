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

## Przykładowy wynik działania programu:

Przy wykonaniu komendy:

```
python NeedlemanWunsch.py file.fasta 1 -1 -1
```

i zawartości pliku:

```
> seq1
MVLSEGEWQLVLHVWAKVEA
> seq2
MNIFEMLRIDEGLRLKIYKD
```

program wygeneruje następujące dane:

```
sequence 1: MVLSEGEWQLVLHVWAKVEA
sequence 2: MNIFEMLRIDEGLRLKIYKD
matrix:
[[  0  -1  -2  -3  -4  -5  -6  -7  -8  -9 -10 -11 -12 -13 -14 -15 -16 -17
  -18 -19 -20]
 [ -1   1   0  -1  -2  -3  -4  -5  -6  -7  -8  -9 -10 -11 -12 -13 -14 -15
  -16 -17 -18]
 [ -2   0   0  -1  -2  -3  -4  -5  -6  -7  -8  -9 -10 -11 -12 -13 -14 -15
  -16 -17 -18]
 [ -3  -1  -1  -1  -2  -3  -4  -3  -4  -5  -6  -7  -8  -9 -10 -11 -12 -13
  -14 -15 -16]
 [ -4  -2  -2  -2  -2  -3  -4  -4  -4  -5  -6  -7  -8  -9 -10 -11 -12 -13
  -14 -15 -16]
 [ -5  -3  -3  -3  -3  -1  -2  -3  -4  -5  -6  -5  -6  -7  -8  -9 -10 -11
  -12 -13 -14]
 [ -6  -4  -4  -4  -4  -2  -2  -3  -4  -5  -6  -6  -4  -5  -6  -7  -8  -9
  -10 -11 -12]
 [ -7  -5  -5  -5  -5  -3  -3  -3  -4  -5  -6  -5  -5  -5  -6  -7  -8  -9
  -10 -11 -12]
 [ -8  -6  -6  -6  -6  -4  -4  -4  -4  -5  -6  -6  -6  -6  -6  -7  -8  -9
  -10 -11 -12]
 [ -9  -7  -7  -7  -7  -5  -5  -5  -5  -5  -6  -7  -7  -7  -7  -7  -8  -9
  -10 -11 -12]
 [-10  -8  -8  -8  -8  -6  -6  -4  -5  -6  -6  -7  -8  -6  -7  -6  -7  -8
   -9 -10 -11]
 [-11  -9  -9  -9  -9  -7  -7  -5  -5  -6  -7  -7  -8  -7  -7  -7  -7  -8
   -9 -10 -11]
 [-12 -10 -10 -10 -10  -8  -8  -6  -6  -6  -7  -8  -8  -7  -8  -6  -7  -8
   -9 -10 -11]
 [-13 -11 -11 -11 -11  -9  -9  -7  -7  -7  -7  -8  -9  -8  -8  -7  -7  -8
   -9 -10 -11]
 [-14 -12 -12 -12 -12 -10 -10  -8  -8  -8  -8  -8  -9  -9  -9  -8  -8  -8
   -9 -10 -11]
 [-15 -13 -13 -13 -13 -11 -11  -9  -9  -9  -9  -9  -9 -10 -10  -9  -9  -9
   -9 -10 -11]
 [-16 -14 -14 -14 -14 -12 -12 -10 -10 -10 -10 -10 -10 -10 -11 -10 -10 -10
  -10 -10 -11]
 [-17 -15 -15 -15 -15 -13 -13 -11 -11 -11 -11 -11 -11 -11 -11 -11  -9 -10
  -11  -9 -10]
 [-18 -16 -16 -16 -16 -14 -14 -12 -12 -12 -12 -12 -12 -12 -12 -12 -10 -10
  -11 -10 -10]
 [-19 -17 -17 -17 -17 -15 -15 -13 -13 -13 -13 -11 -12 -13 -13 -13 -11 -11
  -11 -11 -11]
 [-20 -18 -18 -18 -18 -16 -16 -14 -14 -14 -14 -12 -12 -13 -14 -14 -12 -12
  -12 -12 -12]]
direction:
[['' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '']
 ['' 'd' 'l' 'l' 'l' 'l' 'd' 'l' 'l' 'l' 'l' 'l' 'l' 'l' 'l' 'l' 'l' 'l'
  'l' 'l' 'l']
 ['' 'u' 'd' 'd' 'd' 'd' 'd' 'd' 'd' 'd' 'd' 'd' 'd' 'd' 'd' 'd' 'd' 'd'
  'd' 'd' 'd']
 ['' 'u' 'd' 'd' 'd' 'd' 'd' 'd' 'l' 'l' 'l' 'l' 'l' 'd' 'l' 'd' 'l' 'l'
  'l' 'l' 'l']
 ['' 'u' 'd' 'd' 'd' 'd' 'd' 'u' 'd' 'd' 'd' 'd' 'd' 'd' 'd' 'd' 'd' 'd'
  'd' 'd' 'd']
 ['' 'u' 'd' 'd' 'd' 'd' 'l' 'l' 'l' 'd' 'd' 'd' 'l' 'l' 'l' 'l' 'l' 'l'
  'l' 'l' 'l']
 ['' 'u' 'd' 'd' 'd' 'u' 'd' 'd' 'd' 'd' 'd' 'u' 'd' 'l' 'l' 'l' 'l' 'l'
  'l' 'l' 'l']
 ['' 'u' 'd' 'd' 'd' 'd' 'd' 'd' 'd' 'd' 'd' 'd' 'u' 'd' 'd' 'd' 'd' 'd'
  'd' 'd' 'd']
 ['' 'u' 'd' 'd' 'd' 'u' 'd' 'd' 'd' 'd' 'd' 'u' 'd' 'd' 'd' 'd' 'd' 'd'
  'd' 'd' 'd']
 ['' 'u' 'd' 'd' 'd' 'u' 'd' 'd' 'd' 'd' 'd' 'd' 'd' 'd' 'd' 'd' 'd' 'd'
  'd' 'd' 'd']
 ['' 'u' 'd' 'd' 'd' 'u' 'd' 'd' 'l' 'd' 'd' 'd' 'd' 'd' 'l' 'd' 'l' 'l'
  'l' 'l' 'l']
 ['' 'u' 'd' 'd' 'd' 'u' 'd' 'u' 'd' 'd' 'd' 'd' 'd' 'u' 'd' 'u' 'd' 'd'
  'd' 'd' 'd']
 ['' 'u' 'd' 'd' 'd' 'u' 'd' 'd' 'd' 'd' 'd' 'd' 'd' 'd' 'd' 'd' 'l' 'd'
  'd' 'd' 'd']
 ['' 'u' 'd' 'd' 'd' 'u' 'd' 'u' 'd' 'd' 'd' 'd' 'd' 'u' 'd' 'u' 'd' 'd'
  'd' 'd' 'd']
 ['' 'u' 'd' 'd' 'd' 'u' 'd' 'u' 'd' 'd' 'd' 'd' 'd' 'u' 'd' 'u' 'd' 'd'
  'd' 'd' 'd']
 ['' 'u' 'd' 'd' 'd' 'u' 'd' 'u' 'd' 'd' 'd' 'd' 'd' 'd' 'd' 'u' 'd' 'd'
  'd' 'd' 'd']
 ['' 'u' 'd' 'd' 'd' 'u' 'd' 'u' 'd' 'd' 'd' 'd' 'd' 'd' 'd' 'u' 'd' 'd'
  'd' 'd' 'd']
 ['' 'u' 'd' 'd' 'd' 'u' 'd' 'u' 'd' 'd' 'd' 'd' 'd' 'd' 'd' 'u' 'd' 'l'
  'd' 'd' 'l']
 ['' 'u' 'd' 'd' 'd' 'u' 'd' 'u' 'd' 'd' 'd' 'd' 'd' 'd' 'd' 'd' 'u' 'd'
  'd' 'u' 'd']
 ['' 'u' 'd' 'd' 'd' 'd' 'd' 'u' 'd' 'd' 'd' 'd' 'l' 'd' 'd' 'd' 'u' 'd'
  'd' 'u' 'd']
 ['' 'u' 'd' 'd' 'd' 'u' 'd' 'u' 'd' 'd' 'd' 'u' 'd' 'd' 'd' 'd' 'u' 'd'
  'd' 'd' 'd']]
align 1: M----VLSEGEWQLVLHVWAKVEA
align 2: MNIFEMLRIDE-GLRL-KIYK--D
score:  -12
```
