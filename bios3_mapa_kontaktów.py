# wczytanie bibliotek

from Bio.PDB import PDBList, PDBParser
import numpy as np
import matplotlib.pyplot as plt

# pobranie struktury w formacie pdb

pdb_list = PDBList()
parser = PDBParser()

pdb_id = '2HHB'
pdb_file_path = pdb_list.retrieve_pdb_file(pdb_id, file_format = 'pdb')
structure = parser.get_structure(pdb_id, pdb_file_path)

# przechodzenie przez modele, łańcuchy, reszty i atomy w strukturze

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

#chyba wychodzi odwrotnie, sprawdzic przy wpisywaniu wartości do macierzy -> gdy przedostatnia linijka jest zakomentowana - działa (ale dlaczego?)

