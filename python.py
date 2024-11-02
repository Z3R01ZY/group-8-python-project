import os
import tkinter as tk
import shutil
from tkinter import filedialog
from tkinter import messagebox

BG = "#358597"  # BACKGROUND COLOR NATIN
# gathered most of the formats <3
formats = {
    # Text and Document Files
    ".txt": "Text Files",
    ".pdf": "PDFs",
    ".doc": "Word Files",
    ".docx": "Word Files",
    ".odt": "OpenDocument Text",
    ".rtf": "Rich Text Format",
    ".xls": "Excel Files",
    ".xlsx": "Excel Files",
    ".ppt": "PowerPoint Presentations",
    ".pptx": "PowerPoint Presentations",
    ".csv": "Comma-Separated Values",
    ".xml": "XML Files",
    ".md": "Markdown Files",

    # Image Files
    ".jpg": "Pictures JPGs",
    ".jpeg": "Pictures JPEGs",
    ".png": "Pictures PNGs",
    ".gif": "GIF Images",
    ".bmp": "Bitmap Images",
    ".tif": "TIFF Images",
    ".tiff": "TIFF Images",
    ".svg": "Vector Images",
    ".ico": "Icons",
    ".webp": "Web Picture",

    # Video Files
    ".mov": "Videos",
    ".mp4": "Videos",
    ".avi": "Videos",
    ".mkv": "Videos",
    ".flv": "Flash Videos",
    ".wmv": "Windows Media Videos",
    ".webm": "Web Videos",

    # Audio Files
    ".mp3": "Music",
    ".wav": "WAV Audio",
    ".flac": "Lossless Audio",
    ".aac": "AAC Audio",
    ".ogg": "OGG Audio",
    ".m4a": "M4A Audio",

    # Compressed Files
    ".zip": "Compressed Files",
    ".rar": "Compressed Files",
    ".7z": "Compressed Files",
    ".tar": "Tar Archives",
    ".gz": "Gzip Files",

    # Code and Development Files
    ".py": "Python Scripts",
    ".java": "Java Source Code",
    ".cpp": "C++ Source Code",
    ".c": "C Source Code",
    ".html": "HTML Files",
    ".css": "CSS Files",
    ".js": "JavaScript Files",
    ".php": "PHP Files",
    ".json": "JSON Files",
    ".yml": "YAML Files",
    ".yaml": "YAML Files",
    ".rb": "Ruby Files",
    ".go": "Go Source Code",
    ".sql": "SQL Files",

    # Executable Files
    ".exe": "Executable Files",
    ".msi": "Windows Installers",
    ".sh": "Shell Scripts",
    ".bat": "Batch Files",
    ".apk": "Android Packages",
    ".dmg": "MacOS Disk Images",
}


def organize_all(directory):
    if not directory:
        messagebox.showinfo("No directory", "Invalid Directory.")

    if not messagebox.askyesno("Confirmation",
                               "Are you sure you want to organize all file in the selected folder?"):
        return
    files_found = False
    file_count = 0
    for file in os.listdir(directory):
        file_extension = os.path.splitext(file)[1].lower()
        if file_extension in formats:
            files_found = True
            file_name = formats[file_extension]
            folder_path = os.path.join(directory, file_name)
            file_count += 1
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            shutil.move(str(os.path.join(directory, file)), str(folder_path))
    if not files_found:
        messagebox.showinfo("No files", "No files to organize")
    else:
        messagebox.showinfo("Success", f"Selected files have been organized.\nFiles found:{file_count}")


def prepare_folder(input_format, directory):
    user_input = input_format.get().lower()
    if user_input not in formats.keys():
        messagebox.showerror("Error!", "Please enter a valid format")
        return
    folder_name = formats[user_input]
    folder = os.path.join(directory, folder_name)

    if not messagebox.askyesno("Confirmation",
                               f"You are about to organize files of type '{user_input}' into the folder '{folder_name}"
                               f"' in the selected directory.\n\nDo you want to proceed?"):
        return

    files_found = False
    for files in os.listdir(directory):
        if files.endswith(user_input):
            files_found = True
            break

    if not files_found:
        messagebox.showinfo("Not found", f"No files of the specified type were found")
        return
    create_folder(user_input, directory, folder)


def create_folder(user_input, directory, folder):
    # creation ng folder
    if not os.path.exists(folder):
        os.makedirs(folder)

    # ito yung checking ng files para malipat sa folder
    files_moved = 0
    for filename in os.listdir(directory):
        if filename.endswith(user_input):
            path = os.path.join(directory, filename)
            shutil.move(path, folder)  # move yung specific file using path dun sa folder
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
    window2.title("Enter Format")
    window2.geometry("500x280")
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

    organize_all_files = tk.Button(
        window2,
        font=("Helvetica", 15),
        text="Organize all files",
        bg=BG,
        fg="white",
        activebackground=BG,
        activeforeground="white",
        command=lambda: organize_all(directory)
    )
    organize_all_files.pack(pady=5)


window = tk.Tk()
window.title("OrgaNice")
window.geometry("500x250")
window.config(bg=BG)

# css style, sheeesh para readable

# labels
title_label = tk.Label(
    window,
    font=("Helvetica", 20, "bold"),
    text="Welcome to OrgaNice!",
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

# button
organize_button = tk.Button(
    window,
    command=organize,
    text="Choose a Folder",
    bg=BG,
    fg="white",
    width=20,
    height=0,
    activebackground=BG,  # background pag na click
    activeforeground="white",  # text pag na click
    font=("Helvetica", 18)
)
organize_button.pack(pady=50)

window.mainloop()
