import tkinter as tk
from tkinter import LEFT, BOTH
import customtkinter
from tk_front import App_front
from kivy.core.window import Window
from kivy.app import App


class App_new(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # dpi = self.winfo_fpixels('1i')
        # factor = dpi / 72
        #
        # width = self.winfo_screenwidth()
        # height = self.winfo_screenheight()
        #
        # ratio_1 = width * height
        # ratio_2 = 1
        # r2_width = 4
        # r2_height = 3
        #
        # while (ratio_1 / ratio_2) != 1.6875:
        #    r2_height = r2_width / 1.33333333333
        #    ratio_2 = r2_width * r2_height
        #    r2_width = r2_width + 1
        #
        #    if (ratio_1/ratio_2) <= 1.6875:
        #        break
        #    if width + 1 == r2_width:
        #        break
        #
        # self.geometry(str(r2_width) + "x"+ str(int(r2_height)))
        #
        #
        # factor_multiplier = (.40*factor) +.46
        # factor = factor/factor_multiplier
        self.title("Group creation tool")
        app = App_front(self)
        app.pack(side=LEFT, fill=BOTH, expand=True)
        # app.tk.call('tk', 'scaling', factor)
        # app.place(height=int(r2_height), width = r2_width)


class MyApp(App):
    size_x = NumericProperty(0)
    size_y = NumericProperty(0)

    def on_start(self):
        window_sizes = Window.size
        self.size_x, self.size_y = window_sizes
        print(self.size_x, self.size_y)


if __name__ == "__main__":
    MyApp().run()
