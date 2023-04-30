import customtkinter


class Table(customtkinter.CTkFrame):
    def __init__(self, *args, items, **kwargs):
        super().__init__(*args, **kwargs)
        self.items = items
        self.total_rows = len(self.items)
        self.total_columns = len(self.items[0])
        for row in range(self.total_rows):
            for column in range(self.total_columns):
                self.label = customtkinter.CTkLabel(
                    master=self,
                    text=self.items[row][column],
                    width=60,
                    height=25,
                    corner_radius=10,
                )
                self.label.grid(row=row, column=column)
