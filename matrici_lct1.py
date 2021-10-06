matrice=[[34,17,4,89,3],
  [11,26,49,54,9],
  [8,44,37,21,35],
  [20,42,19,73,10],
  [56,47,36,1,17]]

s=[]
for i in range(len(matrice)):
    s.append(sum(matrice[i]))
print("Suma elementelor de pe fiecare linie:",s)

suma=[]
coloana=[]
for j in range(len(matrice[0])):
    for i in matrice:
        coloana.append(i[j])
    suma.append(sum(coloana))
print("Suma elementelor de pe fiecare coloana:",suma)

diagonala_principala=[]
for i in range(len(matrice)):
    for j in range(len(matrice[0])) :
        if i==j :
            diagonala_principala.append(matrice[i][j])
print("Diagonala principala:",diagonala_principala)

diagonala_secundara=[] 
for i in range(len(matrice)):
    for j in range(len(matrice[0])) :
        n=5
        if i+j==n-1:
            diagonala_secundara.append(matrice[i][j])
print("Diagonala secundara:",diagonala_secundara) 
