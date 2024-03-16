import time
from customtkinter import CTk
import tkinter
import customtkinter 

# Create the splash screen window
splash_screen = CTk()
splash_screen.geometry("400x300")
splash_screen.title("My App Splash Screen")

# Add elements to the splash screen (labels, images, etc.)
label = customtkinter.CTkLabel(splash_screen, text="Loading...")
label.pack(pady=20)

# Simulate some loading time
time.sleep(2)  # Replace with your actual loading logic

# Destroy the splash screen after a delay
splash_screen.after(2000, splash_screen.destroy)  # 2 seconds delay

# Your main application window and code goes here
# ... (replace with your main application logic)

splash_screen.mainloop()
