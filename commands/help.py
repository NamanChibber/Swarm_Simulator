def see_all(modem):
    at_cmd = "AT?"
    modem.send_command(at_cmd)
    
def see_data_control(modem):
    at_cmd = "AT*$"
    modem.send_command(at_cmd)
    
def see_settings_management(modem):
    at_cmd = "AT&$"
    modem.send_command(at_cmd)
    
def see_requests(modem):
    at_cmd = "AT?$"
    modem.send_command(at_cmd)
    
def see_settings(modem):
    at_cmd = "AT!$"
    modem.send_command(at_cmd)
    
def see_interface_and_data_channel(modem):
    at_cmd = "AT*$"
    modem.send_command(at_cmd)
    
def search(modem, keyword):
    at_cmd = f"AT{keyword}$"
    modem.send_command(at_cmd)
    
def see_command_format(modem, cmd):
    at_cmd = f"AT{cmd}$"
    modem.send_command(at_cmd)