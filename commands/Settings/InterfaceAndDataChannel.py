def get_global_settings_control(modem):
    at_cmd = "AT?CTRL"
    modem.send_command(at_cmd)

def enable_global_settings_control(modem):
    at_cmd = "AT@CTRL"
    modem.send_command(at_cmd)

def get_external_protocol_mode(modem):
    at_cmd = "AT?ZF"
    modem.send_command(at_cmd)

def set_external_protocol_mode(modem, n):
    at_cmd = f"AT@ZF{n}"
    modem.send_command(at_cmd)

def get_notifications_control(modem):
    at_cmd = "AT?ZB"
    modem.send_command(at_cmd)

def set_notifications_control(modem, n):
    at_cmd = f"AT@ZB{n}"
    modem.send_command(at_cmd)

def get_extended_notifications_control(modem):
    at_cmd = "AT?ZX"
    modem.send_command(at_cmd)

def set_extended_notifications_control(modem, n):
    at_cmd = f"AT@ZX{n}"
    modem.send_command(at_cmd)

def get_pool_size(modem):
    at_cmd = "AT?ZL"
    modem.send_command(at_cmd)

def set_pool_size(modem, n):
    at_cmd = f"AT@ZL{n}"
    modem.send_command(at_cmd)

def get_drop_counter(modem):
    at_cmd = "AT?ZD"
    modem.send_command(at_cmd)

def reset_drop_counter(modem):
    at_cmd = "AT@ZD"
    modem.send_command(at_cmd)

def get_overflow_counter(modem):
    at_cmd = "AT?ZO"
    modem.send_command(at_cmd)

def reset_overflow_counter(modem):
    at_cmd = "AT@ZO"
    modem.send_command(at_cmd)

def get_position_data_output_setting(modem):
    at_cmd = "AT?ZU"
    modem.send_command(at_cmd)

def set_position_data_output_setting(modem, n):
    at_cmd = f"AT@ZU{n}"
    modem.send_command(at_cmd)

def get_external_clock_output_setting(modem):
    at_cmd = "AT?ZA"
    modem.send_command(at_cmd)

def set_external_clock_output_setting(modem, n):
    at_cmd = f"AT@ZA{n}"
    modem.send_command(at_cmd)

def get_external_clock_output(modem):
    at_cmd = "AT?ECLK"
    modem.send_command(at_cmd)