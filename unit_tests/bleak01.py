# Test run of Bleak
# https://github.com/hbldh/bleak?tab=readme-ov-file#usage

import asyncio
from bleak import BleakScanner

def sortMethod(e):
    return e.address

async def main():
    devices = await BleakScanner.discover()
    if devices:
        devices.sort(key=sortMethod)
        for d in devices:
            details = d.details["props"]

            mfData = "No data"
            if "ManufacturerData" in details:
                mfData = details["ManufacturerData"]
                mfData = str(mfData[list(mfData.keys())[0]])

            print(d.address, d.name, " " * (20 - len(d.name)), "\t", details["RSSI"], details["UUIDs"], mfData)
    else:
        print("No BLE Devices found.")


asyncio.run(main())
