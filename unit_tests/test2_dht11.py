# Complete Project Details: https://RandomNerdTutorials.com/raspberry-pi-dht11-dht22-python/
# Based on Adafruit_CircuitPython_DHT Library Example

import time
import board
import adafruit_dht
import json
import requests

# Sensor data pin is connected to GPIO 4
# sensor = adafruit_dht.DHT22(board.D4)
# Uncomment for DHT11
sensor = adafruit_dht.DHT11(board.D14)

# Save the auth key to the web server at this file path
auth_key_path = "/var/data/dht11/auth.omneo"

with open(auth_key_path, "r") as file:
    auth_key = file.readline().strip()

while True:
    try:
        # Print the values to the serial port
        temperature_c = sensor.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = sensor.humidity
        print("Temp={0:0.1f}ºC, Temp={1:0.1f}ºF, Humidity={2:0.1f}%".format(temperature_c, temperature_f, humidity))

        url = "http://raspberrypi/api/consumers/dht11"    # Upload back up to your own locally hosted web server for forwarding to db
        requests.post(url, json = {
            "temperature": temperature_c,
            "humidity": humidity
        }, headers={
            "omneoAuth": auth_key
        })

        # with open("/var/data/dht11/out", "+a") as file:
        #     file.write(json.dumps({
        #         "temp":temperature_c,
        #         "humidity": humidity,
        #         "time": int(time.time() * 1000)  # JS-friendly ms since epoch
        #     }))
        #     file.write("\n")

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error

    time.sleep(60 * 5)   # wait 5 mins between data points
