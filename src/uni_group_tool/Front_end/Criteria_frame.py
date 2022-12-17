import customtkinter


class CriteriaFrame(customtkinter.CTkFrame):
    def __init__(self, *args, type_to_make, criteria_data, **kwargs):
        super().__init__(*args, **kwargs)
        self.type_to_make = type_to_make
        self.criteria_data = criteria_data
        self.type_to_make = type_to_make
        if type_to_make[0] == "diversity":
            self.checkbox = customtkinter.CTkCheckBox(master=self, text=type_to_make[1], onvalue="on", offvalue="off",
                                                      command=self.update_criteria_diversity)
            self.checkbox.grid(row=0, column=0, padx=10, pady=10)
            self.label = customtkinter.CTkLabel(master=self,
                                                text="Priority",
                                                width=40,
                                                height=25,
                                                corner_radius=8)
            self.label.grid(row=0, column=1, padx=10, pady=10)
            self.priority = customtkinter.CTkSegmentedButton(master=self,
                                                             values=["Very low", "Low", "Medium", "High", "Very high"])
            self.priority.grid(row=0, column=2, padx=10, pady=10)
        if type_to_make[0] == "types_together":
            self.label1 = customtkinter.CTkLabel(master=self,
                                                 text=type_to_make[1],
                                                 width=40,
                                                 height=25,
                                                 corner_radius=8)
            self.label1.grid(row=0, column=0, padx=10, pady=10)
            self.combobox = customtkinter.CTkComboBox(master=self, command=self.update_criteria_together,
                                                      values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])

            self.combobox.grid(row=0, column=1, padx=10, pady=10)
            self.label2 = customtkinter.CTkLabel(master=self,
                                                 text="Priority",
                                                 width=40,
                                                 height=25,
                                                 corner_radius=8)
            self.label2.grid(row=0, column=2, padx=10, pady=10)
            self.priority = customtkinter.CTkSegmentedButton(master=self,
                                                             values=["Very low", "Low", "Medium", "High", "Very high"])
            self.priority.grid(row=0, column=3, padx=10, pady=10)
        if type_to_make[0] == "groups":
            self.groups = customtkinter.CTkSegmentedButton(master=self,
                                                           values=["Minimum group size", "Minimum amount of groups"])
            self.groups.grid(row=0, column=0, padx=10, pady=10)
            self.value = customtkinter.CTkComboBox(master=self,
                                                   values=[str(i) for i in range(1, 31)])
            self.value.grid(row=0, column=1, padx=10, pady=10)

    def update_criteria_diversity(self):
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
