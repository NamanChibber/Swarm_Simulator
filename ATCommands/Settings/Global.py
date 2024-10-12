def get_source_level(modem):
    at_cmd = "AT?L"
    modem.send_command(at_cmd)
    
def set_source_level(modem, n):
    at_cmd = f"AT!L{n}"
    modem.send_command(at_cmd)
    
def get_source_level_control(modem):
    at_cmd = "AT?LC"
    modem.send_command(at_cmd)
    
def set_source_level_control(modem, n):
    at_cmd = f"AT!LC{n}"
    modem.send_command(at_cmd)
    
def get_gain(modem):
    at_cmd = "AT?G"
    modem.send_command(at_cmd)
    
def set_gain(modem, n):
    at_cmd = f"AT!G{n}"
    modem.send_command(at_cmd)
    
def get_carrier_waveform_id(modem):
    at_cmd = "AT?C"
    modem.send_command(at_cmd)
    
def set_carrier_waveform_id(modem, n):
    at_cmd = f"AT!C{n}"
    modem.send_command(at_cmd)
    
def get_local_address(modem):
    at_cmd = "AT?AL"
    modem.send_command(at_cmd)
    
def set_local_address(modem, n):
    at_cmd = f"AT!AL{n}"
    modem.send_command(at_cmd)
    
def get_highest_address(modem):
    at_cmd = "AT?AM"
    modem.send_command(at_cmd)
    
def set_highest_address(modem, n):
    at_cmd = f"AT!AM{n}"
    modem.send_command(at_cmd)
    
def get_cluster_size(modem):
    at_cmd = "AT?ZC"
    modem.send_command(at_cmd)
    
def set_cluster_size(modem, n):
    at_cmd = f"AT!ZC{n}"
    modem.send_command(at_cmd)
    
def get_packet_time(modem):
    at_cmd = "AT?ZP"
    modem.send_command(at_cmd)
    
def set_packet_time(modem, n):
    at_cmd = f"AT!ZP{n}"
    modem.send_command(at_cmd)
    
def get_retry_count(modem):
    at_cmd = "AT?RC"
    modem.send_command(at_cmd)
    
def set_retry_count(modem, n):
    at_cmd = f"AT!RC{n}"
    modem.send_command(at_cmd)
    
def get_retry_timeout(modem):
    at_cmd = "AT?RT"
    modem.send_command(at_cmd)
    
def set_retry_timeout(modem, n):
    at_cmd = f"AT!RT{n}"
    modem.send_command(at_cmd)
    
def get_keep_online_count(modem):
    at_cmd = "AT?KO"
    modem.send_command(at_cmd)
    
def set_keep_online_count(modem, n):
    at_cmd = f"AT!KO{n}"
    modem.send_command(at_cmd)
    
def get_idle_timeout(modem):
    at_cmd = "AT?ZI"
    modem.send_command(at_cmd)
    
def set_idle_timeout(modem, n):
    at_cmd = f"AT!ZI{n}"
    modem.send_command(at_cmd)
    
def get_channel_protocol_id(modem):
    at_cmd = "AT?PID"
    modem.send_command(at_cmd)
    
def set_channel_protocol_id(modem, n):
    at_cmd = "AT!PID{n}"
    modem.send_command(at_cmd)
    
def get_interface_list(modem):
    at_cmd = "AT?ZSL"
    modem.send_command(at_cmd)
    
def get_system_time(modem):
    at_cmd = "AT?UT"
    modem.send_command(at_cmd)
    
def set_system_time(modem, n):
    at_cmd = f"AT!UT{n}"
    modem.send_command(at_cmd)
    
def get_system_clock(modem):
    at_cmd = "AT?CLOCK"
    modem.send_command(at_cmd)
    
def get_system_time_and_clock(modem):
    at_cmd = "AT?UTX"
    modem.send_command(at_cmd)
    
def get_sound_speed(modem):
    at_cmd = "AT?CA"
    modem.send_command(at_cmd)
    
def set_sound_speed(modem, n):
    at_cmd = f"AT!CA{n}"
    modem.send_command(at_cmd)
    
def get_im_retry_count(modem):
    at_cmd = "AT?RI"
    modem.send_command(at_cmd)
    
def set_im_retry_count(modem, n):
    at_cmd = f"AT!RI{n}"
    modem.send_command(at_cmd)

def get_promiscuous_mode(modem):
    at_cmd = "AT?RP"
    modem.send_command(at_cmd)

def set_promiscuous_mode(modem, n):
    at_cmd = f"AT!RP{n}"
    modem.send_command(at_cmd)

def get_transmissions_mode(modem):
    at_cmd = "AT?TX"
    modem.send_command(at_cmd)

def set_transmissions_mode(modem, n):
    at_cmd = f"AT!TX{n}"
    modem.send_command(at_cmd)