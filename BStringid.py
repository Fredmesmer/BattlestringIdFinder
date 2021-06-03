import csv
import time
from tkmain import window
from fnvhash import fnv1a_32

def hash(stringId) :
    result = 0xFFFFFFFF
    for  i in range (0,len(stringId)):
        result = ord(stringId[i]) + 33 * result
    out= str(hex(result))
    return out[len(out)-8:len(out)]

def bruteforce(hexa):
    c = hexa.lower()
    i = 0
    a = 0
    a = str(hash(str(i)))
    while c != a :
        i += 1
        a = str(hash(str(i)))
    return str(i)



start = time.time()

with open('stringsid.csv', newline='') as f:
    tabn = ['']*40000
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

with open('customnames.csv', newline='') as f:
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


index = 0

i=0
j=0
with open('output.txt','w') as output :
    while i < len(tabn) and j < len(tabe) :
        if tabn[i]!='' or tabe[j]!='':
            if tabn[i][0:8] == tabe[j][0:8]:
                i += 2
                j += 2
            else :
                print(str(tabe[j]))
                print('=>'+ bruteforce(tabe[j][0:8]))
                char = str(tabe[j]) + ' => ' + bruteforce(tabe[j][0:8])+'\n' + '\n'
                output.write(char)
                index += 1
                j += 2
        else :
            if tabn[i]=='':
                i +=1
            if tabe[j]=='':
                j +=1
    output.write('found {} matches.'.format(index))
    print('found {} matches in {}s.'.format(index,(time.time()-start)))
    window.change('found {} matches in {}s.'.format(index,(time.time()-start)))
