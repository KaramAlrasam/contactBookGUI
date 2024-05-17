from tkinter import *
from tkinter import messagebox

window=Tk()
window.geometry("400x400")
window.config(background="#C5A6F4")
window.title("Contacts book")
contacts_list=[
    ["karam","0782718137"]   
]

name=StringVar()
number=StringVar()

frame=Frame(window,relief="ridge")
frame.pack(side="right",fill="both")
scrooll=Scrollbar(frame,orient=VERTICAL)
select=Listbox(frame,yscrollcommand=scrooll.set,width=15,borderwidth=5)
scrooll.config(command=select.yview)
scrooll.pack(side="right",fill="both")
select.pack(side=RIGHT,fill="both")

def selected():
    print("Hello",len(select.curselection()))
    if select.curselection():
        
        return int(select.curselection()[0])
    else:
        messagebox.showerror("You must add item")
def AddItem():
    if name.get()and number.get():
        contacts_list.append([name.get(),number.get()])
        messagebox.showinfo("It is added")
        Entry_reset()
        reset_listbox()
    else:
        messagebox.showerror("You must fill two inputs")
def Entry_reset():
    name.set("")
    number.set("")
    
    
def reset_listbox():
    select.delete(0,END)
    for name,_ in contacts_list:
        select.insert(END,name)
        
def uppdate():
    if name.get()or number.get():
        contacts_list[selected()]=[name.get(),number.get()]
        Entry_reset()
        reset_listbox()
        messagebox.showinfo("It is uppdated")
    else:
        messagebox.showerror("You have to choose item to update it")
def delete_item():
    if select.curselection():
        ansewr=messagebox.askyesno("Do you want to delete this item?")
        if ansewr==True:
            del contacts_list[selected()]
            messagebox.showinfo("It is deleted!")
            reset_listbox()
    else:
        messagebox.showerror("You must choose item befor to delete!")

def View():
    if select.curselection():
        Name, Number=contacts_list[selected()]
        name.set(Name)
        number.set(Number)
    else:
        messagebox.showerror("You must choose item!!!")
def Exit():
    window.destroy()
reset_listbox()
Label(window,text="Name",font=("Times new roman",10),bg="#7851a9",fg="black").place(x=20,y=10)
Entry(window,textvariable=name,width=30,relief="solid").place(x=90,y=10)
Label(window,text="Number",font=("Times new roman",10),fg="black",bg="#7851a9").place(x=20,y=40)
Entry(window,textvariable=number,width=30,relief="solid").place(x=90,y=40)

Button(window,bg="#648c11",font="Verdana",fg="black",command=AddItem,text="Add").place(x=40,y=80)
Button(window,bg="#648c11",font="Verdana",fg="black",command=View,text="View").place(x=87,y=80)
Button(window,bg="#800000",font="Verdana",fg="black",command=delete_item,text="Delete").place(x=40,y=115)
Button(window,bg="#648c11",font="Verdana",fg="black",command=uppdate,text="uppdate item").place(x=143,y=80)
Button(window,bg="#648c11",font="Verdana",fg="black",command=Entry_reset,text="reset").place(x=110,y=115)
Button(window,bg="#e60026",font="Verdana",fg="black",command=Exit,text="Exit").place(x=170,y=115)


window.update()

   
window.mainloop()