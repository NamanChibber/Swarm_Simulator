import logging
import socket
import threading
import os
from datetime import datetime
import sys
import select
import time
from util.Parser import parser
import json

script_dir = os.path.dirname(os.path.abspath(__file__))
log_folder = os.path.join(script_dir, 'logs')
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

timestamp = datetime.now().strftime("%m-%d_%H-%M")
log_file = os.path.join(log_folder, f"debug_{timestamp}.log")

logging.basicConfig(filename=log_file, filemode="w", level=logging.DEBUG, 
                    format='%(asctime)s.%(msecs)03d: %(message)s', 
                    datefmt='%d-%m-%Y %H:%M:%S')

logging.debug("Logging Start")

class Modem:
    def init(self, host_ip, node_id, port):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((host_ip+str(node_id), port))
            logging.debug(f"N{self.node_id}@Connected to {host_ip}{node_id}:{port}")

            self.stop_event = threading.Event()
            self.receive_thread = threading.Thread(target=self.receive_data)
            self.receive_thread.start()
        except Exception as e:
            logging.error(f"N{self.node_id}@Error initializing modem: {e}")
            
    def serialize_to_json(self, obj):
        try:
            return json.dumps(obj, default=lambda o: o.to_dict() if hasattr(o, 'to_dict') else str(o))
        except TypeError as e:
            raise ValueError(f"Serialization error: {e}")
    
    def deserialize_from_json(self, json_string):
        try:
            return json.loads(json_string)
        except json.JSONDecodeError as e:
            raise ValueError(f"Deserialization error: {e}")

    def send_command(self, at_cmd):
        time.sleep(1)
        try:
            self.socket.send(f"+++{at_cmd}\n".encode())
            logging.debug(f"N{self.node_id}@Sent: {at_cmd}")
        except Exception as e:
            logging.error(f"N{self.node_id}@Error sending command: {e}")

    def receive_data(self):
        while not self.stop_event.is_set():
            try:
                ready = select.select([self.socket], [], [], 5)
                if ready[0]:
                    data = self.socket.recv(2048).decode()
                    data = data.replace('\n',"").replace('\r',"").replace('+++',"")
                    logging.debug(f"N{self.node_id}@Received: {data}")
                    self.receive_message(parser(data))
            except Exception as e:
                logging.error(f"N{self.node_id}@Error receiving data: {e}")
                break

    def close(self):
        try:
            self.stop_event.set()
            self.receive_thread.join()
            self.socket.close()
            
            logging.debug(f"N{self.node_id}@Socket closed")
            sys.exit(0)
            
        except Exception as e:
            logging.error(f"N{self.node_id}@Error closing socket: {e}")