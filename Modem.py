import logging
import socket
import threading
import os
from datetime import datetime
import sys
import select
import time

script_dir = os.path.dirname(os.path.abspath(__file__))
log_folder = os.path.join(script_dir, 'logs')
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

timestamp = datetime.now().strftime("%m-%d_%H-%M")
log_file = os.path.join(log_folder, f"debug_{timestamp}.log")

logging.basicConfig(filename=log_file, filemode="w", level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s: %(message)s', 
                    datefmt='%d-%m-%Y %H:%M:%S %p')

logging.debug("Logging Start")

class Modem:
    def __init__(self, host_ip, port):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((host_ip, port))
            logging.debug(f"Connected to {host_ip}:{port}")

            self.stop_event = threading.Event()
            self.receive_thread = threading.Thread(target=self.receive_data)
            self.receive_thread.start()
        except Exception as e:
            logging.error(f"Error initializing modem: {e}")

    def send_command(self, at_cmd):
        time.sleep(1)
        try:
            self.socket.send(f"+++{at_cmd}\n".encode())
            logging.debug(f"Sent: {at_cmd}")
            print(at_cmd)
        except Exception as e:
            logging.error(f"Error sending command: {e}")

    def receive_data(self):
        while not self.stop_event.is_set():
            try:
                ready = select.select([self.socket], [], [], 5)
                if ready[0]:
                    data = self.socket.recv(2048).decode()
                    logging.debug(f"Received: {data}")
                    print(data)
            except Exception as e:
                logging.error(f"Error receiving data: {e}")
                break

    def close(self):
        try:
            self.stop_event.set()
            self.receive_thread.join()
            self.socket.close()
            
            logging.debug("Socket closed")
            sys.exit(0)
            
        except Exception as e:
            logging.error(f"Error closing socket: {e}")