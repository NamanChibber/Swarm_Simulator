def switch_to_deaf_state(modem):
    at_cmd = "ATS"
    modem.send_command(at_cmd)
    
def switch_to_noise_state(modem):
    at_cmd = "ATN"
    modem.send_command(at_cmd)
    
def switch_to_listen_state(modem):
    at_cmd = "ATA"
    modem.send_command(at_cmd)
    
def close_acoustic_connection(modem):
    at_cmd = "ATH0"
    modem.send_command(at_cmd)
    
def terminate_acoustic_connection(modem):
    at_cmd = "ATH1"
    modem.send_command(at_cmd)
    
def reset_device(modem):
    at_cmd = "ATZ0"
    modem.send_command(at_cmd)
    
def drop_burst_data(modem):
    at_cmd = "ATZ1"
    modem.send_command(at_cmd)
    
def drop_instant_message(modem):
    at_cmd = "ATZ3"
    modem.send_command(at_cmd)
    
def clear_transmission_buffer(modem):
    at_cmd = "ATZ4"
    modem.send_command(at_cmd)
    
def view_firmware_version(modem):
    at_cmd = "ATI0"
    modem.send_command(at_cmd)
    
def view_physical_datalink_version(modem):
    at_cmd = "ATI1"
    modem.send_command(at_cmd)
    
def view_serial_number(modem):
    at_cmd = "ATI2"
    modem.send_command(at_cmd)
    
def view_device_manufacturer(modem):
    at_cmd = "ATI7"
    modem.send_command(at_cmd)