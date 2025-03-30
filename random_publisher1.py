#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import random

def publish_random_data():
    rospy.init_node('random_publisher1')
    pub = rospy.Publisher('/sensor1', String, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz
    
    while not rospy.is_shutdown():
        # Generate a single random coordinate set
        x = round(random.uniform(-100, 100), 2)
        y = round(random.uniform(-100, 100), 2)
        z = round(random.uniform(-100, 100), 2)
        
        random_value = f"S1 - x: {x}, y: {y}, z: {z}"
        rospy.loginfo(f"Publishing: {random_value}")
        pub.publish(random_value)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_random_data()
    except rospy.ROSInterruptException:
        pass
