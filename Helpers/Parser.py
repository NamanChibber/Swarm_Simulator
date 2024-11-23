from Helpers.MessageFormat import *

def parser(msg):
    rmsg = msg
    msg = msg.split(':',2)[2].split(",")
    
    if "OK" == msg[0]:
        recv = OK(rmsg.split(":")[0])
    elif "ERROR" in msg[0]:
        recv = ERROR(rmsg.split(" ", 1)[1])
    elif "BUSY" in msg[0]:
        recv = BUSY(rmsg.split(" ", 1)[1])
    elif msg[0] == "RECVIM":
        recv = RECVIM(*msg[1:])
    elif msg[0] == "RECVIMS":
        recv = RECVIMS(*msg[1:])
    elif msg[0] == "RECVPBM":
        recv = RECVPBM(*msg[1:])
    elif msg[0] == "DELIVEREDIM":
        recv = DELIVEREDIM(*msg[1:])
    else:
        recv = rmsg
        
    return recv