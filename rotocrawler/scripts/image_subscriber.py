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

def callback(data):
    br = CvBridge()
    rp.loginfo('recieving image')
    cv.imshow("camera", br.imgmsg_to_cv2(data))
    cv.waitKey(1)

def cv_listener():
    rp.init_node('listener', anonymous=False)
    rp.Subscriber('image_data', Image, callback)
    rp.spin()
    cv.destroyAllWindows()

if __name__ == '__main__':
    cv_listener()

