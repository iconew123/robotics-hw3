#!/usr/bin/env python
import rospy
from Twist.msg import Twist

def callback(msg):
    print "subscribe:", msg.timestamp.secs%100, msg.pose.x, msg.pose.y, msg.pose.z

rospy.init_node('subscriber_algorithm')
sub = rospy.Subscriber('Twist_msg', Twist, callback)
rospy.spin()

