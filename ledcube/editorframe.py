import tkinter as tk
import tkinter.ttk as ttk

import cube

class EditorFrame(ttk.Frame):

    def __init__(self, parent, pattern):
        ttk.Frame.__init__(self, parent)
        self.pack()

        self.pattern = pattern
        self.voxel_editor = []
        self.pattern_view = []

        self.make_menu_bar()
        self.make_pattern_display()
        self.make_frame_editor()
        self.make_3d_view()

    def make_menu_bar(self):
        ttk.Button(self, text='New Pattern', command=self.create_new_pattern)
        ttk.Button(self, text='Add Frame')

        for child in self.winfo_children():
            child.pack()

    def make_pattern_display(self):
        self.pattern_view = ttk.LabelFrame(self, text='Patern Editor', padding="10 10 10 10")

        ttk.Button(self.pattern_view, text="blah").pack()


        for child in self.winfo_children():
            child.pack()

    def make_frame_editor(self):

        self.frame_editor = FrameEditor(self)

        for child in self.winfo_children():
            child.pack()

    def make_3d_view(self):
        for child in self.winfo_children():
            child.pack()

    def create_new_pattern(self):
        self.current_pattern = cube.Pattern()

    def create_new_voxel(self):
        self.current_voxel = cube.Voxel()

    def add_voxel_to_pattern(self):
        self.current_pattern.add_voxel(self.current_voxel)

class FrameEditor(ttk.LabelFrame):

    def __init__(self, parent):
        ttk.LabelFrame.__init__(self, parent, text='Frame Editor')
        self.config(padding="10 10 10 10")
        self.pack()

        self.buttons = []

        self.make_buttons(3, 3, 3)

    def button_press(self, button_id):
        print ("Callback ID: " + str(button_id))

        if self.buttons[button_id].cget('text') == '':
            self.buttons[button_id].config(text='X')
        else:
            self.buttons[button_id].config(text='')

        return True

    def make_buttons(self, max_length, max_width, max_height):

        button_id = 0

        for length in range(0, max_length * max_width):

            start = length % max_height
            end = start + max_height

            for height in range(start, end):
                self.buttons.append(ttk.Button(self, text='', width=3, command=lambda bid=button_id: self.button_press(bid)))
                self.buttons[-1].grid(row=height, column=length)
                button_id += 1


    def get_button_states(self):
        pass
