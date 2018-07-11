#!/usr/bin/env python

#----------------------------------------#
# @title: image_subscriber.py
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

def callbackLeft(data):
    br_left = CvBridge()
    rp.loginfo('recieving image left')
    cv.imshow('camera_driver', br_left.imgmsg_to_cv2(data))
    cv.waitKey(5)

def callbackRight(data):
    br_right = CvBridge()
    rp.loginfo('recieveing image right')
    cv.imshow('camera_driver', br_right.imgmsg_to_cv2(data))
    cv.waitKey(5)

def cv_listener():
    rp.init_node('listener', anonymous=False)
    rp.Subscriber('image_raw_left', Image, callbackLeft)
    rp.Subscriber('image_raw_right', Image, callbackRight)
    rp.spin()
    cv.destroyAllWindows()

if __name__ == '__main__':
    cv_listener()

