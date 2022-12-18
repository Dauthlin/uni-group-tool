import customtkinter, tkinter
from ScrollBar_On_Table import AddScrollbar
from Treeview_table import TreeViewTable


class Test(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.box = TreeViewTable(self)
        self.box.grid(row=0, column=0, padx=20, pady=10)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.table = Test(self)
        self.table.grid(row=0, column=0, padx=20, pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()