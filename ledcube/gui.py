import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import tkinter.filedialog as filedialog

from editorframe import *

class Application(ttk.Frame):
    def __init__(self, parent=None):
        ttk.Frame.__init__(self, parent, width=800, height=600, padding="10 10 10 10")

        self.menubar = tk.Menu(parent, tearoff=False)
        parent.config(menu=self.menubar)
        self.make_menu()

        self.pack()

        self.pattern = None

    def make_menu(self):

        filemenu = tk.Menu(self.menubar, tearoff=False)
        filemenu.add_command(label='New', command=self.create_new_pattern)
        filemenu.add_command(label='Open', command=self.load_pattern)
        filemenu.add_command(label='Save', command=self.save_pattern)
        filemenu.add_command(label='Close', command=self.close_pattern)
        self.menubar.add_cascade(label='File', menu=filemenu)

        for child in self.winfo_children():
            child.pack()

    def create_new_pattern(self):
        if self.pattern:
            response = tk.messagebox.askyesno(message='Are you sure you want to overwrite the current pattern?', icon='question', title='New Pattern?')
            if response == 'yes':
                self.pattern = cube.Pattern((3, 3, 3))
                self.editor_frame.destroy()
                self.editor_frame = EditorFrame(self, self.pattern)
            elif response == 'no':
                pass

        elif not self.pattern:
            self.pattern = cube.Pattern((3, 3, 3))
            self.editor_frame = EditorFrame(self, self.pattern)

        else:
            print('ERROR: Program does not know if a pattern exists or not')

    def load_pattern(self):

        if self.pattern:
            response = tk.messagebox.askyesno(message='Are you sure you want to overwrite the current pattern?', icon='question', title='Load Pattern?')
            if response == True:
                filename = filedialog.askopenfilename()
                print("Filename: "+filename)
                if filename:
                    self.pattern = cube.Pattern()
                    self.pattern.load(filename)
                    self.editor_frame.destroy()
                    self.editor_frame = EditorFrame(self, self.pattern)
            elif response == False:
                print('No pattern loaded.')

            else:
                print('Response was not yes or no')

        else:
            filename = filedialog.askopenfilename()
            if filename:
                self.pattern = cube.Pattern()
                self.pattern.load(filename)
                self.editor_frame = EditorFrame(self, self.pattern)

    def save_pattern(self):

        if self.pattern:
            filename = filedialog.asksaveasfilename()
            if filename:
                self.pattern.save(filename)

        else:
            tk.messagebox(message='There is no pattern to save.')

    def close_pattern(self):
        self.editor_frame.destroy()
        self.pattern = None
