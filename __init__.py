from mycroft import MycroftSkill, intent_file_handler
#from mycroft import intent_handler
#from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
import socket

LOGGER = getLogger(__name__)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind(("192.168.1.103",5564))
except socket.error as msg:
	print("error occured")

print("socket created")
s.listen(10)

while True:
    conn, addr = s.accept()
    print("client connected")

    data = conn.recv(1024)
    print("data received from client: ", data.decode('utf-8'))
    
    if data is not None:

        class MeterDataSkill(MycroftSkill):
            def __init__(self):
                super(MeterDataSkill, self).__init__(name="MeterDataSkill")
    
            result = data.decode('utf-8')
            @intent_file_handler('data.meter.intent')
            def handle_data_meter(self, message):
                meter_type = message.data.get('type')
                meter_value = self.result
                print ("value: ", self.socket_server())
                self.speak_dialog('data.meter', data={'type':meter_type, 'value':meter_value})
    
    #def stop(self):
        #pass
        #return False        

    else:break
    def create_skill():
        return MeterDataSkill()
conn.close()
s.close()
