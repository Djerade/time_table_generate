import customtkinter as ctk
from tkinter import Tk
# Create the main window

def main_screen():
    app = ctk.CTk()
    app.geometry("800x600")
    app.title("--------------")
    # w.destroy()
    header_frame = ctk.CTkFrame(master=app)
    data_frame = ctk.CTkFrame(master=app)
    header_label = ctk.CTkLabel(master=header_frame, text="Welcome to your Dashboard!")
    header_label.pack()
    data_label = ctk.CTkLabel(master=data_frame, text="Data will be displayed here")
    data_label.pack()
    progress_bar = ctk.CTkProgressBar(master=data_frame)  # Example progress bar
    progress_bar.pack()
    # Arrange the frames in your desired layout
    header_frame.grid(row=0, column=0, columnspan=2)
    data_frame.grid(row=1, column=0, columnspan=2)
    # Customize appearance (optional)
    ctk.set_appearance_mode("light")  
    app.mainloop()


