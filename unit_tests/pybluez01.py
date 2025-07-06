# pip install pybluez

import bluetooth

print("Scanning for Bluetooth devices...")
nearby_devices = bluetooth.discover_devices(lookup_names=True)

if nearby_devices:
    print(f"Found {len(nearby_devices)} devices:")
    for addr, name in nearby_devices:
        print(f"  Address: {addr}, Name: {name if name else 'Unknown'}")
else:
    print("No Bluetooth devices found.")
