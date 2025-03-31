#!/usr/bin/env python3
from agent_node import AgentNode  # Ensure agent_node.py is in the same directory or adjust the path

# Parameters for the agent: source, sensor_topic, destination, and publisher_topic.
source = 1
sensor_topic = "/bluerov_heavy0/State"  # Topic for sensor data subscription
destination = 2
publisher_topic = "node1_received"  # Topic to publish received messages

# Create an instance of AgentNode with the specified parameters.
agent_node_instance = AgentNode(
    source_id=source, 
    sensor_topic=sensor_topic, 
    destination_id=destination, 
    publisher_topic=publisher_topic
)
agent_node_instance.run()
