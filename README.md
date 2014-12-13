raspberry-pi-security-system
============================

A simple GPIO program with a web interface with the intention to use as a alarm system.

Hardware:
- Raspberry Pi (Using a B+ myself)
- Internet via Wi-Fi/LAN (Initially via LAN to make setup easy)
- Pi Camera (Optional, but basically is the coolest thing of the website part of this project)
- Some sensors as inputs (PIR/Door Sensors etc.)
- A siren or buzzer as output

Setup enviroment:

1. Configure a sd card with the latest Raspian (I used win32diskImager on Windows to get started)
2. On first boot raspi-config will run, configure locate and partion size as required. (Not going into detail on the basics)
3. Setup your desired network (I used a supported USB Wi-Fi dongle)
  - Configure /etc/network/interfaces (I committed mine, under network folder. I used wlan0)
  - Configure /etc/wpa_supplicant/wpa_supplicant.conf (also committed under network folder)
  - Configure /etc/resolv.conf (nameservers <your-dns>)
  - If you struggle to get your wireless lan going, first use a local LAN connection on the ethernet port. Do step 4 first       and then run "sudo apt-get install wireless-tools wpa_supplicant".
4. Get your pi up to date:
  - sudo apt-get update
  - sudo apt-get upgrade
5. Install some basic stuff you might need:
  - sudo apt-get install git 
  - sudo apt-get install vsfptd (Optional)
6. To make our lifes easier we reuse a well-mantained other project to stream our pi camera. All we will do is add the stream to our website. Get RPi_Cam_Web_Interface and install:
  - git clone https://github.com/silvanmelchior/RPi_Cam_Web_Interface.git
  - git pull origin master
  - ./RPi_Cam_Web_Interface_Installer.sh install
  - ./RPi_Cam_Web_Interface_Installer.sh start
  - Test your camera stream through web browser
7. 
  
  
  

