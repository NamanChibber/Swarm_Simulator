import commands.DataControl as DataControl
import commands.Settings.Global as Global
import commands.Settings.InterfaceAndDataChannel as InterfaceAndDataChannel
from util.MessageFormat import *
from util import Modem

import threading
import time

class Agent(Modem.Modem):
    def __init__(self, host_ip, port, node_id):
        super().__init__()  # Initialize the parent Modem class
        self.node_id = node_id
        self.latest_received_msg = None  # New variable to store the latest received message
        self.init(host_ip, node_id, port)
        Global.set_promiscuous_mode(self, 0)  # Set promiscuous mode to off
        InterfaceAndDataChannel.set_position_data_output_setting(self, 0)  # Disable position data output

    def send_msg(self, destination_id, ctx):
        """Send a message to another agent."""
        data = {"to": destination_id, "msg": ctx}
        msg = self.serialize_to_json(data)
        DataControl.send_instant_message(
            self,
            length=len(msg),
            destination=destination_id,
            flag="noack",
            data=msg,
        )
        print(f"Node {self.node_id} sent: {ctx} to Node {destination_id}")

    def receive_message(self, msg):
        """Process incoming messages and store the latest received message."""
        if isinstance(msg, RECVIM):  # Check if the message is of type RECVIM
            data = self.deserialize_from_json(msg.data)
            print(f"Node {self.node_id} received: {data['msg']} from Node {msg.source}")
            
            # Store the latest received message
            self.latest_received_msg = data['msg']
            
            # Example: Modify the message and forward it to another node if needed
            if "to" in data and data["to"] != self.node_id:
                data["msg"] += f" (forwarded by Node {self.node_id})"
                msg = self.serialize_to_json(data)
                DataControl.send_instant_message(
                    self,
                    length=len(msg),
                    destination=data["to"],
                    flag="noack",
                    data=msg,
                )
                print(f"Node {self.node_id} forwarded: {data['msg']} to Node {data['to']}")


    def run(self):
        """Run the agent to listen for incoming messages."""
        print(f"Agent {self.node_id} running...")


    def __call__(self):
        """Allows instance to be callable in threading."""
        self.run()
