def command_interpreter(modem):
    at_cmd = "AT?MODE"
    modem.send_command(at_cmd)
    
def physical_layer_status(modem):
    at_cmd = "AT?PHY"
    modem.send_command(at_cmd)

def battery_voltage(modem):
    at_cmd = "AT?BV"
    modem.send_command(at_cmd)
    
def acoustic_connection_status(modem):
    at_cmd = "AT?S"
    modem.send_command(at_cmd)