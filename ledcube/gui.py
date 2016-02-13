import Tkinter as tk
import ttk

from editorframe import *
from optionsframe import *

class Application(ttk.Frame):
    def __init__(self, parent=None):
        ttk.Frame.__init__(self, parent)
        self.pack()

        self.options = None

        self.make_widgets()

    def make_widgets(self):

        self.toggle_button = ttk.Button(self, text='Editor', command=self.toggle_frame)

        self.current_frame = OptionsFrame(self)
        self.current_frame_name = 'options'

        for child in self.winfo_children():
            child.pack()

    def toggle_frame(self):
        print self.current_frame_name
        if self.current_frame_name == 'options':
            self.current_frame_name = 'editor'
            self.toggle_button.config(text='Options')
            self.options = self.current_frame.output_options()
            self.current_frame.destroy()
            self.current_frame = EditorFrame(self)

        elif self.current_frame_name == 'editor':
            self.toggle_button.config(text='Editor')
            self.current_frame_name = 'options'
            self.current_frame.destroy()
            self.current_frame = OptionsFrame(self)

        else:
            print("WARNING: Invalid value for current_frame")
            pass
