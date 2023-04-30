import customtkinter
import asyncio
import time


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("minimal example app")
        self.minsize(400, 300)

        self.button = customtkinter.CTkButton(master=self, command=self.button_callback)
        self.button.pack(padx=20, pady=20)

    def button_callback(self):
        print("button pressed")


async def say_after():
    while True:
        await asyncio.sleep(1)
        print("hello")


async def main():
    app = App()
    task1 = asyncio.create_task(app.mainloop())

    task2 = asyncio.create_task(say_after())

    # print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2


if __name__ == "__main__":
    async_loop = asyncio.get_event_loop()
    asyncio.run(main())
