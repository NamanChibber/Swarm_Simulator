def get_status(modem):
    at_cmd = "AT%STATUS"
    modem.send_command(at_cmd)

def reset(modem):
    at_cmd = "AT%RESET"
    modem.send_command(at_cmd)
    
def acoustic_release_control(modem, destination, retry, command, releaser_id):
    at_cmd = f"AT%RELEASE{destination},{retry},{command},{releaser_id}"
    modem.send_command(at_cmd)
    
def check_battery_voltage(modem, destination, retry):
    at_cmd = f"AT%VOLTAGE{destination},{retry}"
    modem.send_command(at_cmd)
    
def check_pressure_sensor_data(modem, destination, retry):
    at_cmd = f"AT%PRESSURE{destination},{retry}"
    modem.send_command(at_cmd)
    
def check_ahrs_data(modem, destination, retry):
    at_cmd = f"AT%AHRS{destination},{retry}"
    modem.send_command(at_cmd)
    
def check_optocoupler_control(modem, destination, retry):
    at_cmd = f"AT%VOLTAGE{destination},{retry},check"
    modem.send_command(at_cmd)
    
def set_optocoupler_control(modem, destination, retry, state, timeout):
    at_cmd = f"AT%VOLTAGE{destination},{retry},set,{state},{timeout}"
    modem.send_command(at_cmd)
    
def change_remote_setting(modem, destination, retry, setting, value):
    at_cmd = f"AT%CONFIG{destination},{retry},{setting},{value}"
    modem.send_command(at_cmd)