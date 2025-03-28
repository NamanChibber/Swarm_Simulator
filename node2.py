#!/usr/bin/env python3
import rospy
from simulation2 import Agent
import commands.DataControl as DataControl
import commands.Settings.Global as Global
import commands.Settings.InterfaceAndDataChannel as InterfaceAndDataChannel
from util.MessageFormat import *
from util import Modem
from std_msgs.msg import String

import threading
import time

if __name__ == '__main__':
    ip = "10.78.31."
    port = 9200
    agent_ids = [2]  # Define IDs for all agents

    agents = {}
    threads = []

    # Create agents and start their threads
    for agent_id in agent_ids:
        agent = Agent(ip, port, agent_id)
        agents[agent_id] = agent  # Store references to agents
        thread = threading.Thread(target=agent.run)
        threads.append(thread)
        thread.start()

    # Example: Send messages between agents
    time.sleep(5)  # Allow agents to initialize

    while True:
        agents[2].send_msg(destination_id=1, ctx="Hello from Naman")
        time.sleep(2)
        
        