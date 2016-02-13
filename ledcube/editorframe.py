import Tkinter as tk
import ttk

import cube

class EditorFrame(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.pack()

        self.make_menu_bar()
        self.make_pattern_display()
        self.make_voxel_editor()
        self.make_3d_view()

    def make_menu_bar(self):
        ttk.Button(self, text='New Pattern', command=self.create_new_pattern())
        ttk.Button(self, text='Add Voxel')

        for child in self.winfo_children():
            child.pack()

    def make_pattern_display(self):
        for child in self.winfo_children():
            child.pack()

    def make_voxel_editor(self):

        vview = VoxelView(self)

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

class VoxelView(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.pack()

        self.buttons = []

        self.make_buttons(3, 3, 3)

    def button_press(self, button_id):
        print "Callback ID: " + str(button_id)
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
                self.buttons.append(ttk.Button(self, text='', command=lambda bid=button_id: self.button_press(bid)))
                print "Assigned ID: " + str(button_id)
                self.buttons[-1].grid(row=height, column=length)
                button_id += 1


    def get_button_states(self):
        pass
