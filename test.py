import commands.help as help
import commands.general as general
import commands.datacontrol as datacontrol

from modem import Modem

host_ip = "10.78.31.1"
port = 9200
nodes = 3

modem = Modem(host_ip, port)

help.see_command_format(modem, "*SENDIMS")
general.clear_transmission_buffer(modem)
datacontrol.send_instant_message(modem, 4, 2, "ack", "test")