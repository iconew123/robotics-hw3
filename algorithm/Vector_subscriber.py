#!/usr/bin/env python
import rospy
from Vector3.msg import Vector3

def callback(msg):
    print "subscribe:", msg.timestamp.secs%100, msg.pose.x, msg.pose.y, msg.pose.z

rospy.init_node('Vector3_subscriber')
sub = rospy.Subscriber('Vector3_msg', TimePose, callback)
rospy.spin()
