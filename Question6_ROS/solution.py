#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

num1 = 0.0
num2 = 0.0

def bruh1_num(data):
    global num1
    num1 = data


def bruh2_num(data):
    global num2
    num2 = data


def sum():
    global num1, num2
    rospy.init_node('bruh_sum', anonymous=True)

    rospy.Subscriber('bruh1', Int32, bruh1_num)
    rospy.Subscriber('bruh2', Int32, bruh2_num)

    rate = rospy.Rate(10) # 10hz
    pub = rospy.Publisher('sum', Int32, queue_size=10)
    
    rate.sleep()
    while not rospy.is_shutdown():
        pub.publish(num1 + num2)
        rate.sleep()
    # rospy.spin()

if __name__ == '__main__':
    sum()
