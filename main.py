import tkinter as tk
from tkinter import filedialog, Text
import os


root = tk.Tk()


canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack() #adds green background

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx = 0.1, rely = 0.1) # centers white box

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42")
openFile.pack()


root.mainloop()

