from mycroft import MycroftSkill
from mycroft.util import play_audio_file
import random

class TextToBeep(MycroftSkill):
    def initialize(self):
        self.add_event("recognizer_loop:record_end", self.end_recording_sound)
        self.add_event("speak", self.play_sound)

    print('Loading Communication Relay...')
    
    def end_recording_sound(self, message):
        play_audio_file("/home/alex/mycroft-core/mycroft/res/snd/BD1_end_listening.wav")
    
    def play_sound(self, message):
        
        speak_text = str(message.data.get('utterance'))
        speak_len = len(speak_text)
        
        print("There are {} characters in this sentence.".format(speak_len))
        
        if speak_len <= 15:
            number = random.randint(1,46)
            play_audio_file(
            "/home/alex/mycroft-core/mycroft/res/snd/BD1/Sounds/BD1_Sounds_{}.wav".format(number)
            ) 
        elif speak_len > 15:
            number = random.randint(1,19)
            play_audio_file(
            "/home/alex/mycroft-core/mycroft/res/snd/BD1/Talking/BD1_Talking_{}.wav".format(number)
            )

def create_skill():
    return TextToBeep()

