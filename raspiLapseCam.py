#!/usr/bin/env python

# Import some frameworks
import os
import time

from datetime import datetime

debug = False

if not debug:
    import RPi.GPIO as GPIO

outFolder = "/var/www/tl/"
project = "stavba"
start_hour = 7
stop_hour = 18
delay = 60  # seconds
delay = 1 if debug else delay

# Define the size of the image you wish to capture.
imgWidth = 1920  # Max = 2592
imgHeight = 1080  # Max = 1944

# Grab the current datetime which will be used to generate dynamic folder names
d = datetime.now()
initYear = "%04d" % (d.year)
initMonth = "%02d" % (d.month)
initDate = "%02d" % (d.day)
initHour = "%02d" % (d.hour)
initMins = "%02d" % (d.minute)

# initially disabled (nothing to compress)
compress_enabled = False
# Set the initial serial for saved images to 1
fileSerial = 1

# Run a WHILE Loop of infinitely
while True:

    d = datetime.now()
    if start_hour <= d.hour < stop_hour and (not debug or fileSerial < 2):
        compress_enabled = True

        # create or check if this day folder exists
        folderToSave = project + "_" + str(initYear) + str(initMonth) + str(initDate) if debug else \
            outFolder + project + "_" + str(initYear) + str(initMonth) + str(initDate)
        if not os.path.exists(folderToSave):
            os.mkdir(folderToSave)

        # Set FileSerialNumber to 000X using four digits
        fileSerialNumber = "%04d" % (fileSerial)

        # Capture the CURRENT time (not start time as set above) to insert into each capture image filename
        year = "%04d" % (d.year)
        month = "%02d" % (d.month)
        date = "%02d" % (d.day)
        hour = "%02d" % (d.hour)
        mins = "%02d" % (d.minute)

        print " ============= Saving file at " + hour + ":" + mins

        # Capture the image using raspistill. Set to capture with added sharpening, auto white balance and average metering mode
        # Change these settings where you see fit and to suit the conditions you are using the camera in
        if debug:
            os.system("touch " + str(folderToSave) + "/" + str(fileSerialNumber) + "_" + str(hour) + str(mins) + ".txt ")
        else:
            os.system("raspistill -w " + str(imgWidth) + " -h " + str(imgHeight) +
                      " -o " + str(folderToSave) + "/" + str(fileSerialNumber) + "_" + str(hour) + str(mins) +
                      ".jpg  -sh 40 -awb auto -mm average -hf -vf")

        # Increment the fileSerial
        fileSerial += 1

        # Wait before next capture
        time.sleep(delay)
    else:

        # night lets compress this day
        if compress_enabled:
            print " ============= Compressing file " + folderToSave
            os.system("tar -zcf " + folderToSave + ".tar.gz " + folderToSave)

            print " ============= Removing photo folder" + folderToSave
            os.system("rm -rf " + folderToSave)
            compress_enabled = False
