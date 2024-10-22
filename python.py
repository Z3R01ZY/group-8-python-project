import os
import tkinter as tk
import shutil
from tkinter import filedialog
from tkinter import messagebox

BG = "#358597"

formats = {
    ".txt": "Text Files",
    ".pdf": "PDFs",
    ".jpg": "Pictures JPGs",
    ".png": "Pictures PNGs",
    ".docx": "Word Files",
    ".mov": "Videos",
    ".mp4": "Videos",
    ".mp3": "Music"
}


def prepare_folder(input_format, directory):
    user_input = input_format.get().lower()
    if user_input not in formats.keys():
        messagebox.showerror("Error!", "Please enter a valid format")
        return
    folder_name = formats[user_input]
    folder = os.path.join(directory, folder_name)

    if not messagebox.askyesno("Confirmation",f"You are about to organize files of type '{user_input}' into the folder '{folder_name}' in the selected directory.\n\nDo you want to proceed?"):
        return

    files_found = False
    for files in os.listdir(directory):
        if files.endswith(user_input):
            files_found = True
            break

    if not files_found:
        messagebox.showinfo("Not found", f"No files of the specified type were found")
        return

    # creation ng folder
    if not os.path.exists(folder):
        os.makedirs(folder)

    # ito yung checking ng files para malipat sa folder
    files_moved = 0
    for filename in os.listdir(directory):
        if filename.endswith(user_input):
            path = os.path.join(directory, filename)
            shutil.move(path, folder) # move yung specific file using path dun sa folder
            files_moved += 1
    if files_moved == 0:
        messagebox.showinfo("No moved files", f"No files of the specified type were found to move.")
    else:
        messagebox.showinfo("Success", f"Files organized into: {folder}\nFiles moved: {files_moved}")
    return


def organize():
    directory = filedialog.askdirectory(title="Select folder to Organize")
    if not directory:
        return

    window2 = tk.Toplevel(window)
    window2.title("Please Enter Format")
    window2.geometry("500x250")
    window2.config(bg=BG)
    ask_format = tk.Label(
        window2,
        font=("Helvetica", 20, "bold"),
        text="Enter format to organize: ",
        bg=BG,
        fg="white"
    )
    ask_format.pack(pady=20)
    guide = tk.Label(
        window2,
        font=("Helvetica", 15, "bold"),
        text="examples: '.txt' '.pdf' '.docx'",
        bg=BG,
        fg="white"
    )
    guide.pack(pady=5)
    # input ng format ng user
    input_format = tk.Entry(window2, width=24)
    input_format.pack(pady=10)
    # submit
    submit = tk.Button(
        window2,
        font=("Helvetica", 18),
        text="Submit",
        bg=BG,
        fg="white",
        activebackground=BG,
        activeforeground="white",
        command=lambda: prepare_folder(input_format, directory)
    )
    submit.pack(pady=10)


window = tk.Tk()
window.title("Orga-Nice")
window.geometry("500x250")
window.config(bg=BG)

#css style, sheeesh para readable

#labels
title_label = tk.Label(
    window,
    font=("Helvetica", 20, "bold"),
    text="Welcome to Orga-Nice!",
    bg=BG,
    fg="white")
title_label.pack(pady=2)
title_label = tk.Label(
    window,
    font=("Helvetica", 12),
    text="By Giggity",
    bg=BG,
    fg="white")
title_label.pack(pady=2)

#button
organize_button = tk.Button(
    window,
    command=organize,
    text="Choose a Folder",
    bg=BG,
    fg="white",
    width=20,
    height=0,
    activebackground=BG,  #background pag na click
    activeforeground="white",  #text pag na click
    font=("Helvetica", 18)
)
organize_button.pack(pady=50)

window.mainloop()
