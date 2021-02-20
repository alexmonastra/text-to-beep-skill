from mycroft import MycroftSkill
from mycroft.util import play_audio_file
import random

class TextToBeep(MycroftSkill):
    def initialize(self):
        self.add_event("recognizer_loop:record_end", self.end_recording_sound)
        self.add_event("speak", self.play_sound)

    print('Loading Communication Relay...')
    
    def end_recording_sound(self, message):
        play_audio_file("/home/alex/mycroft-core/mycroft/res/snd/end_listening.wav")
    
    def play_sound(self, message):
        number = random.randint(1,11)
        play_audio_file(
            "/home/alex/mycroft-core/mycroft/res/snd/bd1clips/BD-1 Clip {}.wav".format(number)
            )

def create_skill():
    return TextToBeep()

