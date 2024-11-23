class OK:
    def __init__(self, *args):
        self.msg = args[0]

class BUSY:
    def __init__(self, *args):
        self.msg = args
        
class ERROR:
    def __init__(self, *args):
        self.msg = args

class RECVIM:
    def __init__(self, *args):
        self.destination_pid = None

        if len(args) == 10:
            self.destination_pid = args[0]
            args = args[1:]
            
        self.length = args[0]
        self.source = args[1]
        self.destination = args[2]
        self.flag = args[3]
        self.duration = args[4]
        self.rssi = args[5]
        self.integrity = args[6]
        self.velocity = args[7]
        self.data = args[8]
            
class RECVIMS:
    def __init__(self, *args):
        self.destination_pid = None

        if len(args) == 10:
            self.destination_pid = args[0]
            args = args[1:]
            
        self.length = args[0]
        self.source = args[1]
        self.destination = args[2]
        self.timestamp = args[3]
        self.duration = args[4]
        self.rssi = args[5]
        self.integrity = args[6]
        self.velocity = args[7]
        self.data = args[8]
        
class RECVPBM:
    def __init__(self, *args):
        self.destination_pid = None

        if len(args) == 9:
            self.destination_pid = args[0]
            args = args[1:]
            
        self.length = args[0]
        self.source = args[1]
        self.destination = args[2]
        self.duration = args[3]
        self.rssi = args[4]
        self.integrity = args[5]
        self.velocity = args[6]
        self.data = args[7]
        
class DELIVEREDIM:
    def __init__(self, *args):
        self.destionation = args[0]