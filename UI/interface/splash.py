from tkinter import ttk
import customtkinter as ctk
from tkinter import Tk
from tkinter.ttk import Progressbar
from tkinter import *

from UI.dashboard import main_screen

w=Tk()


width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))


w.overrideredirect(1)


s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='black')
progress=Progressbar(w,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate',)


def splash():
    w.mainloop()

def bar():

    l4=Label(w,text='Chargement...',fg='white',bg=a)
    lst4=('Calibri (Body)',10)
    l4.config(font=lst4)
    l4.place(x=18,y=210)
    
    import time
    r=0
    for i in range(100):
        progress['value']=r
        w.update_idletasks()
        time.sleep(0.03)
        r=r+1
    
    
    w.after(2000, w.destroy() )
    main_screen()
        
    
progress.place(x=-10,y=235)


a='#B60000'
Frame(w,width=427,height=241,bg=a).place(x=0,y=0)  #249794
b1=Button(w,width=10,height=1,text='Get Started',command=bar,border=0,fg=a,bg='white')
b1.place(x=170,y=200)


######## Label

l1=Label(w,text='Génération',fg='white',bg=a)
lst1=('Calibri (Body)',14,'bold')
l1.config(font=lst1)
l1.place(x=50,y=80)

l2=Label(w,text='automatique',fg='white',bg=a)
lst2=('Calibri (Body)',14)
l2.config(font=lst2)
l2.place(x=155,y=82)

l3=Label(w,text='DE PROGRAMME',fg='white',bg=a)
lst3=('Calibri (Body)',10)
l3.config(font=lst3)
l3.place(x=50,y=110)

  





