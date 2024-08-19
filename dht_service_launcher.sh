echo "DHT11 Service Launcher: moving to omneo deploy"
cd /home/pi/omneo-deploy      # Go to base directory
echo "DHT11 Service Launcher: activating virtual environment"
source ./dht11/bin/activate   # Enable venv
echo "DHT11 Service Launcher: starting up service"
python3 unit_tests/test2_dht11.py
