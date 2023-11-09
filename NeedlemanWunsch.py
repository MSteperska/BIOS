import numpy as np
import sys

match_value = 1
mismatch_value = -1
gap_value = -2

def match_val(val_1, val_2):
  if val_1 == val_2:
    return match_value
  else:
    return mismatch_value

# wczytywanie danych z pliku
if len(sys.argv) < 2:
  print("Missing input")
else:
  fasta_file = sys.argv[1]
  match_value = int(sys.argv[2])
  mismatch_value = int(sys.argv[3])
  gap_value = int(sys.argv[4])

file = open(fasta_file, 'r')
seq1 = ''
seq2 = ''
curr = None

for line in file:
  line = line.strip()
  if not line.startswith('>'):
    if seq1 == '':
      seq1 = line
    else:
      seq2 = line
      
print('sequence 1: ', seq1)
print('sequence 2: ', seq2)
num1 = len(seq1)
num2 = len(seq2)

# utworzenie macierzy do zastosowania algorytmu
macierz = np.zeros((num1 + 1, num2 + 1), dtype = int)
pochodzenie = np.zeros((num1 + 1, num2 + 1), dtype = str)

licznik = -1
for i in range(1, num1 + 1):
  macierz[i][0] = licznik
  licznik = licznik - 1

licznik = -1
for i in range(1, num2 + 1):
  macierz[0][i] = licznik
  licznik = licznik - 1

# uzupelnianie macierzy
for x in range(1, num1 + 1):
  for y in range(1, num2 + 1):
    score = match_val(seq1[x-1], seq2[y-1])
    wartosc = max(macierz[x-1][y-1] + score, macierz[x-1][y] + gap_value, macierz[x][y-1] + gap_value)
    macierz[x][y] = wartosc
    if wartosc == macierz[x-1][y-1] + score:
      pochodzenie[x][y] = 'd'
    elif wartosc == macierz[x-1][y] + gap_value:
      pochodzenie[x][y] = 'u'
    elif wartosc == macierz[x][y-1] + gap_value:
      pochodzenie[x][y] = 'l'

print("matrix: ")
print(macierz)
print("direction: ")
print(pochodzenie)

# znalezienie rozwiazania
align1 = ''
align2 = ''

while num1 > 0 and num2 > 0:
  current_score = macierz[num1][num2]
  diagonal_score = macierz[num1 - 1][num2 - 1]
  up_score = macierz[num1 - 1][num2]
  left_score = macierz[num1][num2 - 1]

  if pochodzenie[num1][num2] == 'd':
    align1 += seq1[num1 - 1]
    align2 += seq2[num2 - 1]
    num1 -= 1
    num2 -= 1
  elif pochodzenie[num1][num2] == 'u':
    align1 += seq1[num1 - 1]
    align2 += '-'
    num1 -= 1
  elif pochodzenie[num1][num2] == 'l':
    align1 += '-'
    align2 += seq2[num2 - 1]
    num2 -= 1

while num2 > 0:
  align2 += seq2[num2 - 1]
  align1 += '-'
  num2 -= 1
while num1 > 0:
  align1 += seq1[num1 - 1]
  align2 += '-'
  num1 -= 1

print('align 1: ', align1[::-1])
print('align 2: ', align2[::-1])

final_score = 0

for x in range(0, len(align1)):
  if (align1[x] == '-' or align2[x] == '-'):
    final_score += gap_value
  else:
    final_score += match_val(align1[x], align2[x])

print("score: ", final_score)