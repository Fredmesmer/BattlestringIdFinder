import csv
import time
from tkinter import*
from tkinter import filedialog
import encodings

class window :
    def __init__(self,geometry,title):
        self.core = Tk()
        self.core.geometry(geometry)
        self.core.title(title)

        self.file1 = StringVar(self.core)
        self.file2 = StringVar(self.core)
        self.file3 = StringVar(self.core)
        self.text = StringVar(self.core)
        self.idd = StringVar(self.core)
        self.var = StringVar(self.core)
        self.text.set('idle')

        self.entitle1 = Label(self.core,text='Reference csv file path').place(x=10,y=5)
        self.filepath1 = Entry(self.core, textvariable=self.file1,width=50).place(x= 10,y=30)
        self.pick1 = Button(self.core,text='select file 1',command=pickone).place(x = 320 , y = 25)

        self.entitle2 = Label(self.core,text='Edited csv file path').place(x=10,y=50)
        self.filepath2 = Entry(self.core, textvariable=self.file2,width=50).place(x=10,y=75)
        self.pick2 = Button(self.core,text='select file 2',command=picktwo).place(x = 320 , y = 70)

        self.entitle3 = Label(self.core,text='output directory').place(x=10,y=95)
        self.filepath3 = Entry(self.core, textvariable=self.file3,width=50).place(x=10,y=120)
        self.pick3 = Button(self.core,text='select output',command=pickthree).place(x = 320 , y = 115)

        self.process = Button(self.core,text = 'process', command=search).place(x = 480, y = 30)
        self.output = Label(self.core, textvariable=self.text ).place(x=450,y=70)

        self.idl = Label(self.core,text = 'id :').place(x=10, y=225)
        self.idin = Entry(self.core, textvariable=self.idd).place(x=10,y=250)
        self.iddo = Button(self.core, text = 'hash' ,command = dohashid).place(x = 200,y = 250)
        self.idre = Entry(self.core,textvariable=self.var).place(x=300,y=250)
    def browsefile(self):
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("csv Files","*.csv*"),("all files","*.*")))
        return filename
    def browsedir(self):
        dirname = filedialog.askdirectory(initialdir = "/",title = "Select a Directory")
        return dirname

def pickone():
    screen.file1.set(screen.browsefile())

def picktwo():
    screen.file2.set(screen.browsefile())

def pickthree():
    screen.file3.set(screen.browsedir())

def dohashid():
    screen.var.set(hash(screen.idd.get()))

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


def search():
    try : 
        screen.text.set('In progress...')
        start = time.time()
        with open(screen.file1.get(), newline='') as f:
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

            with open(screen.file2.get(), newline='') as f:
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
            a = screen.file3.get()+'/battlestringoutput.txt'
            print(a)
            with open(a,'w') as output :
                while i < len(tabn) and j < len(tabe) :
                    if tabn[i]!='' or tabe[j]!='':
                        if tabn[i][0:8] == tabe[j][0:8]:
                            i += 2
                            j += 2
                        else :
                            print(str(tabe[j]))
                            char = str(tabe[j]) 
                            output.write(char)
                            index += 1
                            j += 2
                    else :
                        if tabn[i]=='':
                            i +=1
                        if tabe[j]=='':
                            j +=1
                output.write('found {} matches.'.format(index+1))
                print('found {} matches in {}s.'.format(index+1,(time.time()-start)))
                screen.text.set('found {} matches \n in {}s.'.format(index+1,(time.time()-start)))
    except :
        screen.text.set('Error try again')

screen = window('600x300','test')
screen.core.mainloop()
