from tkinter import *
from tkinter import messagebox
import asyncio
from async_tkinter_loop import async_handler, async_mainloop
import threading
import random

async def say_after(string):
    while True:
        await asyncio.sleep(1)
        print(string)

async def do_urls1():
    """ Creating and starting 10 tasks. """
    task2 = asyncio.create_task(
        say_after("hello"))
    task1 = asyncio.create_task(
        say_after("goodbye"))
    await task1
    await task2

def do_urls():
    do_urls1()
def do_freezed():
    messagebox.showinfo(message='Tkinter is reacting.')


async def main():
    root = Tk()
    Button(master=root, text='Asyncio Tasks', command=lambda:  async_handler(do_urls1))
    Button(master=root, text='Freezed???', command=do_freezed).pack()
    async_mainloop(root)


asyncio.run(main())