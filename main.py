import csv

with open('REFERENCE_CSV', newline='') as f:
    tabn = ['']*100000
    i = 0
    for line in f :
        if len(line) != 0 :
            if i == 0:
                for j in range (0,len(str(line)),2):
                    ording = ord(line[j])
                    tabn[i] = tabn[i] + chr(ording)
            else :
                for j in range (1,len(str(line)),2):
                    ording = ord(line[j])
                    tabn[i] = tabn[i] + chr(ording)
            i += 1

with open('EDITED_CSV', newline='') as f:
    tabe = ['']*40000
    i = 0
    for line in f :
        if line != '' :
            if i == 0:
                for j in range (0,len(str(line)),2):
                    ording = ord(line[j])
                    tabe[i] = tabe[i] + chr(ording)
            else :
                for j in range (1,len(str(line)),2):
                    ording = ord(line[j])
                    tabe[i] = tabe[i] + chr(ording)
            i += 1

print(tabe[0:10])

i=0
j=0
while i < len(tabn) and j < len(tabe) :
    if tabn[i]!='' or tabe[j]!='':
        if tabn[i][0:8] == tabe[j][0:8]:
            i += 2
            j += 2
        else :
            print(tabe[j])
            j += 2
    else :
        if tabn[i]=='':
            i +=1
        if tabe[j]=='':
            j +=1
