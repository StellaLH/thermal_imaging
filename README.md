# thermal_imaging
A FLIR Lepton and Raspberry Pi NoIR Camera have been used for imaging in the lab. Scripts have been developed to continually save images from both cameras.

These cameras should be connected to a Raspberry Pi and teh folllowing scripts run from there.

# picam.py

Saves an image acquired by the Raspberry Pi camera once every 30 seconds using the python module, picamera.


# leptoncam.py

Saves an image acquired by the FLIR Lepton once every 30 seconds using the python modules, pylepton. This module can be used to overlay the thermal image onto the regular image. 
