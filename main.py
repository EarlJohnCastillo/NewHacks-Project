import tkinter as tk
from tkinter import filedialog, Text
import os


root = tk.Tk()
apps = []




def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables", "*.PNG"),("all files", "*.*")))

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg ="gray")
        label.pack()

def runApp():
    for app in apps:
        os.startfile(app)

def addCourse():
    print("How many courses are you taking?")
    x = input()
    print(x)




canvas = tk.Canvas(root, height=800, width=800, bg="#78C7C7")
canvas.pack() #adds green background

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.7, relheight=0.7, relx=0.1, rely = 0.1) # centers white box

openFile = tk.Button(root, text="Open File", width=10, padx=10, pady=10, fg="white", bg="#263D42", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", width=10, padx=10, pady=10, fg="white", bg="#263D42", command=runApp)
runApps.pack()

addCourses = tk.Button(root, text="Add Courses",width=10, padx=10, pady=5, fg="white", bg="#263D42", command = addCourse)
addCourses.pack()

root.mainloop()

