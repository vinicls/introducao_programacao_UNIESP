#TED AULA 11
#QUESTÃO 1

linha,coluna = (10,10)
from random import randint

matriz1 = []

for l in range(linha):
    lin = []
    for c in range(coluna):
        lin.append(randint(1,100))
    matriz1.append(lin)

print(matriz1)

soma = 0
for l in range(linha):
    for c in range(coluna):
        soma +=matriz1[l][c]
print("A soma de todos os vetores da matriz é {}".format(soma)) 
