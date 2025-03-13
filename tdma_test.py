import commands.DataControl as DataControl
import commands.Settings.Global as Global
import commands.Settings.InterfaceAndDataChannel as InterfaceAndDataChannel
from util.MessageFormat import *
from util import Modem

import threading
import time

TIME_SLOT_DURATION = 2  # Each node gets 2 seconds to transmit

class Agent(Modem.Modem):
    def __init__(self, host_ip, port, node_id):
        self.node_id = node_id
        self.init(host_ip, node_id, port)
        
        Global.set_promiscuous_mode(self, 0)
        InterfaceAndDataChannel.set_position_data_output_setting(self, 0)
        
        self.startup()
    
    def startup(self):
        while True:
            time.sleep((self.node_id - 1) * TIME_SLOT_DURATION)  # Wait for its time slot
            
            if self.node_id == 1:
                data = {"to": 3, "msg": "From 1 to 2"}
                msg = self.serialize_to_json(data)
                DataControl.send_instant_message(self, length=len(msg), destination=2, 
                                                 flag="noack", data=msg)
                print(f"Node {self.node_id} transmitted message.")
            
            time.sleep(TIME_SLOT_DURATION)  # Simulate transmission time

            time.sleep((3 - self.node_id) * TIME_SLOT_DURATION)  # Wait for next cycle
    
    def receive_message(self, msg):
        if self.node_id == 2 and isinstance(msg, RECVIM):
            data = self.deserialize_from_json(msg.data)
            data["msg"] = data["msg"] + " and then to 3"
            msg = self.serialize_to_json(data)
            DataControl.send_instant_message(self, length=len(msg),
                                             destination=data["to"], flag="noack",
                                             data=msg)
        elif self.node_id == 3 and isinstance(msg, RECVIM):
            print(msg.data)

ip = "10.78.31."
port = 9200
agent_ids = [1, 2, 3]

threads = []
for agent_id in agent_ids:
    thread = threading.Thread(target=Agent, args=(ip, port, agent_id))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()