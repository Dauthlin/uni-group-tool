import asyncio
import websockets
import time
import ast

current_response = {}


async def test(ws):
    global current_response
    print("waiting")
    # await self.event.wait()
    json_data = """{
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
    }"""
    # print(type(self.ws))
    await ws.send(json_data)
    response = await ws.recv()
    response2 = ast.literal_eval(response)
    while response2.get("complete") is not True:
        response = await ws.recv()
        response2 = ast.literal_eval(response)

        current_response = response2


async def say_after():
    while current_response.get("complete") is not True:
        await asyncio.sleep(1)
        print(current_response.get("loop"))


async def main():
    # ws = websocket.WebSocketApp("ws://127.0.0.1:5000/run_program")
    async with websockets.connect("ws://127.0.0.1:5000/run_program") as ws:
        task1 = asyncio.create_task(test(ws))

        task2 = asyncio.create_task(say_after())

        print(f"started at {time.strftime('%X')}")

        # Wait until both tasks are completed (should take
        # around 2 seconds.)
        await task1
        await task2
        # await asyncio.gather(task1, task2)
        print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
