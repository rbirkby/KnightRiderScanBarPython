KnightRiderScanBar in Python
============================

An implementation of the KnightRiderScanBar Arduino/C repo for Python on a 
Raspberry pi. Tested with a Raspberry Pi Zero.

TODO: 
* How to enable SPI on Raspbian

```bash
$ sudo pip install -r requirements.txt
$ sudo cp /home/pi/KnightRiderScanBar.service /etc/systemd/system
$ sudo systemctl enable KnightRiderScanBar
$ sudo systemctl start KnightRiderScanBar
```
