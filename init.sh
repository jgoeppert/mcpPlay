# make MCP2210 accessible w/o root access
sudo lsusb  -v | grep -A 25 Microchi > lsusbROOT  # check mcp availabilty
lsusb  -v | grep -A 25 Microchi > lsusbUSR # check mcp availabilty
diff lsusb*
sudo cp 99-my-device.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules && sudo udevadm trigger


python3 -m venv .p_venv

source .p_venv/bin/activate

pip install pyusb




