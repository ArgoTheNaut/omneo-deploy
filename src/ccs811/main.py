import time
import board
import busio
import adafruit_ccs811
import requests

# Set up the sensor
i2c_bus = busio.I2C(board.SCL, board.SDA)
ccs811 = adafruit_ccs811.CCS811(i2c_bus)

restarts = 0
posts_since_restart = 0

# Load the auth key to the web server at this file path
auth_key_path = "/var/data/dht11/auth.omneo"
with open(auth_key_path, "r") as file:
    auth_key = file.readline().strip()

awaiting_ready_sec = 0
while not ccs811.data_ready:
    print(f"Awaiting ready. t={awaiting_ready_sec}")
    awaiting_ready_sec += 1
    time.sleep(1)

while True:
    try:
        print("CO2: %1.0f PPM" % ccs811.eco2)
        print("TVOC: %1.0f PPM" % ccs811.tvoc)

        url = "https://argus-lab.org/api/data/ccs811"    # Upload back up to your own locally hosted web server for forwarding to db
        requests.post(url, json = {
            "eco2": ccs811.eco2,
            "tvoc": ccs811.tvoc,
            "restarts": restarts,
            "posts_since_restart": posts_since_restart
        }, headers={
            "omneoAuth": auth_key
        })

    except Exception as error:
        print(f"Request failed with exception {error} | Resetting sensor")
        ccs811.reset()
        i2c_bus = busio.I2C(board.SCL, board.SDA)
        ccs811 = adafruit_ccs811.CCS811(i2c_bus)
        restarts += 1
        posts_since_restart = 0

    print("5-minute cooldown")
    time.sleep(60 * 5)   # wait 5 mins between data points
    posts_since_restart += 1
