# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 12:35:41 2017

@author: stella
"""

import numpy as np
import time as t
import cv2
from pylepton import Lepton

try:
    while True:
        with Lepton() as l:
            a,_=l.capture()
        time_str=t.strftime("%Y%m%d%H%M%S")
        cv2.normalize(a,a,0,65535,cv2.NORM_MINMAX)
        np.right_shift(a,8,a)
        cv2.imwrite("lepton_img_%s,jpg" %time_str)
	t.sleep(30)