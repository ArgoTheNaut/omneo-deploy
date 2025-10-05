echo "CCS811 Service Launcher: moving to omneo deploy"
cd /home/pi/omneo-deploy      # Go to base directory
echo "CCS811 Service Launcher: activating virtual environment"
source ./.ccs811/bin/activate   # Enable venv
echo "CCS811 Service Launcher: starting up service"
python3 src/ccs811/main.py
