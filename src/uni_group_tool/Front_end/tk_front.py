import json
import copy
from tkinter.filedialog import askopenfilename
import customtkinter
from uni_group_tool.main import run, get_csv, get_csv_table_students
from Criteria_frame import CriteriaFrame
from Criteria_storage import CriteriaStorage
from Treeview_table import TreeViewTable
from all_data_to_send import AllDataToSend
from Processing import processing
from tkinter import Tk, Label, X, Frame, Y, TOP, BOTH,LEFT,BOTTOM
from websocket import *
class App_front(customtkinter.CTk):
    def Run_program(self):
        for i in run(self.all_data.criteria,int(self.all_data.size_of_teams),self.all_data.shuffle,self.all_data.weights,self.all_data.data_path,self.all_data.debugging,self.all_data.saving):
            print(i)
            self.result = i
    def run_event(self):
        specific_teams = []
        for line in self.table.tree.get_children():
            if self.table.tree.item(line)['values'][2] != "":
                specific_teams.append([str(self.table.tree.item(line)['values'][0]),self.table.tree.item(line)['values'][2]])
        specific_teams = [specific_teams]
        self.criteria_data.set_specific_teams(specific_teams)

        criteria = copy.deepcopy(self.criteria_data.get_all())
        criteria["amount_to_be_together"]["home"]['H'] = criteria["amount_to_be_together"]["home"]["Home"]
        del criteria["amount_to_be_together"]["home"]["Home"]
        criteria["amount_to_be_together"]["home"]['O'] = criteria["amount_to_be_together"]["home"]["Online"]
        del criteria["amount_to_be_together"]["home"]["Online"]
        criteria["amount_to_be_together"]["Gender"]["F"] = criteria["amount_to_be_together"]["Gender"]["Female"]
        del criteria["amount_to_be_together"]["Gender"]["Female"]
        criteria["amount_to_be_together"]["Gender"]["M"] = criteria["amount_to_be_together"]["Gender"]["Male"]
        del criteria["amount_to_be_together"]["Gender"]["Male"]
        criteria["amount_to_be_together"]["gender"] = criteria["amount_to_be_together"]["Gender"]
        del criteria["amount_to_be_together"]["Gender"]

        diversity = criteria['diversity']
        store = []
        for i in diversity:
            if diversity[i]:
                store.append(i)
        criteria['diversity'] = store
        amount_to_be_together = criteria['amount_to_be_together']
        store = []
        for i in amount_to_be_together:
            for j in amount_to_be_together[i]:
                if amount_to_be_together[i][j] is not None:
                    store.append([i,j,int(amount_to_be_together[i][j])])
        criteria['amount_to_be_together'] = store
        self.all_data.set_criteria(criteria)
        self.Run_program()



    def file_explorer(self):
        path = askopenfilename()
        self.data = get_csv_table_students(path)
        if hasattr(self, 'table'):
            self.table.destroy()
        self.table = TreeViewTable(self, items=self.data)
        self.table.pack(side=TOP,pady=self.pad_ammount)
        self.all_data.set_data_path(path)

        #self.scroll_bar.config(command=self.table.yview)
    def __init__(self):
        super().__init__()
        self.all_data = AllDataToSend()
        self.framed_table = None
        self.data = None
        self.pad_ammount = 5
        #self.tk.call('tk','scaling',5.0)
        self.title("Group creation tool")
        #setting fonts
        self.title_font = customtkinter.CTkFont(size=35)
        self.sub_title_font = customtkinter.CTkFont(size=30)
        self.sub_sub_title_font = customtkinter.CTkFont(size=20)

        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        self.criteria_data = CriteriaStorage()
        self.row_count = 0
        title = customtkinter.CTkLabel(master=self, text="Group creation tool", font=self.title_font)
        title.pack(side=TOP,pady=self.pad_ammount)
        self.row_count += 1
        self.file = customtkinter.CTkButton(master=self, text="Import Students file", command=self.file_explorer)
        self.file.pack(side=TOP,pady=self.pad_ammount)
        self.row_count += 1
        # set group size
        self.groups = CriteriaFrame(self, type_to_make=["groups"], criteria_data=self.all_data)
        self.groups.pack(side=TOP,pady=self.pad_ammount)
        self.row_count += 1
        # set diversity
        subtitle = customtkinter.CTkLabel(master=self, text="Criteria", font=self.sub_title_font)
        subtitle.pack(side=TOP,pady=self.pad_ammount)
        self.row_count += 1
        subtitle = customtkinter.CTkLabel(master=self, text="Diversity", font=self.sub_sub_title_font)
        subtitle.pack(side=TOP,pady=self.pad_ammount)
        self.row_count += 1
        # set types to be together
        self.criteria_diversity = [
            CriteriaFrame(self, type_to_make=("diversity", "average"), criteria_data=self.criteria_data),
            CriteriaFrame(self, type_to_make=("diversity", "home"), criteria_data=self.criteria_data),
            CriteriaFrame(self, type_to_make=("diversity", "gender"), criteria_data=self.criteria_data)]
        for i in range(self.row_count, self.row_count + len(self.criteria_diversity)):
            self.criteria_diversity[i - self.row_count].pack(side=TOP,pady=self.pad_ammount)


        subtitle = customtkinter.CTkLabel(master=self, text="Types that should be together", font=self.sub_sub_title_font)
        subtitle.pack(side=TOP,pady=self.pad_ammount)


        self.criteria_together= [CriteriaFrame(self, type_to_make=("types_together", ("Gender", "Male")),
                                                 criteria_data=self.criteria_data),
                                   CriteriaFrame(self, type_to_make=("types_together", ("Gender", "Female")),
                                                 criteria_data=self.criteria_data),
                                   CriteriaFrame(self, type_to_make=("types_together", ("home", "Home")),
                                                 criteria_data=self.criteria_data),
                                   CriteriaFrame(self, type_to_make=("types_together", ("home", "Online")),
                                                 criteria_data=self.criteria_data)]

        for i in range(self.row_count, self.row_count + len(self.criteria_together)):
            self.criteria_together[i - self.row_count].pack(side=TOP,pady=self.pad_ammount)
        self.row_count_marker = self.row_count

        #self.student_teams = SpecificTeams(self)
        data=[['StudentID', 'username','team']]
        #self.student_teams.grid(row=self.row_count_marker, column=0, pady=self.pad_ammount0, pady=10)
        self.table = TreeViewTable(self, items=data)
        self.table.pack(side=TOP,pady=self.pad_ammount)
        self.button = customtkinter.CTkButton(master=self, text="Run", command=self.run_event)
        self.button.pack(side=BOTTOM, pady=self.pad_ammount)


if __name__ == "__main__":
    app = App_front()
    app.mainloop()

# if __name__ == '__main__':
#     customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
#     customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
#
#     app = customtkinter.CTk()  # create CTk window like you do with the Tk window
#     app.geometry("1280x720")
#     combobox = customtkinter.CTkComboBox(master=app,
#                                          values=["option 1", "option 2"],
#                                          command=combobox_callback)
#     combobox.grid(row=1, column=0, pady=self.pad_ammount0, pady=10)
#
#     combobox2 = customtkinter.CTkComboBox(master=app,
#                                           values=["option 1", "option 2"],
#                                           command=combobox_callback)
#     combobox2.grid(row=1, column=1, pady=self.pad_ammount0, pady=10)
#
#     app.mainloop()
