import socket
from threading import Thread
from mycroft import MycroftSkill, intent_file_handler


class MeterDataSkill(MycroftSkill):
    def __init__(self):
        super(MeterDataSkill, self).__init__(name="MeterDataSkill")
        self.clientmsg = ""
        self.is_shutdown = False
        # Start a thread running the server accepting connections
        self.thread = Thread(target=self.main_server)
        self.thread.start()
    
    def main_server():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # Listen on localhost, port 7724
            s.bind(("127.0.0.1", 7724))

        except socket.error as msg:
            self.log.info("error occured")
            return False

        # This code is not threaded
        # and can ONLY handle one connected
        # client at a time
        s.listen(1)

        self.log.info("socket created")

        # Loop forever
        while not self.is_shutdown:
            # A new client connected
            conn, addr = s.accept()
            self.log.info("client connected", conn)

            # Receive at most 1024 bytes and store in the class.
            self.clientmsg = conn.recv(1024) 
            self.log.info("data received from client: ", clientmsg)

            # Echo back the received data to the client
            conn.send(clientmsg)
            self.log.info("clientmsg echoed back")

            # Close connection to the client
            conn.close()

        s.close()
        #return self.clientmsg
    
    @intent_file_handler('data.meter.intent')
    def handle_data_meter(self, message):
        meter_type = message.data.get('type')
        # Get last data received by server
        meter_value = self.clientmsg
        self.speak_dialog('data.meter', data={'type':meter_type, 'value':meter_value})
    
    
def create_skill():
    return MeterDataSkill()
