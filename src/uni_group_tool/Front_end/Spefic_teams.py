import customtkinter
from table import Table
from ScrollBar_On_Table import AddScrollbar
from Treeview_table import TreeViewTable
import tkinter as tk
from tkinter import ttk


class SpecificTeams(customtkinter.CTkFrame):
    def __init__(self, *args, items, **kwargs):
        super().__init__(*args, **kwargs)

        self.box = TreeViewTable(self, items=items)
        self.box.grid(row=0, column=0, padx=20, pady=10)

    # def __init__(self):
    #     super().__init__()
    #     # print(len(data))
    #     # if hasattr(self, 'table'):
    #     #     self.table.destroy()
    #     self.table = TreeViewTable(self)
    #     self.table.grid(row=0, column=0, padx=20, pady=10)
    #     # if len(data) < 6:
    #     #     self.table = Table(self, items=data)
    #     #     self.table.grid(row=0, column=0, padx=20, pady=10)
    #     # else:
    #     #     self.table = AddScrollbar(self, data=data)
    #     #     self.table.grid(row=0, column=0, padx=20, pady=10)
