# Test run of Bleak
# https://github.com/hbldh/bleak?tab=readme-ov-file#usage

import asyncio
from bleak import BleakScanner

async def main():
    devices = await BleakScanner.discover()
    if devices:
        for d in devices:
            print(d.address, d.name, d.details.RSSI)
    else:
        print("No BLE Devices found.")

asyncio.run(main())