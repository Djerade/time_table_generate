import customtkinter as ctk
from tkinter import Tk


listnbre = [1,2,3,4,5,6]

a= ""




def main_screen():
    app = ctk.CTk()
    app.geometry("900x600")
    app.title("--------------")
    # w.destroy()
    header_frame = ctk.CTkFrame(master=app)
    data_frame = ctk.CTkFrame(master=app)
    header_label = ctk.CTkLabel(master=header_frame, text=a)
    header_label.pack()
    for i in listnbre:
        data_label = ctk.CTkLabel(master=data_frame, text=i)
        data_label.pack()
    
    progress_bar = ctk.CTkProgressBar(master=data_frame)  # Example progress bar
    progress_bar.pack()
    # Arrange the frames in your desired layout
    header_frame.grid(row=0, column=0, columnspan=2)
    data_frame.grid(row=1, column=0, columnspan=2)
    # Customize appearance (optional)
    ctk.set_appearance_mode("light")  
    app.mainloop()
    
    
    
main_screen()