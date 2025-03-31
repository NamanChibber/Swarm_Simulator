#!/usr/bin/env python3
import rospy
import re
from std_msgs.msg import String as ROSString
from waypoint.srv import sendWpType1  # Import the correct service type

def velocity_client_mred(x, y, yaw):
    """
    Client to send waypoint (x, y, yaw) to mred using the sendWpType1 service.
    """
    rospy.loginfo("Waiting for the /mred0/controls/send_wp_standard service...")
    rospy.wait_for_service('/mred0/controls/send_wp_standard')
    rospy.loginfo("Service is available. Preparing to send waypoint for mred.")
    try:
        # Create a service proxy to call the service
        send_wp = rospy.ServiceProxy('/mred0/controls/send_wp_standard', sendWpType1)
        rospy.loginfo(f"Sending waypoint to mred: x={x}, y={y}, yaw={yaw}")
        response = send_wp(x, y, yaw)
        rospy.loginfo(f"Received response: {response}")
        return response
    except rospy.ServiceException as e:
        rospy.logerr(f"Service call failed: {e}")
        return None

def received_callback(msg):
    """
    Callback for the 'node2_received' topic.
    Parses the message string to extract x, y, z, and optionally yaw.
    Then calls the mred waypoint service with x, y, and yaw.
    Expected format: "S{source} - x: {x:.2f}, y: {y:.2f}, z: {z:.2f}" or 
                     "S{source} - x: {x:.2f}, y: {y:.2f}, z: {z:.2f}, yaw: {yaw:.2f}"
    """
    rospy.loginfo(f"Received message: {msg.data}")
    # Updated regex pattern: yaw is optional.
    pattern = r"S\d+\s*-\s*x:\s*([-\d\.]+),\s*y:\s*([-\d\.]+),\s*z:\s*([-\d\.]+)(?:,\s*yaw:\s*([-\d\.]+))?"
    match = re.search(pattern, msg.data)
    if match:
        try:
            x = float(match.group(1))
            y = float(match.group(2))
            # z is parsed but not used for mred waypoint service.
            z = float(match.group(3))
            # yaw is optional; if not provided, default to 0.0
            yaw = float(match.group(4)) if match.group(4) is not None else 0.0
            velocity_client_mred(x, y, yaw)
        except ValueError as e:
            rospy.logerr(f"Error converting parsed values: {e}")
    else:
        rospy.logerr("Failed to parse the waypoint string from the message.")

if __name__ == "__main__":
    # Initialize the node.
    rospy.init_node('velocity_client_node', anonymous=True)
    # Subscribe to the 'node2_received' topic.
    rospy.Subscriber('node2_received', ROSString, received_callback)
    # Keep the node alive.
    rospy.spin()
