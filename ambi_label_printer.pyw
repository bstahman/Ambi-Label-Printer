from label_generator import *
from print_pdf import *
import os
import asyncio
import websockets
import json

async def handler(websocket):

    async for message in websocket:

        request = json.loads(message)

        generate_labels(request)

        print_pdf('labels.pdf')


async def main():

    async with websockets.serve(handler, "localhost", 8765):

        print("listening...")

        await asyncio.Future()


if __name__ == '__main__':

    asyncio.run(main())

