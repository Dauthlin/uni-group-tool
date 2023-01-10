import copy
import csv
import os

import customtkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename
import glob
from xlsxwriter.workbook import Workbook



class SearchBox(customtkinter.CTkFrame):
    def __init__(self, *args,columns,tree, **kwargs):
        super().__init__(*args, **kwargs)
        self.tree = tree
        self.column = columns
        self.columns = [col for col in columns if (col != "gender") and (col != "home")and (col != "average")and (col != "status") ]
        self.default_search = 0
        self.search_ent_var = StringVar()
        label = customtkinter.CTkLabel(master=self, text="Search for student")
        label.grid(row=0, column=0, sticky='ns',padx =10)
        self.search_by = customtkinter.CTkComboBox(master=self, values=self.columns,command=self.update_default_search)
        self.search_by.grid(row=0, column=1, sticky='ns')
        search_entry = customtkinter.CTkEntry(master=self, textvariable=self.search_ent_var)
        search_entry.grid(row=0, column=2, sticky='ns')
        self.search_ent_var.trace("w", self.filterStudentID)

    def update_default_search(self, *args):
        #print(self.search_by.get())
        for col in range(len(self.column)):
            if self.search_by.get() == self.column[col]:
                print(self.search_by.get(),  col)
                self.default_search = col

    def filterStudentID(self, *args):
        ItemsTreeView = self.tree.get_children()
        search = self.search_ent_var.get().lower()
        for each_item in ItemsTreeView:
            if search in (str(self.tree.item(each_item)['values'][self.default_search])).lower():
                #print(self.tree.item(each_item)['values'][self.default_search])
                searchvar = self.tree.item(each_item)['values']
                self.tree.delete(each_item)
                self.tree.insert("",0,values=searchvar)

class TreeViewTable(customtkinter.CTkFrame):
    def __init__(self, *args,items,title,row_size,height, **kwargs):
        super().__init__(*args, **kwargs)
        self.items_store = None
        self.height = height
        self.entryPopup = None
        #[['StudentID', 'username', 'surname','firstName','gender','home','average','status','team']]
        self.sub_title_font = customtkinter.CTkFont(size=30)
        self.highlight_gender = False
        self.highlight_location = False
        if title is not None:
            title2 = customtkinter.CTkLabel(master=self, text="Results", font=self.sub_title_font)
            title2.grid(row=0, column=0, sticky='ns')
            self.highlight_gender_button = customtkinter.CTkCheckBox(master=self, text="Highlight gender", onvalue="on", offvalue="off", command=self.toggle_highlighting_gender)
            self.highlight_gender_button.grid(row=3, column=0)
            self.highlight_location_button = customtkinter.CTkCheckBox(master=self, text="Highlight origin", onvalue="on", offvalue="off", command=self.toggle_highlighting_location)
            self.highlight_location_button.grid(row=4, column=0)
            file = customtkinter.CTkButton(master=self, text="save results as csv", command=self.file_explorer_saving)
            file.grid(row=5, column=0)

        self.columns = items[0]
        self.index = items[0].index('team')
        self.tree = ttk.Treeview(self, columns=self.columns, show='headings', height= self.height)
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",background = self["bg"], foreground="#dce4ee",fieldbackground=self["bg"])
        style.map("Treeview",background=[("selected","#1f6aa5")])
        for column in self.columns:
            self.tree.column(column, minwidth=50,width=row_size, stretch=True)


        # define headings
        for i in items[0]:
            self.tree.heading(i, text=i)


        self.tree.bind("<Double-1>", self.onDoubleClick)

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=2, column=1, sticky='ns')
        search_box = SearchBox(self,columns=self.columns,tree=self.tree)
        search_box.grid(row=1, column=0, sticky='ns')


        # generate sample data
        # students = []
        # for n in items[1:]:
        #     students.append(n)

        # add data to the treeview
        for student in items[1:]:
            self.tree.insert('', tk.END, values=student)

        self.tree.grid(row=2, column=0, sticky='nsew')

    def toggle_highlighting_gender(self):
        self.highlight_gender = not self.highlight_gender
        print(self.highlight_gender)

    def toggle_highlighting_location(self):
        self.highlight_location = not self.highlight_location
        print(self.highlight_location)


    def file_explorer_saving(self):
        file = asksaveasfilename(defaultextension=".csv")
        print(type(self.items_store[0]), self.items_store[0])
        keys = self.items_store[0].keys()
        with open(file, 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)  # type: ignore
            dict_writer.writeheader()
            dict_writer.writerows(self.items_store)  # type: ignore
        if self.highlight_location or  self.highlight_gender:
                workbook = Workbook(file[:-4] + '.xlsx')
                worksheet = workbook.add_worksheet()
                format1 = workbook.add_format({'bg_color': '#FFC7CE','font_color': '#9C0006'})
                format2 = workbook.add_format({'bg_color': '#C6EFCE','font_color': '#006100'})

                with open(file, 'rt', encoding='utf8') as f:
                    reader = csv.reader(f)
                    for r, row in enumerate(reader):
                        for c, col in enumerate(row):
                            worksheet.write(r, c, col)
                if self.highlight_location:
                    worksheet.conditional_format('F1:F1000', {'type': 'cell',
                                             'criteria': '==',
                                             'value': '"O"',
                                             'format': format1})
                if self.highlight_gender:
                    worksheet.conditional_format('E1:E1000', {'type': 'cell',
                                                              'criteria': '==',
                                                              'value': '"F"',
                                                              'format': format2})
                workbook.close()
                os.remove(file)

    def update_table(self,items):
        self.items_store = copy.deepcopy(items)
        self.tree.delete(*self.tree.get_children())
        #print(items)
        dict_list = []
        if isinstance(items[0], dict):
            for single_dict in items:
                temp = []
                for value in single_dict.values():
                    temp.append(value)
                dict_list.append(temp)
            for student in dict_list:
                self.tree.insert('', tk.END, values=student)
        else:
            for student in items[1:]:
                self.tree.insert('', tk.END, values=student)

    def onDoubleClick(self, event):
        # what row and column was clicked on
        region_clicked = self.tree.identify_region(event.x,event.y)
        if region_clicked not in "cell":
            return
        selected_id = self.tree.identify_row(event.y)
        column = self.tree.identify_column(event.x)
        column_index = int(column[1:]) -1
        if column_index != self.index:
            return
        selected_values = self.tree.item(selected_id).get("values")[column_index]
        column_box = self.tree.bbox(selected_id,column)
        entry_edit = ttk.Entry(self,width=column_box[2])
        if  self.height == 10:
            entry_edit.place(x=column_box[0],y=column_box[1]+28,w=column_box[2],h=column_box[3])
        else:
            entry_edit.place(x=column_box[0], y=column_box[1] + 65, w=column_box[2], h=column_box[3])
        entry_edit.editing_column_index = column_index
        entry_edit.editing_item_id = selected_id
        entry_edit.insert(0,selected_values)
        entry_edit.select_range(0,tk.END)
        entry_edit.focus()
        entry_edit.bind("<FocusOut>",self.completed)
        entry_edit.bind("<Return>",self.completed)

    def completed(self,event):
        users_text = event.widget.get()
        selected_id = event.widget.editing_item_id
        colum_index = event.widget.editing_column_index
        current_value = self.tree.item(selected_id).get("values")
        current_value[colum_index] = users_text
        if not users_text.isnumeric():
            event.widget.destroy()
            return
        self.tree.item(selected_id,values=current_value)
        event.widget.destroy()

if __name__ == "__main__":
    app = TreeViewTable()
    app.mainloop()