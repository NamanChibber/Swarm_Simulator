#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from simulation2 import Agent
import threading
import time
import os

class AgentNode:
    """
    AgentNode is a ROS node that wraps an Agent instance.
    It subscribes to a specified sensor topic and periodically sends messages 
    using the latest sensor data.
    """
    def __init__(self, source_id: int, sensor_topic: str, destination_id: int):
        """
        Initializes the AgentNode.

        :param source_id: Unique identifier for this node (used to initialize the Agent)
        :param sensor_topic: Name of the sensor topic to subscribe to (must be a non-empty string)
        :param destination_id: Destination node ID for sending messages
        """
        self.source_id = source_id
        self.sensor_topic = sensor_topic
        self.destination_id = destination_id
        self.sensor_data = "No data received yet"
        self.running = True  # Flag to control the main loop

        # Initialize the ROS node with a unique name based on the source_id.
        rospy.init_node(f'agent_node_{self.source_id}', anonymous=True)

        # Subscribe to the provided sensor topic.
        rospy.Subscriber(self.sensor_topic, String, self.sensor_callback)

        # Create the agent with the given source_id and predefined IP and port.
        ip = "10.78.31."
        port = 9200
        self.agent = Agent(ip, port, self.source_id)

        # Start the agent in its own thread as a daemon so it exits on shutdown.
        self.agent_thread = threading.Thread(target=self.agent.run, daemon=True)
        self.agent_thread.start()

        # Allow the agent to initialize.
        time.sleep(5)

        # Register the shutdown callback to ensure graceful shutdown.
        rospy.on_shutdown(self.shutdown)

    def sensor_callback(self, msg: String):
        """
        Callback function for sensor topic messages.

        :param msg: ROS message of type String from the sensor topic.
        """
        self.sensor_data = msg.data

    def shutdown(self):
        """
        Shutdown callback that stops the main loop and forces process termination.
        """
        self.running = False
        rospy.loginfo(f"AgentNode {self.source_id} shutting down.")
        # Forcefully terminate the process so that no further messages are processed.
        os._exit(0)

    def run(self):
        """
        Main loop that periodically sends messages using the latest sensor data.
        """
        rate = rospy.Rate(0.5)  # 0.5 Hz -> one message every 2 seconds.
        while not rospy.is_shutdown() and self.running:
            self.agent.send_msg(destination_id=self.destination_id, ctx=self.sensor_data)
            rate.sleep()
