# Room Temperature Monitoring Service

# Overview

This segment uses a DHT11 sensor on a Raspberry Pi 3B to track the temperature and humidity of a room.

# Instructions

1. On the Raspberry Pi, clone down the deployment repository
    ```sh
    git clone https://github.com/ArgoTheNaut/omneo-deploy
    cd omneo-deploy
    python3 -m venv dht11
    source ./dht11/bin/activate
    python3 -m pip install adafruit-circuitpython-dht
    ```
1. Run the test script
    ```sh
    python3 unit_tests/test2_dht11.py
    ```
