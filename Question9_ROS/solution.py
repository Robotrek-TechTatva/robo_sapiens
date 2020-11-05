#!/usr/bin/env python3

'''
author: gokulp01
'''

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
import math
from math import sin, cos, tan

# declare all the global variables
_range_max = 10
pose=[]
goal_thresh=0.3

def Waypoints(t):
    x_coordinates=[((2*math.pi*i)/10) for i in range(11)]
    y_coordinates=[t(x_coordinates[i]) for i in range(11)]
    return [x_coordinates,y_coordinates]

def control_loop():
    
    global pose
    rospy.init_node('ebot_controller')
    
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/odom', Odometry, odom_callback)
    
    rate = rospy.Rate(10) 

    velocity_msg = Twist()
    velocity_msg.linear.x = 0
    velocity_msg.angular.z = 0
    pub.publish(velocity_msg)

    trajectory = lambda x: sin(x) 
    waypoint = Waypoints(trajectory)

    # print(waypoint)

    while not rospy.is_shutdown():
        
        i=0
        while i <=(len(waypoint[0])):
            if len(pose)>0:
            	# current pose 
                x1=pose[0]
                y1=pose[1]
                ebot_theta=pose[2]
            	
            	# goal pose 
                x2 = waypoint[0][i]
                y2 = waypoint[1][i]

                # deviations 
                theta_goal = math.atan2((y2-y1), (x2-x1))
                e_theta = theta_goal - ebot_theta

                dist = math.sqrt((x2-x1)**2 + (y2-y1)**2) 

                # for debugging 
                # print(pose)

                # proportional controller 
                print(round(dist, 4))
                print(round(e_theta, 4))
                
                velocity_msg.linear.x = 0.15*(dist)
                velocity_msg.angular.z = 0.7*(e_theta)
                pub.publish(velocity_msg)

                if (dist < 0.3):
                    print("reached", i)
                    i+=1


            rate.sleep()

def odom_callback(data):
    global pose
    x  = data.pose.pose.orientation.x;
    y  = data.pose.pose.orientation.y;
    z = data.pose.pose.orientation.z;
    w = data.pose.pose.orientation.w;
    pose = [data.pose.pose.position.x, data.pose.pose.position.y, euler_from_quaternion([x,y,z,w])[2]]







if __name__ == '__main__':
    try:
        control_loop()
    except rospy.ROSInterruptException:
        pass
