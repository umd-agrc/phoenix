#!/usr/bin/env python

#----------------------------------------#
# @title: image_publisher.py
#
# @author: Malcolm D. Forbes
# @email: mdforbes@umd.edu
# @version: v.0.0.1
#
# @licsense: GPLv3 (GNU3)
#----------------------------------------#

import rospy as rp
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2 as cv

def cv_publisher():
    pub = rp.Publisher('image_data', Image, queue_size=1)
    rp.init_node('camera', anonymous=False)
    rate = rp.Rate(60) #60 Hz
    cap = cv.VideoCapture(0)
    br = CvBridge()

    while not rp.is_shutdown():
        [ret, frame] = cap.read()
        if ret == True:
            rp.loginfo('publish image')
            pub.publish(br.cv2_to_imgmsg(frame))

        rate.sleep()

if __name__ == '__main__':
    try:
        cv_publisher()
    except rp.ROSInterruptException:
        pass
