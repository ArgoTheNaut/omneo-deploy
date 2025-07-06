# Test run of Bleak
# https://github.com/hbldh/bleak?tab=readme-ov-file#usage

import asyncio
from bleak import BleakScanner

async def main():
    devices = await BleakScanner.discover()
    if devices:
        for d in devices:
            details = d.details['props']
            mfData = details['ManufacturerData'] if "ManufacturerData" in details else "No data"
            print(d.address, d.name, details['RSSI'], details['UUIDs'], mfData)
    else:
        print("No BLE Devices found.")

asyncio.run(main())