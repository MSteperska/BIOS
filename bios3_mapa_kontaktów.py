# wczytanie bibliotek

from Bio.PDB import PDBList, PDBParser
import numpy as np
import matplotlib.pyplot as plt

# pobranie struktury białka w formacie pdb

pdb_list = PDBList()
parser = PDBParser()

pdb_id = '2HHB'
pdb_file_path = pdb_list.retrieve_pdb_file(pdb_id, file_format = 'pdb')
structure = parser.get_structure(pdb_id, pdb_file_path)

# przechodzenie przez modele, łańcuchy, reszty i atomy w strukturze
"""
alpha_carbons = []
x = 1

for model in structure:
    for chain in model:
        for residue in chain:
          for atom in residue:
            if atom.get_id() == 'CA':
                  try:
                    alpha_carbons.append(residue['CA'].get_coord())
                  except KeyError:
                    continue

contact_map = np.zeros((len(alpha_carbons), len(alpha_carbons)), dtype = int)
cutoff_distance = 8.0

for i in range (len(alpha_carbons)):
  for j in range (i + 1, len(alpha_carbons)):
    distance = np.linalg.norm(alpha_carbons[i] - alpha_carbons[j])
    if distance < cutoff_distance:
      contact_map[i, j] = 1
      contact_map[j, i] = 1

#print(alpha_carbons)
#print(contact_map[10:][:10])

# rozdzielenie wartości 1 i 0 do dwóch struktur, generowanie wykresu

contact_true = []
contact_false = []

for i in range (contact_map.shape[0]):
  for j in range (contact_map.shape[1]):
    if contact_map[i,j] == 1:
      contact_true.append((i, j))
    else:
      contact_false.append((i, j))

xt, yt = zip(*contact_true)
xf, yf = zip(*contact_false)


plt.figure()
plt.scatter(xt, yt, color = 'blue', label = 'contact')
#plt.scatter(xf, yf, color = 'pink', label = 'no contact')

plt.show()
"""
# UWAGA DO KODU - chyba wychodzi odwrotnie, sprawdzic przy wpisywaniu wartości do macierzy -> gdy przedostatnia linijka jest zakomentowana - działa (ale dlaczego?)

# pobranie struktury rna w formacie pdb

pdb_id = '2HHB'
pdb_file_path = pdb_list.retrieve_pdb_file(pdb_id, file_format = 'pdb')
structure = parser.get_structure(pdb_id, pdb_file_path)

# liczenie kątów torsyjnych (kod poprawny tylko jeśli założenie O5' to piąty zapisany tlen w reszcie również jest poprawne)

atomO = []
atomC = []
atomN = []
atomP = []
matrix = []

for res in structure.get_residues():
  atomO.append([])
  atomC.append([])
  atomN.append([])
  atomP.append([])
  matrix.append([])
  for atom in res:
    if atom == "O":
      atomO.append(atom.get_vector())
    if atom == "C":
      atomC.append(atom.get_vector())
    if atom == "N":
      atomN.append(atom.get_vector())
    if atom == "P":
      atomP.append(atom.get_vector())

rn = 0
for res in structure.get_residues():
  if len(atomO[rn]) > 4 and len(atomC[rn]) > 4 and len(atomP[rn]) > 0:
    if rn > 0 and len(atomO[rn - 1]) > 2:
      matrix.append(calc_dihedral(atomO[rn - 1][2], atomP[rn][0], atomO[rn][4], atomC[rn][4]))
    else:
      matrix.append(0)
    matrix.append(calc_dihedral(atomP[rn][0], atomO[rn][4], atomC[rn][4], atomC[rn][3]))
    matrix.append(calc_dihedral(atomO[rn][4], atomC[rn][4], atomC[rn][3], atomC[rn][2]))
    matrix.append(calc_dihedral(atomC[rn][4], atomC[rn][3], atomC[rn][2], atomO[rn][2]))
    if rn < len(matrix) - 2 and len(atomO[rn + 1]) > 4 and len(atomP[rn + 1]) > 0:
      matrix.append(calc_dihedral(atomC[rn][3], atomC[rn][2], atomO[rn][2], atomP[rn + 1][0]))
      matrix.append(calc_dihedral(atomC[rn][2], atomO[rn][2], atomP[rn + 1][0], atomO[rn + 1][4]))
    else:
      matrix.append(0)
      matrix.append(0)
    if len(atomN[rn]) > 8:
      matrix.append(calc_dihedral(atomO[rn][3], atomC[rn][0], atomN[rn][8], atomC[rn][3]))
    elif len(atomN[rn]) > 0:
      matrix.append(calc_dihedral(atomO[rn][3], atomC[rn][0], atomN[rn][0], atomC[rn][1]))
    else:
      matrix.append(0)
  #final incrementation
  rn = rn + 1
  
  # zapis do pliku
  
file = open("output_matrix.txt", "w")
for i in range(0, len(matrix) - 1):
  for j in range(0, len(matrix[i]) - 1):
    file.write(str(matrix[i][j]))
    if j + 1 == len(matrix[i]):
      file.write("\n")
    else:
      file.write(" - ")
file.close()