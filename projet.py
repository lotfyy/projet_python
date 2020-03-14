from tkinter import *
from tkinter import ttk
import sqlite3





db = sqlite3.connect('mysq.db')
cursor = db.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Notes(
     id integer ,
     note_python integer,
     note_algebre integer,
     note_analyse integer,
     note_mecanique integer,
     note_electronique integer,
     note_anglais integer,
     note_communication_fr integer,
     note_PNL integer,
     note_BaseDonnee integer,
     note_flash integer
     
)
""")
cursor.execute('''
CREATE TABLE IF NOT EXISTS Etudiant(
     id integer ,
     nom text ,
     prenom text 
      
)''')
etudiant=[(1,'AROUS','Wael'),(2,'BAALOUCH','Mayssa'),(3,'BACCAR','Anwer'),(4,'BEN AMARA','Rania'),(5,'BEN CHAALIA','Samy'),
          (6, 'BEN REGBA', 'Nour Mayssene'),(7,'BOUZIRI ','Youssef'),(8,'ETTEIBI','Lotfi'),(9,'FERJANI','Olfa'),(10,'HAMDI ','Mohamed'),
          (11, 'HAMZA', 'Taha Halim'),(12,'KAOUEL','Mohamed Amine'),(13,'KARRAY','Yasmine'),(14,'MANSOURI','Ala'),(15,'NOUIRA','Bessem'),
          (16, 'OUKHAY', 'Ayed'),(17,'ROUINI','Kais'),(18,'SOUILHI','Nesrine'),(19,'ZAKHAMA','Saif Eddine')]
for i in etudiant:
    cursor.execute("insert into Etudiant(id, nom,prenom) VALUES(?,?,?)", i)
#    print(i)

db.commit()
root=Tk()
root.title("Notes des etudiants")
lab=Label(root,text='ID:')
lab.grid(column=0, row=0)

ID=StringVar()
E=Entry(root,width=20,textvar=ID)
E.grid(column=1, row=0)

lab2=Label(root,text='Note python:')
lab2.grid(column=0, row=1)

note_python=StringVar()
E1=Entry(root ,textvar=note_python)
E1.grid(column=1, row=1)

lab3=Label(root,text='Note algebre:')
lab3.grid(column=0, row=2)

note_algebre=StringVar()
E2=Entry(root,width=20, textvar=note_algebre)
E2.grid(column=1, row=2)

lab4=Label(root,text='Note analyse:')
lab4.grid(column=0, row=3)

note_analyse=StringVar()
E3=Entry(root,width=20, textvar=note_analyse)
E3.grid(column=1, row=3)
lab5=Label(root,text='Note mecanique:')
lab5.grid(column=0, row=4)

note_mecanique=StringVar()
E4=Entry(root,width=20, textvar=note_mecanique)
E4.grid(column=1, row=4)
lab6=Label(root,text='Note electronique:')
lab6.grid(column=0, row=5)

note_electronique=StringVar()
E5=Entry(root,width=20 ,textvar=note_electronique)
E5.grid(column=1, row=5)
lab7=Label(root,text='Note anglais:')
lab7.grid(column=0, row=6)

note_anglais=StringVar()
E6=Entry(root,width=20, textvar=note_anglais)
E6.grid(column=1, row=6)
lab8=Label(root,text='Note communication fr:')
lab8.grid(column=0, row=7)

note_communication_fr=StringVar()
E7=Entry(root,width=20 ,textvar=note_communication_fr)
E7.grid(column=1, row=7)
lab9=Label(root,text='Note PNL:')
lab9.grid(column=0, row=8)

note_PNL=StringVar()
E8=Entry(root,width=20 ,textvar=note_PNL)
E8.grid(column=1, row=8)
lab10=Label(root,text='Note BaseDonnee:')
lab10.grid(column=0, row=9)

note_BaseDonnee=StringVar()
E9=Entry(root,width=20 ,textvar=note_BaseDonnee)
E9.grid(column=1, row=9)

lab10=Label(root,text='Note flash:')
lab10.grid(column=0, row=10)

note_flash=StringVar()
E10=Entry(root,width=20 ,textvar=note_flash)
E10.grid(column=1, row=10)




def valider():
   
   x1 = ID.get()
   x2=note_python.get()
   x3=note_algebre.get()
   x4=note_analyse.get()
   x5=note_mecanique.get()
   x6=note_electronique.get()
   x7=note_anglais.get()
   x8=note_communication_fr.get()
   x9=note_PNL.get()
   x10=note_BaseDonnee.get()
   x11=note_flash.get()
   conn = sqlite3.connect('mysq.db')
   with conn:
      cursor = conn.cursor()
      cursor.execute('INSERT INTO Notes(ID, note_python, note_algebre,note_analyse,note_mecanique,note_electronique,note_anglais,note_communication_fr,note_PNL,note_BaseDonnee,note_flash) VALUES(?,?,?,?,?,?,?,?,?,?,?)',(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11))
      db.close()  

def afficher():
   connt = sqlite3.connect('mysq.db')
   cursor = connt.cursor()
   cursor.execute('SELECT * FROM Notes')
   for row in cursor.fetchall():
      print(row)
   tv.insert('',0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])) 
def supp():
   ID.set("")
   note_python.set("")
   note_algebre.set("")
   note_analyse.set("")
   note_mecanique.set("")
   note_electronique.set("")
   note_anglais.set("")
   note_communication_fr.set("")
   note_PNL.set("")
   note_BaseDonnee.set("")
   note_flash.set("")
     
   
      
def afficher2():
   root1=Tk()
   root1.title("Liste des etudiants")
   tv=ttk.Treeview(root1,height=25,columns=('1','2','3' ))
   tv.grid(column=0 , row=0 , columnspan=4)            
   tv.heading ('#0',text='ID')
   tv.column("#0",minwidth=30,width=90 )
   tv.heading ('#1',text='Nom')
   tv.column("#1",minwidth=90,width=90 )
   tv.heading ('#2',text='Prenom')
   tv.column("#2",minwidth=90,width=90) 
   connt = sqlite3.connect('mysq.db')
   cursor = connt.cursor()
   cursor.execute("SELECT * FROM Etudiant order by Etudiant.ID")
   for row in cursor.fetchall():
      tv.insert('',0,text=row[0],values=(row[1],row[2]))
      
def moyenne():
   root1=Tk()
   root1.title("Moyennes")
   connt = sqlite3.connect('mysq.db')
   cursor = connt.cursor()
   cursor.execute("SELECT  Etudiant.ID,nom , avg((note_python*2+note_algebre) as moy FROM Notes ,Etudiant")
   for row in cursor.fetchall():
      print(row)
   
   
   
but=Button(root,padx=2,pady=2,text='Valider',command=valider)
but.grid(column=0, row=11)

res=Button(root,padx=2,pady=2,text='Afficher',command=afficher)
res.grid(column=1, row=11)
res=Button(root,padx=2,pady=2,text='Afficher la liste des etudiants',command=afficher2)
res.grid(column=2, row=11)
res=Button(root,padx=2,pady=2,text='Réinitialiser' ,command=supp)
res.grid(column=3, row=10)
res=Button(root,padx=2,pady=2,text='Moyenne',command=moyenne)
res.grid(column=3, row=11)

tv=ttk.Treeview(root,height=15,columns=('1','Note python','de','d','ddd','dd','fff','fff','ff','ff'))
tv.grid(column=0 , row=12 , columnspan=4)

tv.heading ('#0',text='ID'  )
tv.column("#0",minwidth=30,width=90 )
tv.heading ('#1',text='Note python')
tv.column("#1",minwidth=90,width=90 )
tv.heading ('#2',text='Note algebre')
tv.column("#2",minwidth=90,width=90 )
tv.heading ('#3',text='Note analyse')
tv.column("#3",minwidth=90,width=90 )
tv.heading ('#4',text='Note mecanique')
tv.column("#4",minwidth=90,width=90 )
tv.heading ('#5',text='Note electronique')
tv.column("#5",minwidth=90,width=90 )
tv.heading ('#6',text='Note anglais')
tv.column("#6",minwidth=90,width=90 )
tv.heading ('#7',text='Note fr')
tv.column("#7",minwidth=90,width=90 )
tv.heading ('#8',text='Note PNL')
tv.column("#8",minwidth=90,width=90 )
tv.heading ('#9',text='Note BaseDonnee')
tv.column("#9",minwidth=90,width=90 )
tv.heading ('#10',text='Note flash')
tv.column("#10",minwidth=90,width=90 )
 



  

root.mainloop()
