import customtkinter, tkinter
from ScrollBar_On_Table import AddScrollbar


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.box = AddScrollbar(self)
        self.box.grid(row=0, column=0, padx=20, pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()