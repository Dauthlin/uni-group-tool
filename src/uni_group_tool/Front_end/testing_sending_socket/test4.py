import tkinter as tk
import asyncio

import customtkinter

import subprocess
import sys
import json



class App:
    async def exec(self):
        self.window = Window(asyncio.get_event_loop())
        await self.window.show();


class Window(tk.Tk):
    def __init__(self, loop):
        self.loop_count = None
        self.loop = loop
        self.root = tk.Tk()
        self.label = customtkinter.CTkLabel(master=self.root, text="CTkLabel")
        self.label.grid(row=0, column=0, sticky=tk.W, padx=8, pady=8)
        button_block = tk.Button(text="Calculate Sync", width=10, command=self.calculate_sync)
        button_block.grid(row=2, column=0, sticky=tk.W, padx=8, pady=8)
        button_non_block = tk.Button(text="Calculate Async", width=10, command=lambda: self.loop.create_task(self.calculate_async()))
        button_non_block.grid(row=2, column=1, sticky=tk.W, padx=8, pady=8)

    async def show(self):
        while True:
            #self.label["text"] = self.animation
            #self.animation = self.animation[1:] + self.animation[0]
            self.label.configure(text=self.loop_count)
            self.root.update()
            await asyncio.sleep(.1)

    def calculate_sync(self):
        max = 3000000
        for i in range(1, max):
            self.progressbar["value"] = i / max * 100


    async def calculate_async(self):
        json_data = {
                    "size_of_teams": 8,
                    "shuffle": True,
                    "criteria": {
                        "diversity": ["average", "gender"],
                        "amount_to_be_together": [
                            ["gender", "F", 2],
                            ["home", "O", 2]
                        ],
                        "specific_teams": [
                            [
                                ["208026943", 3],
                                ["208063956", 3],
                                ["207069131", 4]
                            ]
                        ]
                    },
                    "weights": {},
                    "data_path": "test_data/sample.csv",
                    "debugging": False,
                    "saving": True
                }

        async for path in self.execute(json_data):
            self.loop_count = (path)

    async def execute(self,json_data):
        popen = subprocess.Popen([sys.executable, "Run_app.py",json.dumps(json_data) ],
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True)
        for stdout_line in iter(popen.stdout.readline, ""):
            yield stdout_line
            await asyncio.sleep(1)
        popen.stdout.close()


        # Example


        # print(type(p.stdout))
        # while p.poll() is None:
        #     await asyncio.sleep(0)
        #     if len(select.select([p.stdout], [], [], 0)[0]) > 0:
        #         print(p.stdout)


asyncio.run(App().exec())