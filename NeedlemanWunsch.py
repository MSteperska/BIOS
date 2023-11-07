import numpy as np #biblioteka do macierzy
import sys

#seq1 = 'CCGAACGA'
#seq2 = 'CAAGAC'

'''
#wczytywanie danych z pliku
if len(sys.argv) < 2:
  print("Nie podano pliku wejœciowego.")
else:
  fasta_file = sys.argv[1]

with open(fasta_file, 'r') as file:
  seq1 = ''
  seq2 = ''
  curr = None

  for line in file:
    line = line.strip()

    if line.startwith('>'):
      if curr is None:
        curr = seq1
      else:
        curr = seq2
      curr = ''
    else:
      curr += line

print('sequence 1: ', seq1)
print('sequence 2: ', seq2)
'''

#seq1 = 'CCGAACGACGTACGAAGCTG'
#seq2 = 'CAAGACTGCATGCATGACTC'
#type(seq1)   output:  str

seq1 = 'MVLSEGEWQLVLHVWAKVEA'
seq2 = 'MNIFEMLRIDEGLRLKIYKD'

#ustalenie d³ugoœci sekwencji
num1 = len(seq1)
num2 = len(seq2)
#print(num1, num2)

#ustalenie wartoœci score
match_value = 1
mismatch_value = -1
gap_value = -2


#utworzenie macierzy z samymi zerami
macierz = np.zeros((num1 + 1, num2 + 1), dtype = int)
#macierz, z informacjami sk¹d pochodzi dana wartoœæ w macierzy
pochodzenie = np.zeros((num1 + 1, num2 + 1), dtype = str)

#uzupe³nienie pierwszego wiersza i pierwszej kolumny macierzy
licznik = -1
for i in range(1, num1 + 1):
  macierz[i][0] = licznik
  licznik = licznik - 1


licznik = -1
for i in range(1, num2 + 1):
  macierz[0][i] = licznik
  licznik = licznik - 1

#funkcja okreœlaj¹ca wartoœæ dla score (match/mismatch po przek¹tnej)
def match_val(val_1, val_2):
  if val_1 == val_2:
    return match_value
  else:
    return mismatch_value

#uzupe³nianie macierzy
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

print(macierz)
print("pochodzenie")
print(pochodzenie)


#Znalezienie rozwi¹zania
align1 = ''
align2 = ''

while num1 > 0 and num2 > 0:
  current_score = macierz[num1][num2]
  #print('i', i, 'j', j,  macierz[i][j], '<-current score')
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
'''
#do poprawy bo i, j siê myl¹ i wszytsko siê pierdzieli :)
while i > 0 and j > 0:

  current_score = macierz[i][j]
  print('i', i, 'j', j,  macierz[i][j], '<-current score')
  diagonal_score = macierz[i-1][j-1]
  up_score = macierz[i-1][j]
  left_score = macierz[i][j-1]

  if(current_score == diagonal_score + match_val(seq1[i-1], seq2[j-1])):
    print(current_score, diagonal_score + match_val(seq1[i-1], seq2[j-1]), "czy wartoœci siê zgadzaj¹")
    print("idziemy po przek¹tnej")
    print(seq1[i-1], "Seq1", seq2[y-1], "seq2")
    align1 = align1 + seq1[j-1]
    align2 = align2 + seq2[i-1]
    print('align1, diag', align1)
    print('align2, diag', align2)
    j = j - 1
    i = i - 1
  elif current_score == up_score - 1:
    print(current_score, up_score -1, "czy wartoœci siê zgadzj¹")
    print("idziemy do góry")
    print(seq1[i-1], "Seq1", seq2[y-1], "seq2")
    align1 = align1 + seq1[j-1]
    align2 = align2 + '-'
    j = j - 1
    print('align1, up', align1)
    print('align2, up', align2)
  elif current_score == left_score - 1:
    print(current_score, left_score - 1, "czy wartoœci siê zgadzaj¹")
    print("idziemy w lewo")
    print(seq1[i-1], "Seq1", seq2[y-1], "seq2")
    align1 = align1 + '-'
    align2 = align2 + seq2[i-1]
    i = i - 1
    print('align1, left', align1)
    print('align2, left', align2)

while j > 0:
  align1 += seq1[j-1]
  align2 += '-'
  j -= 1
while i > 0:
  align1 += '-'
  align2 += seq2[i-1]
  i -= 1
'''
print('align2', align2[::-1])
print('align1', align1[::-1])

final_score = 0

for x in range(0, len(align1)):
  if (align1[x] == '-' or align2[x] == '-'):
    final_score += gap_value
  else:
    final_score += match_val(align1[x], align2[x])
  '''if align1[x] == align2[x]:
    final_score += 1
  else:
    final_score -= 1'''

print("score: ", final_score)