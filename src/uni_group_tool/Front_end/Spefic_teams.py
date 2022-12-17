import customtkinter
from table import Table
from ScrollBar_On_Table import AddScrollbar


class SpecificTeams(customtkinter.CTkFrame):
    def __init__(self, *args,data, **kwargs):
        super().__init__(*args, **kwargs)
        print(len(data))
        if hasattr(self, 'table'):
            self.table.destroy()
        if len(data) < 6:
            self.table = Table(self, items=data)
            self.table.grid(row=0, column=0, padx=20, pady=10)
        else:
            self.table = AddScrollbar(self, data=data)
            self.table.grid(row=0, column=0, padx=20, pady=10)
