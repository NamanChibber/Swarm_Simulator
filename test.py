import ATCommands.Help as Help
import ATCommands.General as General
import ATCommands.DataControl as DataControl
import ATCommands.Status as Status

import ATCommands.Settings.WakeUpModule as WakeUpModule

from Modem import Modem

host_ip = "10.78.31."
port = 9200
node_id = 1

modem = Modem(host_ip+str(node_id), port)

Help.see_command_format(modem, "*SENDIMS")
General.clear_transmission_buffer(modem)
DataControl.send_instant_message(modem, 4, 2, "ack", "test")
DataControl.instant_message_delivery_status(modem)
Status.battery_voltage(modem)

modem.close()