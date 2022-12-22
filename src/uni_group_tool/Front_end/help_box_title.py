
import customtkinter
from toop_tips import ToolTip
from tkinter import TOP,LEFT,RIGHT
from tkinter.filedialog import asksaveasfilename
import csv
def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)

    def enter(event):
        toolTip.showtip(text)

    def leave(event):
        toolTip.hidetip()

    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


class helpBox(customtkinter.CTkFrame):
    def file_explorer_saving(self):
        file = asksaveasfilename(defaultextension=".csv")
        #print(type(self.items_store[0]),self.items_store[0])
        items_store = [{'StudentID':"", 'username':"", 'surname':"",'firstName':"",'gender':"",'home':"",'average':"",'team':"",'status':""}]
        keys =items_store[0].keys()
        with open(file, 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)  # type: ignore
            dict_writer.writeheader()

    def __init__(self, *args,size,text,help_text,button=False, **kwargs):
        super().__init__(*args, **kwargs)

        if not button:
            title = customtkinter.CTkLabel(master=self, text=text, font=customtkinter.CTkFont(size=size))
            title.pack(side=LEFT, pady=3)
            help = customtkinter.CTkLabel(master=self, text="ⓘ")
            help.pack(side=LEFT, pady=3,padx=20)
            CreateToolTip(help, help_text)
        else:
            file = customtkinter.CTkButton(master=self, text="save Student file template",
                                                command=self.file_explorer_saving)
            file.pack(side=LEFT, pady=3)
            help = customtkinter.CTkLabel(master=self, text="ⓘ")
            help.pack(side=LEFT, pady=3, padx=20)
            CreateToolTip(help, help_text)