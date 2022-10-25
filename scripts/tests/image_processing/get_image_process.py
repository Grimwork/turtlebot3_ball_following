#!/usr/bin/env python3

import rospy
import cv2 as cv
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

HEIGHT, WIDTH = 480, 640
HIGHER_YELLOW, LOWER_YELLOW = np.array([35, 255, 255]), np.array([25, 50, 70])

class ImageListener:

    bridge = CvBridge()

    def __init__(self):
        rospy.init_node("listener_camera", anonymous=True)
        self.sub = rospy.Subscriber("/camera/rgb/image_raw", Image, self.callback_image_listener)

        rospy.spin()

    def callback_image_listener(self, image_data):
        try:
            frame = self.bridge.imgmsg_to_cv2(image_data, "bgr8")
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

        for [x, y, radius] in circles[0,:]:
            if mask[y, x]:
                cv.circle(frame, (x, y), radius, (0, 255, 0), 2)
                cv.circle(frame, (x, y), 2, (0, 0, 255), 3)

        cv.imshow("result", frame)

        if cv.waitKey(1) & 0xFF == ord("q"):
            cv.destroyAllWindows()
            self.sub.unregister()
            rospy.signal_shutdown("end")


if __name__ == "__main__":
    ImageListener()
