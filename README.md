# Raspberry PI Configuration for StandUp

This guide describes how to configure [Raspberry PI](https://www.raspberrypi.org/) mini pc.

## Install RaspberryPI
- 1. Format SD card using [SD formatter](https://www.sdcard.org/downloads/formatter_4/)
- 2. Download latest [RASPBIAN JESSIE LITE](https://www.raspberrypi.org/downloads/raspbian/)
- 3. Install [Etcher](https://etcher.io/) and write img into SD card

## RaspberryPI Configuration

### 1) Necessary preconditions

**Let's start to update and set every important settings**

> Make sure to update your Pi

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade
sudo apt-get clean
sudo raspi-config
```

> - Enlarge your disk Size
> - Set correct timezone
> - Enable SSH
> - Enable Camera

Install some utils
sudo apt-get install mc vim htop

Set 1G mode in /boot/config.txt
arm_freq=1000

> Test Camera
```
raspistill -w 1920 -h 1080 -sh 40 -awb auto -mm average -hf -vf
```

## Install Tools:


### 1) Install Supervisor

```
sudo apt-get install supervisor
sudo service supervisor restart
```

### 2) Install Apache

```
sudo apt-get install apache2 -y
```

disable default enable custom with 

```
DocumentRoot /var/www/tl
<Directory “/var/www/tl“>
    Options All Indexes FollowSymLinks
    Order allow,deny
    Allow from all
</Directory>
```

## Notes:

- Compress images:
-z : Compress archive using gzip program
-c: Create archive
-v: Verbose i.e display progress while creating archive
-f: Archive File name

```
tar -zcvf prog-1-jan-2005.tar.gz /home/jerry/prog
```

- Check Free SPACE
```
df -Bm
```


- Copy file to Raspy:

```
scp raspiLapseCam.py timelapse-work:/home/pi/raspiLapseCam.py


```
