#!/usr/bin/env python3

import rospy
import cv2 as cv
import numpy as np

from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from turtlebot3_ball_following.msg import ImageInfo
from constants import *

bridge = CvBridge()

class ImageProcessing:

    def __init__(self):

        self.bridge = CvBridge()

        rospy.init_node("camera_driver", anonymous=True)

        self.sub = rospy.Subscriber("/camera/rgb/image_raw", Image, self.image_listener_callback)
        self.pub = rospy.Publisher("/image_processing/info", ImageInfo, queue_size=10)

        self.rate = rospy.Rate(2) # 2hz

        rospy.spin()

        self.unregister()

    def image_listener_callback(self, image_data):
        try:
            frame = bridge.imgmsg_to_cv2(image_data, "bgr8")
        except CvBridgeError as e:
            print(e)

        hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        mask = cv.inRange(hsv_frame, LOWER_YELLOW, HIGHER_YELLOW)

        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        circles = cv.HoughCircles(
            gray_frame, 
            cv.HOUGH_GRADIENT,
            1,20,
            param1=50,param2=30,minRadius=0,maxRadius=0
        )

        circles = np.uint16(np.around(circles))
        circles = circles[0,:]

        if circles.size == 0:
            rospy.loginfo(rospy.get_caller_id() + " I don't see yellow ball")
            return

        for [x, y, radius] in circles:
            if mask[y, x]:
                image_info = ImageInfo()

                image_info.ball_found = len(circles) > 0
                image_info.ball_center_x = x
                image_info.ball_center_y = y
                image_info.ball_radius = radius

                self.pub.publish(image_info)

                rospy.loginfo(rospy.get_caller_id() + " Publishing image information :\n" + str(image_info))

                #TODO Gerer le cas où on a plusieurs boules
                break

        self.rate.sleep()

    def unregister(self):
        self.sub.unregister()
        self.pub.unregister()

if __name__ == "__main__":
    ImageProcessing()
