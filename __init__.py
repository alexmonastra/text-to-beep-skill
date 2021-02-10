from mycroft import MycroftSkill, intent_file_handler


class TextToBeep(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('beep.to.text.intent')
    def handle_beep_to_text(self, message):
        self.speak_dialog('beep.to.text')


def create_skill():
    return TextToBeep()

