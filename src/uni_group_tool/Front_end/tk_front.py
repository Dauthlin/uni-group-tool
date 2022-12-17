from tkinter.filedialog import askopenfilename
import customtkinter
from Criteria_frame import CriteriaFrame
from Criteria_storage import CriteriaStorage
from table import Table


class App(customtkinter.CTk):
    def button_event(self):
        print(self.criteria_data.get_all())
        print(self.path)

    def file_explorer(self):
        self.path = askopenfilename()

    def __init__(self):
        super().__init__()
        self.path = None

        #setting fonts
        self.title_font = customtkinter.CTkFont(size=35)
        self.sub_title_font = customtkinter.CTkFont(size=30)
        self.sub_sub_title_font = customtkinter.CTkFont(size=20)

        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        #self.geometry("1920x1080")
        self.title("Group creation tool")
        self.criteria_data = CriteriaStorage()
        self.row_count = 0
        title = customtkinter.CTkLabel(master=self, text="Group creation tool", font=self.title_font)
        title.grid(row=self.row_count, column=0, padx=20, pady=10)
        self.row_count += 1
        self.file = customtkinter.CTkButton(master=self, text="Import Students file", command=self.file_explorer)
        self.file.grid(row=self.row_count, column=0, padx=20, pady=10)
        self.row_count += 1
        # set group size
        self.groups = CriteriaFrame(self, type_to_make=["groups"], criteria_data=self.criteria_data)
        self.groups.grid(row=self.row_count, column=0, padx=20, pady=10)
        self.row_count += 1
        # set diversity
        subtitle = customtkinter.CTkLabel(master=self, text="Criteria", font=self.sub_title_font)
        subtitle.grid(row=self.row_count, column=0, padx=20, pady=10)
        self.row_count += 1
        subtitle = customtkinter.CTkLabel(master=self, text="Diversity", font=self.sub_sub_title_font)
        subtitle.grid(row=self.row_count, column=0, padx=20, pady=10)
        self.row_count += 1
        # set types to be together
        self.criteria_diversity = [
            CriteriaFrame(self, type_to_make=("diversity", "average"), criteria_data=self.criteria_data),
            CriteriaFrame(self, type_to_make=("diversity", "home"), criteria_data=self.criteria_data),
            CriteriaFrame(self, type_to_make=("diversity", "gender"), criteria_data=self.criteria_data)]
        for i in range(self.row_count, self.row_count + len(self.criteria_diversity)):
            self.criteria_diversity[i - self.row_count].grid(row=i, column=0, padx=20, pady=10)
        self.row_count += len(self.criteria_diversity)

        subtitle = customtkinter.CTkLabel(master=self, text="Types that should be together", font=self.sub_sub_title_font)
        subtitle.grid(row=self.row_count, column=0, padx=20, pady=10)
        self.row_count += 1

        self.criteria_together= [CriteriaFrame(self, type_to_make=("types_together", ("Gender", "Male")),
                                                 criteria_data=self.criteria_data),
                                   CriteriaFrame(self, type_to_make=("types_together", ("Gender", "Female")),
                                                 criteria_data=self.criteria_data),
                                   CriteriaFrame(self, type_to_make=("types_together", ("home", "Home")),
                                                 criteria_data=self.criteria_data),
                                   CriteriaFrame(self, type_to_make=("types_together", ("home", "Online")),
                                                 criteria_data=self.criteria_data)]

        for i in range(self.row_count, self.row_count + len(self.criteria_together)):
            self.criteria_together[i - self.row_count].grid(row=i, column=0, padx=20, pady=10)
        self.row_count += len(self.criteria_together)
        self.button = customtkinter.CTkButton(master=self, text="CTkButton", command=self.button_event)
        self.button.grid(row=self.row_count, column=0, padx=20, pady=10)
        self.row_count += 1

        self.items = [(1, 'Raj', 'Mumbai', 19),
                      (2, 'Aaryan', 'Pune', 18),
                      (3, 'Vaishnavi', 'Mumbai', 20),
                      (4, 'Rachna', 'Mumbai', 21),
                      (5, 'Shubham', 'Delhi', 21)]

        self.table = Table(self, items=self.items)
        self.table.grid(row=self.row_count, column=0, padx=20, pady=10)
        self.row_count += 1


if __name__ == "__main__":
    app = App()
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
#     combobox.grid(row=1, column=0, padx=10, pady=10)
#
#     combobox2 = customtkinter.CTkComboBox(master=app,
#                                           values=["option 1", "option 2"],
#                                           command=combobox_callback)
#     combobox2.grid(row=1, column=1, padx=10, pady=10)
#
#     app.mainloop()
