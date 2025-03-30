#!/usr/bin/env python3
from agent_node import AgentNode  # Ensure agent_node.py is in the same directory or adjust the path

# Parameters for the agent: source, sensor_topic, destination, and publisher_topic.
source = 2
sensor_topic = "sensor2"  # Topic for sensor data subscription
destination = 1
publisher_topic = "node2_received"  # Topic to publish received messages

# Create an instance of AgentNode with the specified parameters.
agent_node_instance = AgentNode(
    source_id=source, 
    sensor_topic=sensor_topic, 
    destination_id=destination, 
    publisher_topic=publisher_topic
)
agent_node_instance.run()
