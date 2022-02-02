# Oregon Wmr500Oregon Scientific WMR500 Driver for Weewx
This repository contains a Weewx driver for the Oregon Scientific WMR500 weather station.

# If you have not mqtt Server
## Install and setup mqtt
* Install mosquitto
  ``` 
  sudo apt update
  sudo apt upgrade
  sudo apt install mosquitto 
  ```

* If you have enable firewall you need open 1883 port
  ```
  iptables -t filter -A INPUT -p tcp --dport 1883 -j ACCEPT
  ```
  
# You need redirect mqtt.idtlive.com on your own mqtt
* Setup your DNS Router if possible else install dnsmasq
  ```
  sudo apt install dnsmasq
  ```

* Update the dsnmasq conf  
  ```
  sudo nano /etc/dnsmasq.conf
  ```

  ```
  dhcp-range=192.168.1.10,192.168.1.150,24h #ip range ipStart,ipEnd,validity_time
  dhcp-option=option:netmask,255.255.255.0
  dhcp-option=option:router,192.168.1.1 # Network Gateway ( Your internet box )
  dhcp-option=option:dns-server,192.168.1.25
  cache-size=256 # Number of DNS keep in cache (Mo)
  dhcp-host=xx:xx:xx:xx:xx:xx,machine_name,192.168.1.xx # set specific ip to exlude of range  mac,machine_name,ip
  ```

### Add redirect dns for mqtt.idtlive.com
* Create file /etc/dnsmasq.d/wmr500 and add 
  ```address=/mqtt.idtlive.com/192.168.1.25```

* Next check the dns in console<br>
  ```
  nslookup  
  server 192.168.1.xx  # IP where you have install dnsmasq
  mqtt.idtlive.com # Should return ip of your mqtt
  ```
  You should find IP configured in /etc/dnsmasq.d/wmr500
* Disable the DHCP in your router

---------

# Installation of weewx
### Add weewx source
  ```
  wget -qO - https://weewx.com/keys.html | sudo gpg --dearmor --output /etc/apt/trusted.gpg.d/weewx.gpg
  ```
* For python3
  ```
  wget -qO - https://weewx.com/apt/weewx-python3.list | sudo tee /etc/apt/sources.list.d/weewx.list
  ```
* For python2
  ```
  wget -qO - https://weewx.com/apt/weewx-python2.list | sudo tee /etc/apt/sources.list.d/weewx.list
  ```
### Run install
```
sudo apt-get update
sudo apt-get install weewx
```

# Add Wmr500 on weewx

* Download the latest release of Wmr500 : https://github.com/tguillaume02/Wmr500/releases<br/>
* Install the driver : ```wee_extension --install Wmr500.zip```<br/>
* Install require libs Python : ```sudo pip3 install paho-mqtt```<br/>
* Find on weewx.conf (/etc/weewx/weewx.conf) station_type and change by this : station_type = wxWmr500<br/>
* Next on weewx.conf add setup of your wmr500 <br/>
  ```[wxWmr500]
      host = mqtt.idtlive.com
      devid = 672fe9da-1d17-4d4d-8f5b-c824f5c6f0e8
      appid = 5568DD91-E97F-4C68-A567-0B94346681E6
      driver = user.wxWmr500
      poll_interval = 30 # get data each 30 seconds```
 
* Restart weewx : ```sudo service weewx restart```
* Check driver wmr500 ```sudo wee_config --list-drivers```
 
### Tips files weewx
* Config File => /etc/weewx/weewx.conf
* drivers => /usr/share/weewx/weewx/drivers 
* drivers user => /usr/share/weewx/user/
