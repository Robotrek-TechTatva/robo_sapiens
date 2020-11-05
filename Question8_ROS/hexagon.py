#!/usr/bin/env python
import rospy 
from math import pi as PI
from geometry_msgs.msg import Twist 

rospy.init_node('hexagon')

pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
rate = rospy.Rate(10)
vel = Twist():

def deg2rad(deg):
	return deg * PI / 180

def turn():
	global vel, rate, pub
	vel.angular.z = deg2rad(-60)
	pub.publish(vel)

	vel.angular.z = 0
	pub.publish(vel)

	rate.sleep()

def forward():
	global vel, rate, pub 
	
	vel.linear.x = 15
	pub.publish(vel)

	vel.linear.x = 0
	pub.publish(vel)

	rate.sleep()


def main():
	global pub, vel, rate 
	rate.sleep()
	sides = 6
	while not rospy.is_shutdown():
		for x in xrange(sides):
			turn()
			rospy.Rate(1).sleep()
			forward()
			rospy.Rate(1).sleep()
		break
	vel.linear.x = 0 
	vel.angular.z = 0
	pub(vel)

if __name__ == '__main__':
	main()