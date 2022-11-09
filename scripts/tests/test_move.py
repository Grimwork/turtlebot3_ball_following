import rospy
import moveit_commander
import numpy as np
import geometry_msgs

rospy.init_node("move_group_python_interface_tutorial", anonymous=True)
robot = moveit_commander.RobotCommander()

# arm / gripper

arm_group = moveit_commander.MoveGroupCommander("arm")

arm_joints = arm_group.get_current_joint_values()

arm_joints[0] = 0
arm_joints[1] = np.pi / 4
arm_joints[2] = 0
arm_joints[3] = np.pi / 4

arm_group.go(arm_joints, wait=True)
arm_group.stop()

# "end_effector_link"
print("Arm : " + str(arm_group.get_current_pose("end_effector_link")))

gripper_group = moveit_commander.MoveGroupCommander("gripper")

gripper_joints = gripper_group.get_current_joint_values()
gripper_joints = [0.019, 0.019]

gripper_group.go(gripper_joints, wait=True)
gripper_group.stop()

scene = moveit_commander.PlanningSceneInterface()

ball = geometry_msgs.msg.PoseStamped()
ball.header.frame_id = "yellow_ball"
ball.pose.position.x = 0.254363
ball.pose.position.y = -0.148264
ball.pose.position.z = 0.021663
ball_name = "yellow_ball"

scene.add_box(ball_name, ball, size=(1, 1, 1))

attached_objects = scene.get_attached_objects([ball_name])

#print(attached_objects)
print(scene.get_known_object_names())