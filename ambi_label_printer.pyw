from label_generator import *
from print_pdf import *
import os
import asyncio
import websockets
import json
import logging

async def handler(websocket):

    async for message in websocket:

        try:

            request = json.loads(message)

            generate_labels(request)

            print_pdf('labels.pdf')

            await websocket.send('SUCCESS')

        except Exception as e:

            await websocket.send('FAILURE')

            logging.error(str(e))


async def main():

    logging.basicConfig(filename='errors.log', format='%(asctime)s %(message)s', level=logging.ERROR)

    async with websockets.serve(handler, "localhost", 8765):

        await asyncio.Future()

if __name__ == '__main__':

    asyncio.run(main())

