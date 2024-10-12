def get_local_to_remote_bitrate(modem):
    at_cmd = "AT?BL"
    modem.send_command(at_cmd)

def get_remote_to_local_bitrate(modem):
    at_cmd = "AT?BR"
    modem.send_command(at_cmd)

def get_rssi(modem):
    at_cmd = "AT?E"
    modem.send_command(at_cmd)

def get_signal_integrity_level(modem):
    at_cmd = "AT?I"
    modem.send_command(at_cmd)

def get_propogation_time(modem):
    at_cmd = "AT?T"
    modem.send_command(at_cmd)

def get_relative_velocity(modem):
    at_cmd = "AT?V"
    modem.send_command(at_cmd)

def get_multipath_structure(modem):
    at_cmd = "AT?P"
    modem.send_command(at_cmd)

def get_noise_sample(modem):
    at_cmd = "AT?NOISE"
    modem.send_command(at_cmd)
