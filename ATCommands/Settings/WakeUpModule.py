def get_wakeup_active_time(modem):
    at_cmd = "AT?DA"
    print(at_cmd)
    modem.send_command(at_cmd)

def set_wakeup_active_time(modem, n):
    at_cmd = f"AT!DA{n}"
    modem.send_command(at_cmd)

def get_wakeup_period(modem):
    at_cmd = "AT?DT"
    modem.send_command(at_cmd)

def set_wakeup_period(modem, n):
    at_cmd = f"AT!DT{n}"
    modem.send_command(at_cmd)

def get_hold_timeout(modem):
    at_cmd = "AT?ZH"
    modem.send_command(at_cmd)

def set_hold_timeout(modem, n):
    at_cmd = f"AT!ZH{n}"
    modem.send_command(at_cmd)

def get_awake_remote_mode(modem):
    at_cmd = "AT?DW"
    modem.send_command(at_cmd)

def set_awake_remote_mode(modem, n):
    at_cmd = f"AT!DW{n}"
    modem.send_command(at_cmd)

def get_remote_active_time(modem):
    at_cmd = "AT?DR"
    modem.send_command(at_cmd)

def set_remote_active_time(modem, n):
    at_cmd = f"AT!DR{n}"
    modem.send_command(at_cmd)