#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose2D
from Vector3.msg import Vector3

rospy.init_node('Vector3_publisher')
pub = rospy.Publisher('Vector3_msg', Vector3, queue_size=1)
msg = TimePose()
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    msg.timestamp = rospy.get_rostime()
    second = msg.timestamp.secs
    msg.pose = Pose2D(x=second%2, y=second%9, z=second%3)
    pub.publish(msg)
    print "publish:", msg.timestamp.secs%100, msg.pose.x, msg.pose.y, msg.pose.z
    rate.sleep()