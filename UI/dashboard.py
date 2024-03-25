import customtkinter as ctk
from tkinter import Tk


mon_font = ctk.CTKFont(size= 44, weith = "bold" )

def main_screen():
    app = ctk.CTk()
    app.geometry("900x600")
    app.title("-----Generation auto------")
    # w.destroy()
    header_frame = ctk.CTkFrame(master=app)
    data_frame = ctk.CTkFrame(master=app)
    header_label = ctk.CTkLabel(master=header_frame, text="")
    header_label.pack()
    data_label = ctk.CTkLabel(master=data_frame, font=mon_font, text="Aucune matiera enregister")
    data_label.pack()
    # Arrange the frames in your desired layout
    header_frame.grid(row=0, column=0, columnspan=2)
    data_frame.grid(row=1, column=0, columnspan=2)
    # Customize appearance (optional)
    ctk.set_appearance_mode("light")  
    app.mainloop()
    
    
    
main_screen()