# Wall2.0
Starting with a clean install of Raspbian Jessie.
```
sudo apt-get install bluez libusb-dev pyqt4-dev-tools joystick libbluetooth-dev libjack0 libjack-dev bluez-hcidump 
sudo hciconfig hci0 up
```
### Connect controller via USB
```
sudo ./sixpair
```
### Disconnect controller from USB
```
git clone https://github.com/falkTX/qtsixa/ (if needed)
make
make install
```
### Start sixad for testing
```
sudo sixad --start
```
### Install sixad daemon
```
sudo update-rc.d sixad defaults
sudo reboot
```
### Ensure that the Bluetooth adapter is available for pairing
```
sudo hciconfig hci0 pscan
```
### Start the serive
```
sudo systemctl start sixad.service
```
