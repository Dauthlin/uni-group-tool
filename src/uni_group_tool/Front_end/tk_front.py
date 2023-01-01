import copy
import os
from tkinter.filedialog import askopenfilename
import customtkinter
from uni_group_tool.main import run, get_csv, get_csv_table_students, groups_to_csv
from .Criteria_frame import CriteriaFrame
from .Criteria_storage import CriteriaStorage
from .Treeview_table import TreeViewTable
from .all_data_to_send import AllDataToSend
from tkinter import Tk, Label, X, Frame, Y, TOP,LEFT, BOTH,RIGHT,BOTTOM,N,NE
import asyncio
import subprocess
import sys
import json
from .help_box_title import helpBox
from.Run_app import run_main
import tempfile
import shutil

class App:
    async def exec(self):
        self.window = App_front(asyncio.get_event_loop())
        await self.window.show()





class App_front(customtkinter.CTk):



    async def show(self):
        while True:
            #self.label["text"] = self.animation
            #self.animation = self.animation[1:] + self.animation[0]
            data = self.loop_count
            #print(data)
            if data.get("loop") is not None:
                self.progressbar.start()
                print(data)
            elif data.get("answer") is not None:
                self.table_results.update_table(data.get("answer"))
                self.loop_count = json.loads('{"not started":0}')
                self.progressbar.stop()
                self.progressbar.set(0)
            else:
                self.progressbar.stop()
                self.progressbar.set(0)
            #self.progres_label.configure(text=self.loop_count)
            self.update()
            await asyncio.sleep(1/30)

    async def Run_program(self):
        async for path in self.execute(self.all_data):
            self.loop_count = path



    async def execute(self,data):

        dirpath = tempfile.mkdtemp()
        print(dirpath)
        data.set_result_path(os.path.join(dirpath ,'results.json'))
        popen = subprocess.Popen([sys.executable, "src/uni_group_tool/Front_end/Run_app.py",json.dumps(data.get_all()),dirpath ],
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True)
        await asyncio.sleep(2)
        f = open(data.get_result_path())
        result = json.load(f)
        f.close()

        while result.get("answer") is None:
            f = open(data.get_result_path())
            result = json.load(f)
            f.close()
            yield result
            await asyncio.sleep(1)
        #popen.stdout.close()
        shutil.rmtree(dirpath)


    async def run_event(self):
        self.button.configure(state="disabled")
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
        print(self.all_data.get_all())
        await self.Run_program()
        self.button.configure(state="enabled")

    def file_explorer(self):
        path = askopenfilename()
        self.data = get_csv_table_students(path)
        self.table.update_table(self.data)
        self.all_data.set_data_path(path)
        self.button.configure(state="enabled")

        #self.scroll_bar.config(command=self.table.yview)
    def __init__(self, loop):
        super().__init__()
        self.loop = loop
        self.loop_count = json.loads('{"not started":0}')
        self.all_data = AllDataToSend()
        self.framed_table = None
        self.data = None
        self.pad_ammount = 3


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


        self.table_results = TreeViewTable(self, items=[['StudentID', 'username', 'surname','firstName','gender','home','average','team','status']],title="results",row_size=75,height=42)
        self.table_results.pack(side=RIGHT, anchor=NE, pady=self.pad_ammount)
        self.row_count += 1
        self.file = customtkinter.CTkButton(master=self, text="Import Students file", command=self.file_explorer)
        self.file.pack(side=TOP,pady=self.pad_ammount)
        subtitle = helpBox(master=self, size=30, text="",button=True,
                           help_text="This is a template csv file you can use to enter your students information.\n"
                                     "StudentID is a string containing the students ID\n"
                                     "username is the students username\n"
                                     "surname is the students surname\n"
                                     "firstname is the students first name\n"
                                     "gender is the students gender M or F\n"
                                     "average is the students average mark out of 100\n"
                                     "team should be left blank or can contain a predetermined team that the student should be in\n"
                                     "status can be left blank")
        subtitle.pack(side=TOP, pady=self.pad_ammount)
        self.row_count += 1

        self.row_count += 1
        # set group size

        # set diversity
        # subtitle = customtkinter.CTkLabel(master=self, text="Criteria", font=self.sub_title_font)
        # subtitle.pack(side=TOP,pady=self.pad_ammount)
        subtitle = helpBox(master=self, size=30, text="Criteria", help_text="Select what criteria you would like to be active when generating your groups. \n For each criteria you can select a priority which will make that property more important ")
        subtitle.pack(side=TOP, pady=self.pad_ammount)
        self.row_count += 1
        self.groups = CriteriaFrame(self, type_to_make=["groups"], criteria_data=self.all_data)
        self.groups.pack(side=TOP, pady=self.pad_ammount)
        self.row_count += 1
        # subtitle = customtkinter.CTkLabel(master=self, text="Diversity", font=self.sub_sub_title_font)
        # subtitle.pack(side=TOP,pady=self.pad_ammount)
        subtitle = helpBox(master=self, size=20, text="Diversity", help_text="This criteria tells the program to try and diversify these attributes of the students.\n for example 'average' will try to create diverse groups with a large range of averages")
        subtitle.pack(side=TOP, pady=self.pad_ammount)


        self.row_count += 1
        # set types to be together
        self.criteria_diversity = [
            CriteriaFrame(self, type_to_make=("diversity", "average"), criteria_data=self.criteria_data, all_data=self.all_data),
            CriteriaFrame(self, type_to_make=("diversity", "home"), criteria_data=self.criteria_data, all_data=self.all_data),
            CriteriaFrame(self, type_to_make=("diversity", "gender"), criteria_data=self.criteria_data, all_data=self.all_data)]
        for i in range(self.row_count, self.row_count + len(self.criteria_diversity)):
            self.criteria_diversity[i - self.row_count].pack(side=TOP,pady=self.pad_ammount)


        # subtitle = customtkinter.CTkLabel(master=self, text="Types that should be together", font=self.sub_sub_title_font)
        # subtitle.pack(side=TOP,pady=self.pad_ammount)
        subtitle = helpBox(master=self, size=20, text="Types that should be together",
                           help_text="This criteria allows you to specify which types should be grouped together,\n"
                                     "for example you can specify that there should be at least 2 girls together in a group.\n "
                                     "This is used when you don't want specific types to be alone ")
        subtitle.pack(side=TOP, pady=self.pad_ammount)

        self.criteria_together= [CriteriaFrame(self, type_to_make=("types_together", ("Gender", "Male")),
                                                 criteria_data=self.criteria_data, all_data=self.all_data),
                                   CriteriaFrame(self, type_to_make=("types_together", ("Gender", "Female")),
                                                 criteria_data=self.criteria_data, all_data=self.all_data),
                                   CriteriaFrame(self, type_to_make=("types_together", ("home", "Home")),
                                                 criteria_data=self.criteria_data, all_data=self.all_data),
                                   CriteriaFrame(self, type_to_make=("types_together", ("home", "Online")),
                                                 criteria_data=self.criteria_data, all_data=self.all_data)]

        for i in range(self.row_count, self.row_count + len(self.criteria_together)):
            self.criteria_together[i - self.row_count].pack(side=TOP,pady=self.pad_ammount)
        self.row_count_marker = self.row_count


        subtitle2 = helpBox(master=self, size=20, text="Select which students should be in specific teams",
                           help_text="Once you have imported a student list using the button at the top of the page,\n you can specify which students you want to be in a specific team.\n"
                                     "to do this double click in the team cell of the student you would like to set the team for. \n"
                                     "if you cannot find the student use the search box above to sort through the results ")
        subtitle2.pack(side=TOP, pady=self.pad_ammount)


        self.table = TreeViewTable(self, items=[['StudentID', 'username','team']],row_size=200,title=None,height=10)
        self.table.pack(side=TOP,pady=self.pad_ammount)
        self.progressbar = customtkinter.CTkProgressBar(master=self, mode="indeterminate", width=400)
        self.progressbar.pack(side=TOP, pady=self.pad_ammount)
        self.button = customtkinter.CTkButton(master=self, text="Run", command= lambda: self.loop.create_task(self.run_event()))
        self.button.configure(state="disabled")
        self.button.pack(side=TOP, pady=self.pad_ammount)



def run_front_end():
    asyncio.run(App().exec())


if __name__ == "__main__":
    run_front_end()



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
