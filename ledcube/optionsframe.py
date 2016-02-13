import Tkinter as tk
import ttk

class OptionsFrame(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.pack()

        self.length = tk.StringVar()
        self.width = tk.StringVar()
        self.height = tk.StringVar()

        self.make_widgets()
        self.input_options(parent.options)

    def output_options(self):
        options = {
            "length": self.length.get(),
            "width": self.width.get(),
            "height": self.height.get()
        }

        return options

    def input_options(self, options):

        if options:
            self.length.set(options['length'])
            self.width.set(options['width'])
            self.height.set(options['height'])
        else:
            print("INFO: No options were found to load")

    def make_widgets(self):

        ttk.Label(self, text='Length:')
        length_entry = ttk.Entry(self, width=7, textvariable=self.length)
        ttk.Label(self, text='Width:')
        width_entry = ttk.Entry(self, width=7, textvariable=self.width)
        ttk.Label(self, text='Height:')
        height_entry = ttk.Entry(self, width=7, textvariable=self.height)



        for child in self.winfo_children():
            child.pack()
