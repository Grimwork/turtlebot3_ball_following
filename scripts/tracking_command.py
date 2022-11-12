#!/usr/bin/env python3

import rospy
import sys

from std_srvs.srv import SetBool

def tracking_command(command):
    rospy.wait_for_service('/tracking_driver/command')

    run_command = rospy.ServiceProxy('/tracking_driver/command', SetBool)
    result = run_command(command)
    
    return result.success

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: ./tracking_command run/stop")

    command_name = sys.argv[1]

    command = True if command_name == "run" else False
    success = tracking_command(command)

    print(success)