import tkinter as tk
import tkinter.ttk as ttk

from math import floor

import cube

LENGTH = 3
WIDTH = 3
HEIGHT = 3


class EditorFrame(ttk.Frame):

    def __init__(self, parent, pattern):
        ttk.Frame.__init__(self, parent)
        self.pack(fill=tk.BOTH)

        self.pattern = pattern

        self.frame_view = None
        self.pattern_view = None

        self.make_widgets()
        self.update_views()

    def make_widgets(self):

        self.pattern_view = PatternView(self)
        self.frame_view = FrameView(self)
        self.threed_view = ThreeDView(self)
        self.pattern_view.grid(row=0, column=0, rowspan=2, sticky="NS", padx=10, pady=10)
        self.frame_view.grid(row=0, column=1, sticky="EW", padx=10, pady=10)
        self.threed_view.grid(row=1, column=1, sticky="EW", padx=10, pady=10)

    def add_frame(self):
        index = self.pattern_view.get_index()
        frame_values = self.frame_view.get_frame()
        duration = 1

        self.pattern.add_frame(index, frame_values, duration)
        self.update_views()

    def save_frame(self):
        index = self.pattern_view.get_index()
        frame_values = self.frame_view.get_frame()
        duration = 1

        self.pattern.save_frame(index, frame_values, duration)
        self.update_views()

    def delete_frame(self):
        index = self.pattern_view.get_index()

        self.pattern.remove_frame(index)
        self.update_views()

    def move_frame_up(self):
        index = self.pattern_view.get_index()
        self.pattern.move_frame_up(index)
        self.update_views()
    def move_frame_down(self):
        index = self.pattern_view.get_index()
        self.pattern.move_frame_down(index)
        self.update_views()

    def update_views(self):
        self.pattern_view.update_view()
        self.frame_view.update_view()


class PatternView(ttk.LabelFrame):

    def __init__(self, parent):
        ttk.LabelFrame.__init__(self, parent, text='Pattern Editor', padding="10 10 10 10")
        self.parent = parent

        ttk.Button(self, text='Move Frame Up', command=self.parent.move_frame_up).pack(fill=tk.X)
        ttk.Button(self, text='Move Frame Down', command=self.parent.move_frame_down).pack(fill=tk.X)
        ttk.Button(self, text='Delete', command=self.parent.delete_frame).pack(fill=tk.X)

        self.scrollbar = ttk.Scrollbar(self)
        self.frame_list = tk.Listbox(self, yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        self.frame_list.pack(side=tk.LEFT, fill=tk.Y)

        self.frame_list.bind('<<ListboxSelect>>', self.on_select)

        self.update_view()

    def update_view(self):

        self.frame_list.delete(0, tk.END)

        for index, frame in enumerate(self.parent.pattern.frames):

            self.frame_list.insert(tk.END, "Frame " + str(index))

    def on_select(self, event):
        index = self.get_index()
        self.parent.frame_view.set_frame(self.parent.pattern.get_frame(index))

    def get_index(self):
        index = self.frame_list.curselection()
        if index:
            return index[0]
        else:
            return -1

class FrameView(ttk.LabelFrame):

    def __init__(self, parent):
        ttk.LabelFrame.__init__(self, parent, text='Frame Editor', padding="10 10 10 10")
        self.parent = parent

        self.led_buttons = []
        self.led_button_frame = None

        self.make_led_buttons(LENGTH, WIDTH, HEIGHT)

        ttk.Button(self, text='Add Frame', command=parent.add_frame).grid(row=0, column=0, sticky="EW")
        ttk.Button(self, text='Save Frame', command=parent.save_frame).grid(row=0, column=1, sticky="EW")
        self.led_button_frame.grid(row=1, column=0, columnspan=2, sticky="EW")

    def button_press(self, button_id):

        if self.led_buttons[button_id].cget('text') == '':
            self.led_buttons[button_id].config(text='X')
        else:
            self.led_buttons[button_id].config(text='')

        return True

    def make_led_buttons(self, max_length, max_width, max_height):

        self.led_button_frame = ttk.Frame(self, padding="0 10 0 10")

        self.led_buttons = []
        button_id = 0

        for width in range(max_width):
            for height in range(max_height):
                for length in range(max_length):
                    self.led_buttons.append(ttk.Button(self.led_button_frame, text='', width=3, command=lambda bid=button_id: self.button_press(bid)))
                    self.led_buttons[-1].grid(sticky=tk.N+tk.S+tk.E+tk.W, row=height, column=(length+width*(max_length+1)))
                    button_id += 1
        # make this more general at some point
        ttk.Separator(self.led_button_frame, orient=tk.VERTICAL).grid(row=0, column=3, rowspan=max_height, sticky="NS")
        ttk.Separator(self.led_button_frame, orient=tk.VERTICAL).grid(row=0, column=7, rowspan=max_height, sticky="NS")
        self.led_button_frame.columnconfigure(3, minsize=10)
        self.led_button_frame.columnconfigure(7, minsize=10)



    def set_frame(self, values):
        for index, led in enumerate(self.led_buttons):
            if values[index] == 0:
                led.config(text='')
            elif values[index] == 1:
                led.config(text='X')
            else:
                print('ERROR: Invalid value {} in frame at index {}'.format(values[index], index))

    def get_frame(self):
        frame_values = []

        for index, led in enumerate(self.led_buttons):
            value = led.cget('text')
            if value == '':
                frame_values.append(0)
            elif value == 'X':
                frame_values.append(1)
            else:
                print("ERROR: Invalid value for led {} in frame.".format(index))

        return frame_values

    def update_view(self):
        pass

class ThreeDView(ttk.LabelFrame):

    def __init__(self, parent):
        ttk.LabelFrame.__init__(self, parent, text='3D View')
        tk.Canvas(self).pack()
