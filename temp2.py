from simulation import Agent
import commands.DataControl as DataControl
import commands.Settings.Global as Global
import commands.Settings.InterfaceAndDataChannel as InterfaceAndDataChannel
from util.MessageFormat import *
from util import Modem

import threading
import time

ip = "10.78.31."
port = 9200



agent = Agent(ip,port,2)
# print(agent)
thread = threading.Thread(target=agent.run)
thread.start()
while True:
    pass