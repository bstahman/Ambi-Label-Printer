from label_generator import *
from print_pdf import *
import os
import asyncio
import websockets
import json
import logging

DYMO_WHITE_LABEL_PRINTER_NAME = 'KANBAN DYMO'
DYMO_GREEN_LABEL_PRINTER_NAME = 'KANBAN DYMO'

async def handler(websocket):

    async for message in websocket:

        try:

            request = json.loads(message)

            label_file = generate_labels(request)

            if request["Label Type"] == 'Kanban':

                print_pdf(label_file, DYMO_GREEN_LABEL_PRINTER_NAME)

            else:

                print_pdf(label_file, DYMO_WHITE_LABEL_PRINTER_NAME)

            await websocket.send('SUCCESS')

            await websocket.close()

        except Exception as e:

            await websocket.send('FAILURE')

            logging.error(str(e))

            await websocket.close()


async def main():

    async with websockets.serve(handler, "localhost", 8765):

        await asyncio.Future()

if __name__ == '__main__':

    asyncio.run(main())

