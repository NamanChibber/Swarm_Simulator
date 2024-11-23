def get_current_settings(modem):
        at_cmd = "AT&V"
        modem.send_command(at_cmd)
        
def store_current_settings(modem):
    at_cmd = "AT&W"
    modem.send_command(at_cmd)
    
def restore_factory_settings(modem):
    at_cmd = "AT&F"
    modem.send_command(at_cmd)