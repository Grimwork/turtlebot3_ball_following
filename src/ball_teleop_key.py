#!/usr/bin/env python3

import rospy
import sys, select, os
import tty, termios
from geometry_msgs.msg import Twist


LIN_VEL_STEP = 1.0
ANG_VEL_STEP = 1.0

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

if __name__=="__main__":

    rospy.init_node('ball_teleop_key')
    pub = rospy.Publisher('ball_moving_info', Twist, queue_size=10)

    msg = """
    =============================
    Moving the ball around:
         Z
    Q    S    D
        
    Spacebar to jump !

    CTRL-C to quit
    =============================
    """

    print(msg)

    settings = termios.tcgetattr(sys.stdin)
    linear_vel = 0
    linear_vel_z = 0
    angular_vel = 0
    while not rospy.is_shutdown():
        key = getKey()
        if key == 'z' :
            print("Z is pressed !")
            linear_vel = LIN_VEL_STEP
        elif key == 'q' :
            print("Q is pressed !")
            angular_vel = ANG_VEL_STEP
        elif key == 's' :
            print("S is pressed !")
            linear_vel = - LIN_VEL_STEP
        elif key == 'd' :
            print("D is pressed !")
            angular_vel = - ANG_VEL_STEP
        elif key == ' ' :
            print("Space is pressed !")
            linear_vel_z = LIN_VEL_STEP
        elif key == 'x' : # Press x to stop
            print("X is pressed ! \n Ball stopped moving !")
            linear_vel   = 0.0
            angular_vel  = 0.0
        else:
            if key == '\x03' : # CTRL-C
                break

        twist = Twist()

        twist.linear.x = linear_vel
        twist.linear.y = 0.0
        twist.linear.z = linear_vel_z

        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = angular_vel

        pub.publish(twist)
