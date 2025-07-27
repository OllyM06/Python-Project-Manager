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
    global filename
    filepath = filedialog.askopenfilename(filetypes=[("TXT Notes", "*.txt")])
    global txt_file
        
    if filepath:
        
        filename = filepath.split("/")[-1]
        global txpath
        txpath = filepath
        txt_file = filepath
        txfile = tkin.Label(notesection, text=f"{filename}", bg="lightgrey", font=bold_font, cursor="hand2")
        txfile.pack(pady=5)
        txfile.bind("<Button-1>", lambda e: open_txt_folder())

def open_txt_folder():
    # IDK why but tou need to define txt_file in both functions from the global variable 'txpath'.
    txt_file = txpath # <-- Right here.
    with open(txt_file, "r") as txt_file:
        content = txt_file.read()
    note_edit.delete(1.0, tkin.END)
    note_edit.insert(tkin.END, content)

    def save_notes(event=None):
        txt_file = txpath
        with open(txt_file, "w") as txt_file:
            txt_file.write(note_edit.get(1.0, tkin.END))
        messagebox.showinfo("Info", "Notes saved successfully!")

    note_edit.bind("<Control-s>", save_notes)

def open_py_folder():
    os.startfile(pypath)


# Python Project Manager GUI
main.title("Python Project Manager")
main.geometry("600x400")

menubar = tkin.Menu(main)
file_menu = tkin.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Import", menu=file_menu)
file_menu.add_command(label="Python Script", command=upload_py)
file_menu.add_separator()
file_menu.add_command(label="TXT Notes", command=upload_txt)


filesection = tkin.Frame(main, bd=2, relief="sunken", padx=50, pady=10, bg="lightgrey")
filesection.pack(anchor="n", padx=10, pady=10, side="left")
filesection_label = tkin.Label(filesection, text="Scripts:", bg="lightgrey")
filesection_label.pack()

notesection = tkin.Frame(main, bd=2, relief="sunken", padx=50, pady=10, bg="lightgrey")
notesection.pack(anchor="n", padx=10, pady=10, side="right")
notesection_label = tkin.Label(notesection, text="Notes:", bg="lightgrey")
notesection_label.pack()

note_edit = tkin.Text(main, height=10, width=50, bg="lightgrey", font=("Arial", 8))
note_edit.pack(anchor="s", pady=10, padx=10, fill="y", expand=True)



main.config(menu=menubar)
main.mainloop()

