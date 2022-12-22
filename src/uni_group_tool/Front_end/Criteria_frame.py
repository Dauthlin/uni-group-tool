import customtkinter
from toop_tips import ToolTip
def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)

    def enter(event):
        toolTip.showtip(text)

    def leave(event):
        toolTip.hidetip()

    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)
class CriteriaFrame(customtkinter.CTkFrame):


    def __init__(self, *args, type_to_make, criteria_data,all_data =None, **kwargs):
        super().__init__(*args, **kwargs)
        self.all_data = all_data
        self.type_to_make = type_to_make
        self.criteria_data = criteria_data
        self.type_to_make = type_to_make
        if type_to_make[0] == "diversity":
            if type_to_make[1] == "home":
                temp_text = "location"
            else:
                temp_text = type_to_make[1]
            self.checkbox = customtkinter.CTkCheckBox(master=self, text=temp_text, onvalue="on", offvalue="off",
                                                      command=self.update_criteria_diversity)
            self.checkbox.grid(row=0, column=0, padx=10, pady=10)
            if temp_text == "average":
                CreateToolTip(self.checkbox,"This will attempt to diversify the students by their average score")
            if temp_text == "location":
                CreateToolTip(self.checkbox,"This will attempt to diversify the students by their location.\n for example it will try to mix students that are working online with students that are working on campus")
            if temp_text == "gender":
                CreateToolTip(self.checkbox,"This will attempt to diversify the students by their gender score\n for example it will try to mix students that are different genders together ")
            self.label = customtkinter.CTkLabel(master=self,
                                                text="Priority",
                                                width=40,
                                                height=25,
                                                corner_radius=8)
            self.label.grid(row=0, column=1, padx=10, pady=10)
            self.priority = customtkinter.CTkSegmentedButton(master=self,
                                                             values=["Very low", "Low", "Medium", "High", "Very high"],command=self.priority_update,state="disabled")
            self.priority.set("Medium")
            self.priority.grid(row=0, column=2, padx=10, pady=10)
        if type_to_make[0] == "types_together":
            if type_to_make[1][1] == "Home":
                temp_text = "Working on campus"
            elif type_to_make[1][1] == "Online":
                temp_text = "Working Online"
            else:
                temp_text = type_to_make[1][1]
            self.label1 = customtkinter.CTkLabel(master=self,
                                                 text=temp_text,
                                                 width=40,
                                                 height=25,
                                                 corner_radius=8)
            self.label1.grid(row=0, column=0, padx=10, pady=10)
            self.combobox = customtkinter.CTkComboBox(master=self, command=self.update_criteria_together,
                                                      values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])

            self.combobox.grid(row=0, column=1, padx=10, pady=10)
            if temp_text == "Male":
                CreateToolTip(self.label1, "This will attempt to group male students together\n This will try to enforce that at least N male students are together in a group ")
            if temp_text == "Female":
                CreateToolTip(self.label1, "This will attempt to group Female students together\n This will try to enforce that at least N Female students are together in a group ")
            if temp_text == "Working on campus":
                CreateToolTip(self.label1, "This will attempt to group students that are working on campus together\n This will try to enforce that at least N students on campus are together in a group ")
            if temp_text == "Working Online":
                CreateToolTip(self.label1, "This will attempt to group students that are working Online together\n This will try to enforce that at least N students that are working online in a group ")
            self.label2 = customtkinter.CTkLabel(master=self,
                                                 text="Priority",
                                                 width=40,
                                                 height=25,
                                                 corner_radius=8)
            self.label2.grid(row=0, column=2, padx=10, pady=10)
            self.priority = customtkinter.CTkSegmentedButton(master=self,
                                                             values=["Very low", "Low", "Medium", "High", "Very high"],command=self.priority_update)
            self.priority.set("Medium")
            self.priority.grid(row=0, column=3, padx=10, pady=10)
        if type_to_make[0] == "groups":
            self.groups = customtkinter.CTkSegmentedButton(master=self,
                                                           values=["Minimum group size", "Minimum amount of groups"],
                                                           command=self.segmented_button_callback)

            self.groups.grid(row=0, column=0, padx=10, pady=10)
            self.groups.set("Minimum group size")
            self.value = customtkinter.CTkComboBox(master=self,
                                                   values=[str(i) for i in range(2, 31)],
                                                   command=self.update_set_size_of_teams)
            self.value.grid(row=0, column=1, padx=10, pady=10)

    def priority_update(self,data):
        for (i,j) in zip((0.2,.4,.6,.8,1),["Very low", "Low", "Medium", "High", "Very high"]):

            if j == self.priority.get():
                if isinstance(self.type_to_make[1], tuple):
                    temp = self.type_to_make[1][1][0]
                    self.all_data.set_weights(temp, i)
                else:
                    self.all_data.set_weights(self.type_to_make[1],i)

        print(self.all_data.get_all())

    def segmented_button_callback(self,value):
        if value == "Minimum group size":
            self.criteria_data.set_min_group_size_or_amount_of_groups(True)
        else:
            self.criteria_data.set_min_group_size_or_amount_of_groups(False)
    def update_set_size_of_teams(self, data):
        self.criteria_data.set_size_of_teams(self.value.get())

    def update_criteria_diversity(self):
        if self.checkbox.get() == "on":
            self.priority.configure(state="normal")
        else:
            self.priority.configure(state="disabled")
        self.criteria_data.set_diversity(self.type_to_make[1])

    def update_criteria_together(self, data):
        self.criteria_data.set_should_be_together(self.type_to_make[1][0], self.type_to_make[1][1], self.combobox.get())
    # def add_first_box(self, data):
    #     if self.combobox.get() == "diversity":
    #         print("diversity", self.combobox3)
    #         self.combobox2 = customtkinter.CTkComboBox(master=self,
    #                                                    values=["gender", "home", "average"])
    #         self.combobox2.grid(row=1, column=1, padx=10, pady=10)
    #     if self.combobox.get() == "amount_to_be_together":
    #         print("amount_to_be_together", self.combobox3)
    #         self.add_second_box("test")
    #         self.combobox2 = customtkinter.CTkComboBox(master=self,
    #                                                    command=self.add_second_box,
    #                                                    values=["gender", "home"])
    #         self.combobox2.grid(row=1, column=1, padx=10, pady=10)
    #
    #
    # def add_second_box(self, data):
    #     if self.combobox.get() == "amount_to_be_together":
    #         self.combobox3 = customtkinter.CTkComboBox(master=self,
    #                                                    values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
    #         self.combobox3.grid(row=1, column=2, padx=10, pady=10)
