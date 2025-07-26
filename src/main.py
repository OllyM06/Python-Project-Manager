import os
import tkinter as tkin
from tkinter import messagebox
from tkinter import filedialog



main = tkin.Tk()

global bold_font
bold_font = ("Arial", 10, "bold")

def upload_py():
    filepath = filedialog.askopenfilename(filetypes=[("Python Scripts", "*.py")])
    global pypath
    pypath = os.path.dirname(filepath)
        
    if filepath:
        filename = filepath.split("/")[-1]
        global pyfile
        pyfile = tkin.Label(filesection, text=f"{filename}", bg="lightgrey", font=bold_font, cursor="hand2")
        pyfile.pack(pady=5)
        pyfile.bind("<Button-1>", lambda e: open_py_folder())

def upload_txt():
    filepath = filedialog.askopenfilename(filetypes=[("TXT Notes", "*.txt")])
    global txpath
    txpath = os.path.dirname(filepath)
        
    if filepath:
        filename = filepath.split("/")[-1]
        global txfile
        txfile = tkin.Label(notesection, text=f"{filename}", bg="lightgrey", font=bold_font, cursor="hand2")
        txfile.pack(pady=5)
        txfile.bind("<Button-1>", lambda e: open_txt_folder())

def open_txt_folder():
    os.startfile(txpath)

def open_py_folder():
    os.startfile(pypath)

main.title("Python Project Manager")
main.geometry("600x400")
upload_button = tkin.Button(main, text="Upload Python Script", relief="raised", bd=2, command=lambda: upload_py())
upload_button.pack(pady=5)
upload_note_button = tkin.Button(main, text="Upload TXT Note", relief="raised", bd=2, command=lambda: upload_txt())
upload_note_button.pack(pady=5)

filesection = tkin.Frame(main, bd=2, relief="sunken", padx=50, pady=10, bg="lightgrey")
filesection.pack(anchor="n", padx=10, pady=10, side="left")
filesection_label = tkin.Label(filesection, text="Uploaded Files:", bg="lightgrey")
filesection_label.pack()

notesection = tkin.Frame(main, bd=2, relief="sunken", padx=50, pady=10, bg="lightgrey")
notesection.pack(anchor="n", padx=10, pady=10, side="right")
notesection_label = tkin.Label(notesection, text="Notes:", bg="lightgrey")
notesection_label.pack()




main.mainloop()

