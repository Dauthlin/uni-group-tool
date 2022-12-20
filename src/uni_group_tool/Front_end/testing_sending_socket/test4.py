import tkinter as tk
from tkinter import ttk
import asyncio
from uni_group_tool.main import groups_to_csv, run
import subprocess
import sys
import json
import select
import os
from contextlib import contextmanager


class App:
    async def exec(self):
        self.window = Window(asyncio.get_event_loop())
        await self.window.show();


class Window(tk.Tk):
    def __init__(self, loop):
        self.loop = loop
        self.root = tk.Tk()
        self.animation = "░▒▒▒▒▒"
        self.label = tk.Label(text="")
        self.label.grid(row=0, columnspan=2, padx=(8, 8), pady=(16, 0))
        self.progressbar = ttk.Progressbar(length=280)
        self.progressbar.grid(row=1, columnspan=2, padx=(8, 8), pady=(16, 0))
        button_block = tk.Button(text="Calculate Sync", width=10, command=self.calculate_sync)
        button_block.grid(row=2, column=0, sticky=tk.W, padx=8, pady=8)
        button_non_block = tk.Button(text="Calculate Async", width=10, command=lambda: self.loop.create_task(self.calculate_async()))
        button_non_block.grid(row=2, column=1, sticky=tk.W, padx=8, pady=8)

    async def show(self):
        while True:
            self.label["text"] = self.animation
            self.animation = self.animation[1:] + self.animation[0]
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

        p=subprocess.Popen([sys.executable, "Run_app.py",json.dumps(json_data) ],
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              stdin=subprocess.PIPE)
        print(type(p.stdout))
        while p.poll() is None:
            await asyncio.sleep(0)
            if len(select.select([p.stdout], [], [], 0)[0]) > 0:
                print(p.stdout)


asyncio.run(App().exec())