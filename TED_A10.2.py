#TED AULA 10
#QUESTÃO 2


from operator import index


VET = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",\
     "21", "22", "13", "24", "25", "46", "27", "28", "29", "10", "31", "32", "13", "34", "35", "36", "37", "38", "39", "40", \
     "41", "42", "43", "44", "45", "46", "47", "10", "49", "50"]

#print(VET)
VETu = set(VET)
#print(VETu)
VETv=[]
for x in VETu:
    if (VET.count(x) > 1):
        VETv.append(x)
print(VETv)