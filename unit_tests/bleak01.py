# Test run of Bleak
# https://github.com/hbldh/bleak?tab=readme-ov-file#usage

import asyncio
from bleak import BleakScanner

async def main():
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)

asyncio.run(main())