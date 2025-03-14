import commands.DataControl as DataControl
import commands.Settings.Global as Global
import commands.Settings.InterfaceAndDataChannel as InterfaceAndDataChannel
from util.MessageFormat import *
from util import Modem

import threading
import time

class Agent(Modem.Modem):
    def __init__(self, host_ip, port, node_id):
        self.node_id = node_id
        self.init(host_ip, node_id, port)
        Global.set_promiscuous_mode(self, 0)
        InterfaceAndDataChannel.set_position_data_output_setting(self, 0)
        # self.startup()

    def startup(self):
        if self.node_id == 1:
            for i in range(2):
                data = {"to": 3, "msg":"From 1 to 2"}
                msg = self.serialize_to_json(data)
                DataControl.send_instant_message(self, length=len(msg), destination=2   , 
                                                 flag="noack", data=msg)
                time.sleep(5)
        
    def receive_message(self, msg):
        if self.node_id == 2 and isinstance(msg, RECVIM):
            data = self.deserialize_from_json(msg.data)
            # print(type(data))
            print(data['msg'])
            # print('hi')
            data["msg"] = data["msg"]+" and then to 3"
            msg = self.serialize_to_json(data)
            DataControl.send_instant_message(self, length=len(msg),
                                            destination=data["to"], flag = "noack",
                                            data= msg)
        elif self.node_id == 3 and isinstance(msg, RECVIM):
            print(msg.data)
    def send_msg(self,ctx):
        if self.node_id == 1:
            
            data = {"to": 3, "msg":ctx}
            msg = self.serialize_to_json(data)
            DataControl.send_instant_message(self, length=len(msg), destination=2   , 
                                                flag="noack", data=msg)
    def run(self):
        print(f"Agent running ")

    def __call__(self):
        self.run()  # Allows instance to be callable in threading
        
if __name__ == '__main__':    
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