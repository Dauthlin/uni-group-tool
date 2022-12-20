import ast
import time

import websocket
import asyncio


class Send_data():


    def __init__(self):
        # self.event = None
        # self.ws = websocket.WebSocketApp("ws://127.0.0.1:5000/run_program")
        priunt
    async def test(self):
        print("waiting")
        #await self.event.wait()
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
        #print(type(self.ws))
        await self.ws.send(json_data)
        response = await self.ws.recv()
        response = ast.literal_eval(response)
        while response.get("complete") is not True:
            print(response)
            response = await self.ws.recv()
            response = ast.literal_eval(response)

    async def periodic_b(self):
        #self.event.set()
        self.ws.run_forever()


    async def main(self):
        # self.event = asyncio.Event()
        # periodic_a_task = asyncio.create_task(self.test())
        # periodic_b_task = asyncio.create_task(self.periodic_b())
        # await asyncio.gather(periodic_a_task, periodic_b_task)
        print('Hello ...')
        await asyncio.sleep(1)
        print('... World!')


if __name__ == "__main__":
    app = Send_data()
    asyncio.run(app.main())
    #asyncio.get_event_loop().run_until_complete(test())
