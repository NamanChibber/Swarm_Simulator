#!/usr/bin/env python3
import rospy
from std_msgs.msg import String as ROSString
import threading
import time
import os

# Import the modified Agent class
from simulation3 import Agent
from farol_msgs.msg import mState as State


class AgentNode(Agent):
    """
    AgentNode is a ROS-enabled Agent that inherits from Agent.
    It integrates ROS functionality such as topic subscription for sensor data,
    publishing the latest received message, periodic sending of sensor data, 
    and graceful shutdown.
    """
    def __init__(self, source_id: int, sensor_topic: str, destination_id: int, publisher_topic: str):
        """
        Initializes the AgentNode.

        :param source_id: Unique identifier for this node (used to initialize the Agent)
        :param sensor_topic: Name of the sensor topic to subscribe to (must be a non-empty string)
        :param destination_id: Destination node ID for sending messages
        :param publisher_topic: ROS topic to which received messages will be published
        """
        # Store parameters and initialize additional attributes.
        self.source_id = source_id
        self.sensor_topic = sensor_topic
        self.destination_id = destination_id
        self.publisher_topic = publisher_topic
        self.sensor_data = "No data received yet"
        self.running = True  # Flag to control the main sending loop

        # Initialize the ROS node with a unique name based on the source_id.
        rospy.init_node(f'agent_node_{self.source_id}', anonymous=True)
        # Original:
        # rospy.Subscriber(self.sensor_topic, ROSString, self.sensor_callback)
        # Updated:
        rospy.Subscriber(self.sensor_topic, State, self.sensor_callback)

        # Create a publisher for the given publisher topic.
        self.pub = rospy.Publisher(self.publisher_topic, ROSString, queue_size=10)

        # Hard-coded IP and port used for agent communication.
        ip = "10.78.31."
        port = 9200
        # Initialize the parent Agent class.
        super().__init__(ip, port, self.source_id)

        # Start the parent's run() method in a daemon thread.
        self.agent_thread = threading.Thread(target=super().run, daemon=True)
        self.agent_thread.start()

        # Allow the agent to initialize.
        time.sleep(5)

        # Register the shutdown callback to ensure graceful termination.
        rospy.on_shutdown(self.shutdown)

        # Start a thread to periodically publish the latest received message.
        self.pub_thread = threading.Thread(target=self.publish_received, daemon=True)
        self.pub_thread.start()

    def sensor_callback(self, msg: ROSString):
        """
        Callback function for incoming messages on the sensor topic.
        Updates the latest sensor data to be used when sending messages.

        :param msg: ROS message of type String.
        """
        x = msg.X
        y = msg.Y
        z = msg.Z
        yaw = msg.Yaw
        self.sensor_data = f"S{self.source_id} - x: {x:.0f}, y: {y:.0f}, z: {z:.0f}, yaw: {yaw:.0f}"

    def publish_received(self):
        """
        Periodically publishes the latest received message (if any) to the specified ROS topic.
        """
        rate = rospy.Rate(1)  # Publish once per second.
        while not rospy.is_shutdown() and self.running:
            if self.latest_received_msg is not None:
                self.pub.publish(ROSString(self.latest_received_msg))
            rate.sleep()

    def shutdown(self):
        """
        Shutdown callback to terminate loops and force exit the process.
        """
        self.running = False
        rospy.loginfo(f"AgentNode {self.source_id} shutting down.")
        os._exit(0)

    def run(self):
        """
        Main loop for sending messages periodically using the latest sensor data.
        Uses a rospy.Rate object to send messages every 2 seconds.
        """
        rate = rospy.Rate(0.5)  # 0.5 Hz -> one message every 2 seconds.
        while not rospy.is_shutdown() and self.running:
            self.send_msg(destination_id=self.destination_id, ctx=self.sensor_data)
            rate.sleep()
