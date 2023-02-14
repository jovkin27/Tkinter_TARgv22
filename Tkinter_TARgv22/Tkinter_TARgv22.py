from tkinter import*
k=0
def klikker(event):
    global k
    k+=1
    lbl.configure(text=k)

def klikker1(event):
    global k
    if k>0:
        k-=1
    else:
        k=0
    lbl.configure(text=k)

def entry_to_label(event):
    text=ent.get()
    lbl.configure(text=text)
    ent.delete(0,END)

def valik():
    text=var.get()
    ent.insert(END,text)


aken=Tk()
aken.title("Minu esimene aken")
aken.geometry("600x300")
lbl=Label(aken,
          text=" ",
          font='Arial 20',
          )
var=IntVar() #StringVar
btn=Button(aken, 
           text="Vajuta siia", 
           font="Arial 20", 
           fg="#6834eb", 
           bg="#34ebde", 
           width=30, 
           height=5,
           relief=RAISED)# SUNKEN, GROOVE
ent=Entry(aken,
          fg="#6834eb", 
          bg="#34ebde",
          width=30,
          justify=CENTER,
          )

r1=Radiobutton(aken,
               text="Esimene",
               width=20,
               font="Arial 20",
               variable=var,
               value=1,
               command=valik)

r2=Radiobutton(aken,
               text="Teine",
               width=20,
               font="Arial 20",
               variable=var,
               value=2,
               command=valik)

btn.bind("<Button-1>",klikker)#LKM
btn.bind("<Button-3>",klikker1)#PKM
ent.bind("<Return>",entry_to_label)#ENTER
btn.pack()
lbl.pack()
ent.pack()
r1.pack(side=LEFT)
r2.pack(side=LEFT)
aken.mainloop()