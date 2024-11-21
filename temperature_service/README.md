# Room Temperature Monitoring Service

# Overview

This segment uses a DHT11 sensor on a Raspberry Pi 3B to track the temperature and humidity of a room.

# Instructions

1. On the Raspberry Pi, clone down the deployment repository and set up the virtual environment

   ```sh
   git clone https://github.com/ArgoTheNaut/omneo-deploy
   cd omneo-deploy
   python3 -m venv dht11
   python3 -m pip install adafruit-circuitpython-dht
   source dht11/bin/activate
   ```

1. Set up the output data stream

   ```sh
   sudo mkdir /var/data/
   sudo mkdir /var/data/dht11
   # Assign whatever account will be running the program permission to this folder
   ```

1. 
