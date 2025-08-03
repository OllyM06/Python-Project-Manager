import os
import json
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

    # Load existing paths if data.json exists
    data = {"pypaths": []}
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            try:
                data = json.load(f)
            except Exception:
                data = {"pypaths": []}

    # Add new path if not already present
    if pypath not in data["pypaths"]:
        data["pypaths"].append(pypath)
    with open("data.json", "w") as f:
        json.dump(data, f)

        if filepath:
            filename = filepath.split("/")[-1]
            global pyfile
            pyfile = tkin.Label(filesection, text=f"{filename}", bg="lightgrey", font=bold_font, cursor="hand2")
            pyfile.pack(pady=5)
            pyfile.bind("<Button-1>", lambda e: open_py_folder())

def load_py_files():
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            try:
                data = json.load(f)
                for path in data.get("pypaths", []):
                    for file in os.listdir(path):
                        if file.endswith(".py"):
                            pyfile = tkin.Label(filesection, text=file, bg="lightgrey", font=bold_font, cursor="hand2")
                            pyfile.pack(pady=5)
                            pyfile.bind("<Button-1>", lambda e, p=path: os.startfile(p))
            except Exception:
                pass

def upload_txt():
    filepath = filedialog.askopenfilename(filetypes=[("TXT Notes", "*.txt")])
    global txpath
    txpath = filepath

    # Load existing txt paths if data.json exists
    data = {"txtpaths": []}
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            try:
                data = json.load(f)
            except Exception:
                data = {"txtpaths": []}

    # Add new txt path if not already present
    if "txtpaths" not in data:
        data["txtpaths"] = []
    if txpath and txpath not in data["txtpaths"]:
        data["txtpaths"].append(txpath)
    with open("data.json", "w") as f:
        json.dump(data, f)

    if filepath:
        filename = os.path.basename(filepath)
        txfile = tkin.Label(notesection, text=f"{filename}", bg="lightgrey", font=bold_font, cursor="hand2")
        txfile.pack(pady=5)
        txfile.bind("<Button-1>", lambda e: open_txt_folder())

def load_txt_files():
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            try:
                data = json.load(f)
                for path in data.get("txtpaths", []):
                    if os.path.exists(path) and path.endswith(".txt"):
                        filename = os.path.basename(path)
                        txfile = tkin.Label(notesection, text=filename, bg="lightgrey", font=bold_font, cursor="hand2")
                        txfile.pack(pady=5)
                        def open_txt(p=path):
                            global txpath
                            txpath = p
                            open_txt_folder()
                        txfile.bind("<Button-1>", lambda e, p=path: open_txt(p))
            except Exception:
                pass

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
load_py_files()

notesection = tkin.Frame(main, bd=2, relief="sunken", padx=50, pady=10, bg="lightgrey")
notesection.pack(anchor="n", padx=10, pady=10, side="right")
notesection_label = tkin.Label(notesection, text="Notes:", bg="lightgrey")
notesection_label.pack()
load_txt_files()

note_edit = tkin.Text(main, height=10, width=50, bg="lightgrey", font=("Arial", 8))
note_edit.pack(anchor="s", pady=10, padx=10, fill="both", expand=True)



main.config(menu=menubar)
main.mainloop()


