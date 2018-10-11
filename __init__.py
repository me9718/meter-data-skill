from mycroft import MycroftSkill, intent_file_handler
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

LOGGER = getLogger(__name__)

class MeterData(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('data.meter.intent')
    def handle_data_meter(self, message):
        self.speak_dialog('data.meter')


def create_skill():
    return MeterData()

