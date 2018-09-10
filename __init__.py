from mycroft import MycroftSkill, intent_file_handler


class MeterData(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('data.meter.intent')
    def handle_data_meter(self, message):
        self.speak_dialog('data.meter')


def create_skill():
    return MeterData()

