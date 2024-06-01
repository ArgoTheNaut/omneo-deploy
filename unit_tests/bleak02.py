# Test run of Bleak
# https://github.com/hbldh/bleak?tab=readme-ov-file#usage

import asyncio
from bleak import BleakScanner, BleakClient

MODEL_NBR_UUID = "2A24"

async def main():
    devices = await BleakScanner.discover()
    for address in devices:
        async with BleakClient(address) as client:
            model_number = await client.read_gatt_char(MODEL_NBR_UUID)
            print("{1} Model Number: {0}".format("".join(map(chr, model_number)), address))

asyncio.run(main())
