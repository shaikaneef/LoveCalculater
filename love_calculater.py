from tkinter import *
from tkinter import messagebox
import random
from tkinter.messagebox import showinfo
from PIL import Image,ImageTk

root=Tk()
root.title("Love calculater")
def love_calculate():
    if name_entry.get()=="" or p_name_entry.get()=="" :
        messagebox.showwarning("warning","please fill all the fields")
    
    else:
        percentage=random.randint(60,100)
        emoji="\u2764\uFE0F"
        showinfo("Love percentage",f"Love bird's love is{emoji} {percentage}%")

img_open=Image.open("chubby.jpg")
render_img=ImageTk.PhotoImage(img_open)
original_img=Label(root,image=render_img)
original_img.grid(row=0,columnspan=2)


name=Label(root,text="Enter your name :",font=("ariar",10,"bold"))
name.grid(row=2,column=0)


name_entry=Entry(root,font=("ariar",10,"bold"))
name_entry.grid(row=2,column=1)


p_name=Label(root,text="Enter your partner name :",font=("ariar",10,"bold"))
p_name.grid(row=3,column=0)


p_name_entry=Entry(root,font=("ariar",10,"bold"))
p_name_entry.grid(row=3,column=1)


button=Button(root,text="Check your love",bg="red",fg="white",command=love_calculate)
button.grid(row=4,columnspan=2)

root.mainloop()

