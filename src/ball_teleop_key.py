#!/usr/bin/env python3

import rospy
import sys, select, os
import tty, termios
from turtlebot3_ball_following.msg import BallMoveInfo

msg = """
=============================
Moving the ball around:
        Z
   Q    S    D
     
Spacebar to jump !

CTRL-C to quit
=============================
"""

def getKey():
    if os.name == 'nt':
        timeout = 0.1
        startTime = time.time()
        while(1):
            if msvcrt.kbhit():
                if sys.version_info[0] >= 3:
                    return msvcrt.getch().decode()
                else:
                    return msvcrt.getch()
            elif time.time() - startTime > timeout:
                return ''

    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

if __name__=="__main__":

    settings = termios.tcgetattr(sys.stdin)

    rospy.init_node('ball_teleop_key')
    pub = rospy.Publisher('ball_moving_info', BallMoveInfo, queue_size=10)
    
    print(msg)
    while not rospy.is_shutdown():
        key = getKey()
        if key == 'z' :
            print("Z is pressed !")
        elif key == 'q' :
            print("Q is pressed !")
        elif key == 's' :
            print("S is pressed !")
        elif key == 'd' :
            print("D is pressed !")
        elif key == ' ' :
            print("Space is pressed !")
        else:
            if key == '\x03' : # CTRL-C
                break

        pub.publish(BallMoveInfo)
