import customtkinter
from tkinter import *
from tkinter import ttk
from table import Table
from uni_group_tool.main import get_csv_table_students


class AddScrollbar(customtkinter.CTkFrame):
    def __init__(self, *args, data, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = data
        customtkinter.set_appearance_mode("dark")
        my_cavas = Canvas(
            self,
            width=160,
            height=200,
            background=self["bg"],
            bd=0,
            highlightthickness=0,
        )
        # my_cavas.config(bg='#000000')
        my_cavas.pack(side=LEFT, fill=BOTH, expand=0)
        my_scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=my_cavas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)
        my_cavas.configure(yscrollcommand=my_scrollbar.set)
        my_cavas.bind(
            "<Configure>",
            lambda e: my_cavas.configure(scrollregion=my_cavas.bbox("all")),
        )
        second_frame = Frame(my_cavas)
        my_cavas.create_window((0, 0), window=second_frame, anchor="nw")

        self.tk_textbox = Table(second_frame, items=self.data)
        self.tk_textbox.grid(row=0, column=0, sticky="nsew")
