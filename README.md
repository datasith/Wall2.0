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
### Disconnect controller from USB and clone sixad repo
```
wget http://sourceforge.net/projects/qtsixa/files/QtSixA%201.5.1/QtSixA-1.5.1-src.tar.gz
tar xfvz QtSixA-1.5.1-src.tar.gz
```
### Patch it
```
wget https://bugs.launchpad.net/qtsixa/+bug/1036744/+attachment/3260906/+files/compilation_sid.patch
patch ~/QtSixA-1.5.1/sixad/shared.h < compilation_sid.patch
```
### Install it
```
cd QtSixA-1.5.1/sixad
make
sudo mkdir -p /var/lib/sixad/profiles
sudo checkinstall
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
sudo hciconfig hci0 up pscan
```
### Start the serive
```
sudo systemctl start sixad.service
```
