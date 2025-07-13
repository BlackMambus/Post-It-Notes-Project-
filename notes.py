import tkinter as tk
from tkinter import filedialog
import os

class StickyNote:
    def __init__(self, master=None):
        self.root = tk.Tk() if master is None else tk.Toplevel(master)
        self.root.title("📝 Post-it Note")
        self.root.geometry("250x250")
        self.root.configure(bg="lightyellow")

        self.text = tk.Text(self.root, wrap="word", bg="lightyellow", font=("Arial", 12))
        self.text.pack(expand=True, fill="both")

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        file_menu = tk.Menu(self.menu, tearoff=0)
        file_menu.add_command(label="New Note", command=self.new_note)
        file_menu.add_command(label="Save Note", command=self.save_note)
        file_menu.add_command(label="Load Note", command=self.load_note)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.destroy)

        self.menu.add_cascade(label="File", menu=file_menu)

    def new_note(self):
        StickyNote(master=self.root)

    def save_note(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text.get("1.0", tk.END))

    def load_note(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path and os.path.exists(file_path):
            with open(file_path, "r") as file:
                content = file.read()
                self.text.delete("1.0", tk.END)
                self.text.insert(tk.END, content)

def run_post_it_app():
    StickyNote()
    tk.mainloop()

# Run the app
run_post_it_app()




