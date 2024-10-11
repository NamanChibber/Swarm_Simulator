def send_burst_data(modem, length, destination, data, destination_pid = None):
    if destination_pid == None:
        at_cmd = f"AT*SEND,{length},{destination},{data}"
    else:
        at_cmd = f"AT*SEND,p{destination_pid},{length},{destination},{data}"
    
    modem.send_command(at_cmd)
    
def send_counter(modem):
    at_cmd = "AT?PC"
    modem.send_command(at_cmd)
    
def burst_data_delivery_counter(modem):
    at_cmd = "AT?ZE"
    modem.send_command(at_cmd)
    
def send_instant_message(modem, length, destination, flag, data, destination_pid = None):
    if destination_pid == None:
        at_cmd = f"AT*SENDIM,{length},{destination},{flag},{data}"
    else:
        at_cmd = f"AT*SENDIM,p{destination_pid},{length},{destination},{flag},{data}"
    
    modem.send_command(at_cmd)
    
