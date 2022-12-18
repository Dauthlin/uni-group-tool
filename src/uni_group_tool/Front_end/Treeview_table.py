import customtkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class SearchBox(customtkinter.CTkFrame):
    def __init__(self, *args,columns,tree, **kwargs):
        super().__init__(*args, **kwargs)
        self.tree = tree
        self.columns = columns
        self.default_search = 0
        self.search_ent_var = StringVar()
        self.search_by = customtkinter.CTkComboBox(master=self, values=self.columns,command=self.update_default_search)
        self.search_by.grid(row=0, column=0, sticky='ns')
        search_entry = customtkinter.CTkEntry(master=self, textvariable=self.search_ent_var)
        search_entry.grid(row=0, column=1, sticky='ns')
        self.search_ent_var.trace("w", self.filterStudentID)

    def update_default_search(self, *args):
        print(self.search_by.get())
        if self.search_by.get() == "StudentID":
            self.default_search = 0
        if self.search_by.get() == "username":
            self.default_search = 1
        if self.search_by.get() == "team":
            self.default_search = 2
    def filterStudentID(self, *args):
        ItemsTreeView = self.tree.get_children()
        search = self.search_ent_var.get().lower()
        for each_item in ItemsTreeView:
            if search in str(self.tree.item(each_item)['values'][self.default_search]):
                #print(self.tree.item(each_item)['values'][self.default_search])
                searchvar = self.tree.item(each_item)['values']
                self.tree.delete(each_item)
                self.tree.insert("",0,values=searchvar)

class TreeViewTable(customtkinter.CTkFrame):
    def __init__(self, *args,items, **kwargs):
        super().__init__(*args, **kwargs)

        self.entryPopup = None

        self.columns = items[0]
        self.tree = ttk.Treeview(self, columns=self.columns, show='headings')
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",background = self["bg"], foreground="#dce4ee",fieldbackground=self["bg"])
        style.map("Treeview",background=[("selected","#1f6aa5")])


        # define headings
        for i in items[0]:
            self.tree.heading(i, text=i)


        self.tree.bind("<Double-1>", self.onDoubleClick)

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=1, sticky='ns')
        search_box = SearchBox(self,columns=self.columns,tree=self.tree)
        search_box.grid(row=0, column=0, sticky='ns')


        # generate sample data
        # students = []
        # for n in items[1:]:
        #     students.append(n)

        # add data to the treeview
        for student in items[1:]:
            self.tree.insert('', tk.END, values=student)

        self.tree.grid(row=1, column=0, sticky='nsew')

    def onDoubleClick(self, event):
        # what row and column was clicked on
        region_clicked = self.tree.identify_region(event.x,event.y)
        if region_clicked not in "cell":
            return
        selected_id = self.tree.identify_row(event.y)
        column = self.tree.identify_column(event.x)
        column_index = int(column[1:]) -1
        if column_index != 2:
            return
        selected_values = self.tree.item(selected_id).get("values")[column_index]
        column_box = self.tree.bbox(selected_id,column)
        entry_edit = ttk.Entry(self,width=column_box[2])

        entry_edit.place(x=column_box[0],y=column_box[1]+28,w=column_box[2],h=column_box[3])
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