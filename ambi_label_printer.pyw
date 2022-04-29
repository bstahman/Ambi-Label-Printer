from label_generator import *
from print_pdf import *
import os
import asyncio
import websockets
import json
import logging

DYMO_WHITE_LABEL_PRINTER_NAME = 'DYMO LabelWriter 4XL WHITE'
DYMO_GREEN_LABEL_PRINTER_NAME = 'DYMO LabelWriter 4XL GREEN'

async def handler(websocket):

    async for message in websocket:

        try:

            request = json.loads(message)

            generate_labels(request)

            print(request)

            if request["Label Type"] == 'Kanban':

                print_pdf('labels.pdf', DYMO_GREEN_LABEL_PRINTER_NAME)

            else:

                print_pdf('labels.pdf', DYMO_WHITE_LABEL_PRINTER_NAME)

            await websocket.send('SUCCESS')

            await websocket.close()

        except Exception as e:

            print(e)

            await websocket.send('FAILURE')

            logging.error(str(e))

            await websocket.close()


async def main():

    logging.basicConfig(filename='logs.log', format='%(asctime)s %(message)s', level=logging.DEBUG)

    async with websockets.serve(handler, "localhost", 8765):

        await asyncio.Future()

if __name__ == '__main__':

    asyncio.run(main())

