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
    python3 -m pip install adafruit-circuitpython-dht requests
    ```
1. Run the test script
    ```sh
    python3 unit_tests/test2_dht11.py
    ```

## Service Setup
Source: https://medium.com/@benmorel/creating-a-linux-service-with-systemd-611b5c8b91d6

```sh
cd /etc/systemd/system   # Move to the system folder
sudo nano dht11.service  # Create the service file
```

Inside of Nano, write:
```ini
[Unit]
Description=DHT11 onboard temperature and humidity sensor service
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=60
User=pi
ExecStart=/usr/bin/bash /home/pi/omneo-deploy/dht_service_launcher.sh

[Install]
WantedBy=multi-user.target
```

### Service Control Commands
```bash
sudo systemctl status dht11
sudo systemctl start dht11
sudo systemctl restart dht11
sudo systemctl stop dht11
```

