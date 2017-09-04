# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 12:22:18 2017

@author: stella
"""

import picamera
import time as t
camera=picamera.PiCamera()

try:
    while True:
        time_str=t.strftime("%Y%m%d%H%M%S")
        camera.capture("pi_img_%s.jpg" %time_str)
        print "Image campture, saved as img_", time_str,".jpg" 
	t.sleep(30)

except KeyboardInterrupt:   
    print "\nFinished image capture..."  