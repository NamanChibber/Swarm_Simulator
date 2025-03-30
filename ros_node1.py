#!/usr/bin/env python3
from agent_node import AgentNode  # Ensure agent_node.py is in the same directory or adjust the path

# Parameters for the agent: source, sensor_topic, and destination
source = 1
sensor_topic = "sensor1"  # Use a string for the topic name
destination = 2

# Create an instance of AgentNode with the specified parameters
agent_node_instance = AgentNode(source_id=source, sensor_topic=sensor_topic, destination_id=destination)
agent_node_instance.run()
