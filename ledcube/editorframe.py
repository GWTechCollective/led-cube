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
        #self.threed_view = ThreeDView(self)
        self.pattern_view.grid(row=0, column=0, rowspan=2, sticky="NS", padx=10, pady=10)
        self.frame_view.grid(row=0, column=1, padx=10, pady=10)

    def add_frame(self):
        frame_values = self.frame_view.get_frame()
        duration = 1
        print(frame_values)

        self.pattern.add_frame(frame_values, duration)

    def save_frame(self):
        frame = self.frame_view.get_frame()
        print(frame)
        position = self.pattern_view.get_position()

        self.pattern.save_frame(frame, position)

    def update_views(self):
        self.pattern_view.update_view()
        self.frame_view.update_view()


class PatternView(ttk.LabelFrame):

    def __init__(self, parent):
        ttk.LabelFrame.__init__(self, parent, text='Pattern Editor', padding="10 10 10 10")
        self.parent = parent

        ttk.Button(self, text='Move Frame Up').pack(fill=tk.X)
        ttk.Button(self, text='Move Frame Down').pack(fill=tk.X)

        self.scrollbar = ttk.Scrollbar(self)
        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        self.frame_list = tk.Listbox(self, yscrollcommand=self.scrollbar.set)

        self.update_view()

    def update_view(self):
        for index, frame in enumerate(self.parent.pattern.frames):
            self.frame_list.insert(tk.END, "Frame " + str(index))

    def get_position(self):

        return 0

class FrameView(ttk.LabelFrame):

    def __init__(self, parent):
        ttk.LabelFrame.__init__(self, parent, text='Frame Editor', padding="10 10 10 10")
        self.parent = parent

        self.led_buttons = []
        self.led_button_frame = None

        self.make_led_buttons(LENGTH, WIDTH, HEIGHT)

        ttk.Button(self, text='Add Frame', command=parent.add_frame).grid(row=0, column=0, sticky="EW")
        ttk.Button(self, text='Save Frame', command=parent.save_frame).grid(row=0, column=1, sticky="EW")
        self.led_button_frame.grid(row=1, column=0, columnspan=2)

    def button_press(self, button_id):
        #print ("Callback ID: " + str(button_id))

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
                    #print("ID: "+str(button_id)+"\tRow: "+str(height)+"\tCol: "+str(length+width*(max_length+1)))
                    button_id += 1
        # make this more general at some point
        ttk.Separator(self.led_button_frame, orient=tk.VERTICAL).grid(row=0, column=3, rowspan=max_height, sticky="NS")
        ttk.Separator(self.led_button_frame, orient=tk.VERTICAL).grid(row=0, column=7, rowspan=max_height, sticky="NS")
        self.led_button_frame.columnconfigure(3, minsize=10)
        self.led_button_frame.columnconfigure(7, minsize=10)





    def get_frame(self):
        frame_values = []

        for index, led in enumerate(self.led_buttons):
            value = led.cget('text')
            if value == '':
                frame_values.append(0)
            elif value == 'X':
                frame_values.append(1)
            else:
                print("ERROR: Invalid value for led {} in frame.".format())

        return frame_values

    def update_view(self):
        pass

class ThreeDView(ttk.LabelFrame):

    def __init__(self, parent):
        ttk.LabelFrame.__init__(self, parent)
